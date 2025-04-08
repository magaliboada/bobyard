import { Dialog } from "@chakra-ui/react"

interface PreviewDialogProps {
    isOpen: boolean
    setIsOpen: (isOpen: boolean) => void
    children: React.ReactNode
}

const PreviewDialog: React.FC<PreviewDialogProps> = ({ isOpen, setIsOpen, children }) => {
    return (
        <Dialog.Root open={isOpen} onOpenChange={() => setIsOpen(!isOpen)} placement="center">
            <Dialog.Backdrop />
            <Dialog.Positioner>
                <Dialog.Content>
                    <Dialog.CloseTrigger />
                    <Dialog.Body p="0">
                        {children}
                    </Dialog.Body>
                </Dialog.Content>
            </Dialog.Positioner>
        </Dialog.Root>
    )
}

export default PreviewDialog