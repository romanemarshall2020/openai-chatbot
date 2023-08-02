import React from 'react'
import ReactDOM from 'react-dom/client'
import './index.css'
import { initializeIcons } from '@fluentui/react'
// import App from './App';
import { HashRouter, Route, Routes } from 'react-router-dom'
import Chat from './pages/chat/Chat'


initializeIcons();

export default function App() {
  return (
    <HashRouter>
      <Routes>
        <Route path="/" >
          <Route index element={<Chat/>}></Route>
        </Route>
      </Routes>
    </HashRouter>
  )
}

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
