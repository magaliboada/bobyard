import { Button, Dialog } from "@chakra-ui/react"

interface ConfirmDialogProps {
    title: string
    description: string
    onConfirm: () => void
    onCancel: () => void
    isOpen: boolean
    setIsOpen: (isOpen: boolean) => void
}

const ConfirmDialog: React.FC<ConfirmDialogProps> = ({ title, description, onConfirm, onCancel, isOpen, setIsOpen }) => {
    return (
        <Dialog.Root open={isOpen} onOpenChange={() => setIsOpen(!isOpen)} placement="center">
            <Dialog.Backdrop />
            <Dialog.Positioner>
                <Dialog.Content p="5">
                    <Dialog.Title>{title}</Dialog.Title>
                    <Dialog.Description>{description}</Dialog.Description>
                    <Dialog.CloseTrigger />
                    <Dialog.Footer mt="5">
                        <Button onClick={onCancel}>Cancel</Button>
                        <Button onClick={onConfirm}>Confirm</Button>
                    </Dialog.Footer>
                </Dialog.Content>
            </Dialog.Positioner>
        </Dialog.Root>
    )
}

export default ConfirmDialog