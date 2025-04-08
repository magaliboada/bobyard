import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'
import { Provider } from './components/ui/provider'

const style = document.createElement('style')
style.textContent = `
    :root {
        --chakra-colors-bg-panel: #212525;
        --chakra-colors-fg:rgb(255, 255, 255);
        --chakra-colors-fg-muted: #b0b0b0;
        --chakra-colors-bg-muted: #212525;
        --chakra-colors-color-palette-fg:rgb(255, 255, 255);
        
    }
`
document.head.appendChild(style)





ReactDOM.createRoot(document.getElementById('root')!).render(
    <React.StrictMode>
        <Provider>
            <App />
        </Provider>
    </React.StrictMode>
) 