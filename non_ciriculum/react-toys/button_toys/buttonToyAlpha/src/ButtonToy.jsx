import React, { useState }  from "react";

    

    function ButtonToy() {
            const [count, setCount] = useState(0);
            const sayPressed = () => {console.log("You pressed me")
                setCount(count+1)
            }
          

        return <button onClick={sayPressed}>Press Me {count}</button> 
        };
    
    export default ButtonToy;





