import { Card, List, Box } from '@chakra-ui/react'
import React from 'react'
import { LuCircleDashed } from 'react-icons/lu'

const About: React.FC = () => {
    const items = [
        'Get list of users who liked the comment so it can be unliked',
        'Better error handling for body request',
        'Pass user_id through token instead of body',
        'Responsive design',
        'Testing (or not)',
        'Set query data on comments change instead of invalidating the query',
        'Handle on load, on error when retrieving comments',
        'Handle on load, on error when editing comment',
        'Put styles in a separate file and clean up the code',
        'Improve design'
    ]
    return (
        <Card.Root p="4" borderRadius="lg">
            <Card.Title textAlign="center" mb="4">TODO List</Card.Title>
            <List.Root gap="2" maxW="600px" mx="auto">
                {items.map((item) => (
                    <List.Item key={item} display="flex" alignItems="center">
                        <Box color="var(--chakra-colors-blue-700)" mr="2">
                            <LuCircleDashed />
                        </Box>
                        {item}
                    </List.Item>
                ))}
            </List.Root>
        </Card.Root>
    )
}

export default About 