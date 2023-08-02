import './chat.module.css'
import React from 'react'

const Chat = () => {
  return (
    <><>
      <div className='app'>
        <div className='header'> 
          <div className='sidebar-button'>

          </div>
        </div>
        <div className='chat-body'>
        <div className='input'>
          <form className='input' action="">
            <input type="text" name="input-box" id="field" placeholder='Ask me a question' />
            <input type="button" value="submit" />
          </form>
        </div>
        </div>
     
      </div>
    </></>
  )
}

export default Chat;


