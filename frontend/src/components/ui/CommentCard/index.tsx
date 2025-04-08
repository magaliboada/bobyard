import { Comment, CommentUpdate } from "@/types"
import { Avatar, Box, Card, Flex, HStack, IconButton, Image } from "@chakra-ui/react"
import ContextualMenu, { MenuItem } from "../ContextualMenu"
import { useState } from "react"
import { HiExclamation, HiHeart, HiOutlineArrowsExpand } from "react-icons/hi"
import { Tooltip } from "../tooltip"
import { getRelativeTime } from "../../../utils/date"
import ConfirmDialog from "../ConfirmDialog"
import { expandIconStyle } from "./styles"
import { imageStyle } from "./styles"
import EditableText from "../EditableText"
import PreviewDialog from "../PreviewDialog"


interface CommentCardProps {
    comment: Comment
    onEdit: (comment: CommentUpdate) => void
    onDelete: (id: string) => void
    onLike: (id: string) => void
}

const CommentCard: React.FC<CommentCardProps> = ({ comment, onEdit, onDelete, onLike }) => {
    const { id, text, user, created_at, image_url, likes_count } = comment
    const [imageError, setImageError] = useState(false)

    const menuItems: MenuItem[] = [
        { label: "Edit", onClick: () => setIsEditing(true) },
        { label: "Delete", onClick: () => setIsDeleteOpen(true) },
    ]

    const timeAgo = getRelativeTime(created_at)
    const [isPreviewImageOpen, setIsPreviewImageOpen] = useState(false)
    const [isDeleteOpen, setIsDeleteOpen] = useState(false)
    const [isEditing, setIsEditing] = useState(false)

    return (
        <Card.Root borderRadius="lg" display="flex" flexDirection="row" gap="2">
            <Box w="100%">
                <Card.Body display="flex" flexDirection="row" gap="5" justifyContent="space-between">
                    {!imageError && image_url &&
                        <Box display="flex" flexDirection="column" gap="2" position="relative">
                            <Image
                                {...imageStyle}
                                src={image_url}
                                alt={user.name}
                                onError={() => setImageError(true)}
                                onClick={() => setIsPreviewImageOpen(true)}
                            />
                            <Box {...expandIconStyle}>
                                <HiOutlineArrowsExpand />
                            </Box>
                        </Box>
                    }

                    <Card.Description w="100%">
                        <HStack justifyContent="space-between" alignItems="center">
                            <HStack gap="3" alignItems="center">
                                <Avatar.Root size="sm">
                                    <Avatar.Image src={'https://i.pravatar.cc/150?img=' + user.id} />
                                </Avatar.Root>
                                <HStack gap="2" alignItems="baseline">
                                    <Card.Title fontSize="xl">{user.name}</Card.Title>
                                    <Tooltip content={created_at.toLocaleString()} openDelay={0}>
                                        <Box fontSize="sm" color="gray.500">
                                            · {timeAgo}
                                        </Box>
                                    </Tooltip>
                                </HStack>
                            </HStack>
                            <ContextualMenu menuItems={menuItems || []} />
                        </HStack>
                        <Box mt="2">
                            <EditableText
                                text={text}
                                isEditing={isEditing}
                                onSave={(newText) => onEdit({ id, text: newText })}
                                setIsEditing={setIsEditing}
                            />
                        </Box>
                    </Card.Description>

                </Card.Body>
                <Card.Footer>
                    <Flex gap="2" justifyContent={imageError ? "space-between" : "end"} w="100%" alignItems="baseline">
                        {imageError &&
                            <Tooltip content={'Error loading image'} openDelay={0}>
                                <HiExclamation size={20} />
                            </Tooltip>}
                        <IconButton variant="ghost" height="auto" onClick={() => onLike(id)}>
                            <HiHeart color={likes_count ? 'var(--chakra-colors-blue-700)' : ''} /> {likes_count || ""}
                        </IconButton>
                    </Flex>
                </Card.Footer>
            </Box>

            <PreviewDialog isOpen={isPreviewImageOpen} setIsOpen={setIsPreviewImageOpen}>
                <Image src={image_url} alt={user.name} w="100%" h="100%" objectFit="contain" />
            </PreviewDialog>

            <ConfirmDialog title="Delete comment" description="Are you sure you want to delete this comment?"
                onConfirm={() => { onDelete(id); setIsDeleteOpen(false) }} onCancel={() => setIsDeleteOpen(false)}
                isOpen={isDeleteOpen} setIsOpen={setIsDeleteOpen} />


        </Card.Root >
    )
}

export default CommentCard