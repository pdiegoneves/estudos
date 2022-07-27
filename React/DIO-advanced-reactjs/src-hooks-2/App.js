import React, { useState, useEffect } from 'react'
import { ThemeContext, themes } from './Theme'
import Card from './Card'

function App () {
  const [token, setToken] = useState()
  
  useEffect(() => {
    setTimeout(() => {
      setToken('31a5s6d54as5d1')
    }, 4000)
  }, [setToken])

  return (
    <ThemeContext.Provider value={themes.primary}>
      <Card />
    </ThemeContext.Provider>
  )
}

export default App