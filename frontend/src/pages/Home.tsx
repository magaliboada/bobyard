import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query'
import React from 'react'
import { Comment, CommentUpdate } from '../types'
import { Flex, Grid, Text } from '@chakra-ui/react'
import CommentCard from '../components/ui/CommentCard'
import CommentForm from '../components/ui/CommentForm'

const Home: React.FC = () => {
    const queryClient = useQueryClient()
    const { data } = useQuery({
        queryKey: ['comments'],
        queryFn: () => fetch('http://localhost:3000/comments').then(res => res.json())
    })

    const { mutate: deleteComment } = useMutation({
        mutationFn: (id: string) => fetch(`http://localhost:3000/comments/${id}`, {
            method: 'DELETE'
        }).then(() => {
            queryClient.invalidateQueries({ queryKey: ['comments'] })
        })
    })

    const { mutate: editComment } = useMutation({
        mutationFn: (comment: CommentUpdate) => fetch(`http://localhost:3000/comments/${comment.id}`, {
            method: 'PATCH',
            body: JSON.stringify(comment)
        }).then(() => {
            queryClient.invalidateQueries({ queryKey: ['comments'] })
        })
    })

    const { mutate: likeComment } = useMutation({
        mutationFn: (id: string) => fetch(`http://localhost:3000/comments/${id}/like`, {
            method: 'POST',
            body: JSON.stringify({
                user_id: 'b1d7c8e9-4f2d-4a1f-8b5d-9e2c3a4f6d7e'
            })
        }).then(() => {
            queryClient.invalidateQueries({ queryKey: ['comments'] })
        })
    })

    const { mutate: createComment } = useMutation({
        mutationFn: (text: string) => fetch(`http://localhost:3000/comments`, {
            method: 'POST',
            body: JSON.stringify({ text: text, user_id: 'b1d7c8e9-4f2d-4a1f-8b5d-9e2c3a4f6d7e' })
        }).then(() => {
            queryClient.invalidateQueries({ queryKey: ['comments'] })
        })
    })
    const handleEdit = (comment: CommentUpdate) => {
        editComment(comment)
    }

    const handleDelete = (id: string) => {
        deleteComment(id)
    }

    const handleLike = (id: string) => {
        likeComment(id)
    }

    const handleSubmit = (text: string) => {
        createComment(text)
    }

    return (
        <Grid gap="5">
            <Flex flexDirection="column" alignItems="center">
                <Text fontSize="4xl" fontWeight="bold" color="white" textAlign="center">Comment section</Text>
                <Text fontSize="sm" color="white" textAlign="center">
                    {data?.length} comments found
                </Text>
            </Flex>
            <Grid templateColumns="repeat(1, 1fr)" gap="6" mx="auto" maxW="600px">
                <CommentForm onSubmit={handleSubmit} />
                {data?.map((comment: Comment) => (
                    <CommentCard comment={comment} onEdit={handleEdit} onDelete={handleDelete} onLike={handleLike} key={comment.id} />
                ))}
            </Grid>
        </Grid>
    )
}

export default Home 