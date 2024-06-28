
import React, { useState } from 'react'

function LetterBank() {
    const [alphabet, setAlphabet] = useState(Array.from({length:26}, (_, i) => String.fromCharCode(65+i)))   
    return (
        <div>{alphabet}</div>

    )
}

export default LetterBank