import { Text, Textarea } from "@chakra-ui/react"
import { useState, useRef, useEffect } from "react"

interface EditableTextProps {
    text: string
    isEditing: boolean
    onSave: (text: string) => void
    setIsEditing: (isEditing: boolean) => void
}

const EditableText: React.FC<EditableTextProps> = ({ text, isEditing, onSave, setIsEditing }) => {
    const [editedText, setEditedText] = useState(text)
    const textareaRef = useRef<HTMLTextAreaElement>(null)

    useEffect(() => {
        if (isEditing && textareaRef.current) {
            setTimeout(() => {
                const textarea = textareaRef.current
                if (textarea) {
                    textarea.focus()
                    textarea.setSelectionRange(textarea.value.length, textarea.value.length)
                }
            }, 0)
        }
    }, [isEditing])

    return (
        <>
            {isEditing &&
                <>
                    <Textarea
                        ref={textareaRef}
                        value={editedText}
                        onChange={(e) => setEditedText(e.target.value)}
                        onKeyDown={(e) => {
                            if (e.key === 'Enter' && !e.shiftKey) {
                                onSave(editedText)
                                setIsEditing(false)
                            }
                            if (e.key === 'Escape') {
                                setIsEditing(false)
                            }
                        }}
                        backgroundColor="gray.700"
                        autoresize
                    />
                    <Text textAlign="center" fontSize="sm" color="gray.500">
                        Press Enter to save or Escape to cancel
                    </Text>
                </>
            }
            {!isEditing &&
                <Text whiteSpace="pre-wrap">{text}</Text>
            }
        </>
    )
}

export default EditableText