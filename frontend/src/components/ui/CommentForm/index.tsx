import { Button, Grid, Text, Textarea, VStack } from "@chakra-ui/react"
import { useState } from "react"
interface CommentFormProps {
    onSubmit: (text: string) => void
}

const CommentForm: React.FC<CommentFormProps> = ({ onSubmit }) => {
    const [text, setText] = useState('')
    return (
        <Grid templateColumns="repeat(1, 1fr)" gap="6" backgroundColor="var(--chakra-colors-bg-panel)" p="4" borderRadius="lg" w="100%">
            <VStack alignItems="flex-start">
                <Text fontSize="md">Add a comment</Text>
                <Textarea value={text} onChange={(e) => setText(e.target.value)} borderWidth="1px" borderColor="var(--chakra-colors-border-panel)" />
            </VStack>

            <Button onClick={() => { onSubmit(text); setText('') }} disabled={text.length === 0} colorPalette={'blue'} >Submit</Button>
        </Grid >
    )
}

export default CommentForm