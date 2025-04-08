import { BrowserRouter, Routes, Route } from 'react-router-dom'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import Home from './pages/Home'
import NavigationMenu from './components/ui/NavigationMenu'
import About from './pages/About'
import { Box, Container } from '@chakra-ui/react'
const queryClient = new QueryClient()

const App: React.FC = () => {
    return (
        <QueryClientProvider client={queryClient}>
            <BrowserRouter>
                <Container maxWidth="1200px" p={4}>
                    <Box zIndex="-1" bgGradient="to-r" gradientFrom="#00419c" gradientTo="#04041d" height="100vh" position="fixed" top={0} left={0} right={0} bottom={0}>
                    </Box>
                    <NavigationMenu />
                    <Container my="4" px="2">
                        <Routes>
                            <Route path="/" element={<Home />} />
                            <Route path="/improvements" element={<About />} />
                        </Routes>
                    </Container>
                </Container>
            </BrowserRouter>
        </QueryClientProvider >
    )
}

export default App 