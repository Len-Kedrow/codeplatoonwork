//This is a different button component to see the difference in react
import React from "react"

function DifferentButton() {
    const diffPress = () => {
        console.log("this is the different press")
    }
    return( 
        <button onClick={diffPress}>different button</button>
        )
    }

    export default DifferentButton