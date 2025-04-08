import { Portal } from "@chakra-ui/react";

import { Button } from "@chakra-ui/react";

import { Menu } from "@chakra-ui/react";
import { HiDotsVertical } from "react-icons/hi";
import { buttonStyle } from "./styles";
export interface MenuItem {
    label: string
    onClick: () => void
}

interface ContextualMenuProps {
    menuItems: MenuItem[]
}

const ContextualMenu: React.FC<ContextualMenuProps> = ({ menuItems }) => {
    return (
        <Menu.Root>
            <Menu.Trigger asChild>
                <Button size="sm" variant="ghost" {...buttonStyle}>
                    <HiDotsVertical />
                </Button>
            </Menu.Trigger>
            <Portal>
                <Menu.Positioner>
                    <Menu.Content>
                        {menuItems.map((item) => (
                            <Menu.Item cursor="pointer" key={item.label} value={item.label} onClick={() => item.onClick()}>{item.label}</Menu.Item>
                        ))}
                    </Menu.Content>
                </Menu.Positioner>
            </Portal>
        </Menu.Root>
    )
}

export default ContextualMenu