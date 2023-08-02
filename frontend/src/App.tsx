import './App.css'

function App() {


  return (
    <><>
      <div className='app'>
        <div className='header'> 
          <div className="dropdown">
            <button className="dropbtn">Dropdown</button>
              <div id="myDropdown" className="dropdown-content">
                <a href="#">Link 1</a>
                <a href="#">Link 2</a>
                <a href="#">Link 3</a>
            </div>
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

export default App
