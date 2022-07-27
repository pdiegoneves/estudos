import React, { useState } from 'react'
import Button from './Component/Button'
import Calc from './Component/Calc'


function App() {

  const [value, setValue] = useState(0)
  const [min, setMin] = useState(0)
  const [max, setMax] = useState(30)

  const handleClick = () => {
    console.log('adicionado no carrinho')
    setMin(10)
  }
  const handleCalc = ({ target }) => {
    const value = parseInt(target.value)
    setValue(min + max + value)
  }

  return (
    <>
      <div>
        <Button
          onClick={handleClick}
        >
          Adicionar Carrinho
    </Button>
      </div>
      <div>
        <h1>Valor Calculado {value}</h1>
        <Calc
          min={min}
          max={max}
          onChange={handleCalc}
        />
      </div>
    </>
  )
}

export default App