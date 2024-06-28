import { useState } from 'react'
import PokeToy from './PokeToy'
import axios from 'axios'
import MoveIt from './MoveIt'



function App() {
  // const [pokemon, setPokemon] = useState([a, b])
  // const [pokemon, setPokemon] = useState([a, b])

  return (
    <>
      <div><p><PokeToy/></p>
          <p><MoveIt /></p>
      </div>
    </>
  )
}

export default App
