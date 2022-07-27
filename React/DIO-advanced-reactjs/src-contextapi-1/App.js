import React, { Component } from 'react'
import { ThemeContext, themes } from './Theme'
import Card from './Card'

function App () {
  return (
    <ThemeContext.Provider value={themes.primary}>
      <Card />
    </ThemeContext.Provider>
  )
}

export default App