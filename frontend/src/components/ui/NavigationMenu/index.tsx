import { Flex, Image } from "@chakra-ui/react"
import { Link } from "react-router-dom"
const NavigationMenu: React.FC = () => {
    return (
        <Flex as="nav" background="#212525" width="100%" color="white" borderRadius="lg" justifyContent="space-between" px="5" py="4">
            <Image src="/logo.png" alt="Bobyard" width="100px" />
            <Flex direction="row" padding="1" fontWeight="bold" gap="6">
                <Link to="/">Comments</Link>
                <Link to="/improvements">Improvements</Link>
            </Flex>
        </Flex>
    )
}

export default NavigationMenu