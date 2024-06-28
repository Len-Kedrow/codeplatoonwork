
import React, {useState} from 'react'

function UserGuess() {

    const [input, setInput] = useState("")
    const handleInputChange = (event) => {
        setInput(input.current.value)
        event.preventDefault()
    } 
    return (
        <div>
            <form onSubmit={handleInputChange}>
                <input type="text" value={input} onChange={handleInputChange}/>
                <button type= "submit">submit</button>
            </form>
            
            <h3>{input}</h3>

        </div>
    )
}


export default UserGuess

//need an onchage