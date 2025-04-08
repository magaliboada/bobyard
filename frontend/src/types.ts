export interface User {
    id: string
    name: string
}

export interface Comment {
    id: string
    text: string
    user: User
    created_at: string
    image_url: string
    likes_count: number
}

export interface CommentUpdate extends Pick<Comment, 'id' | 'text'> { }