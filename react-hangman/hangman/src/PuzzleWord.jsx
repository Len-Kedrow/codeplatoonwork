import React, { useState } from 'react';
import axios from "axios";

const baseUrl = "https://random-word-api.herokuapp.com/word"

function PuzzleWord() {
    const theWord= () => { axios.get(baseUrl,[,config])}
    
    //const [blanks, setBlanks] = useState(Array(theWord.length).fill("*"))
    //const wordArray = theWord.slice()
    // {wordArray}
    //             {blanks}
    return(
        
        <div>
                <p>this is {theWord}</p>
                
        </div>
        
    )
}

export default PuzzleWord