import React, { useState } from 'react'
import axios from 'axios'

function PokeToy() {
  
  axios.get("https://pokeapi.co/api/v2/pokemon/ditto").then(res =>{
setPokemon(res.data.results.map(p => p.name))

  })
  const [pokemon, setPokemon] = useState([])
  
  
  return (
    <div>PokeToy</div>
  )
}

export default PokeToy

    
   



    