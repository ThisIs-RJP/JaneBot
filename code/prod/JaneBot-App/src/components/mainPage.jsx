import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div className="App">
    {isMobile ? (
        <>
        {/* <MobileNav /> */}
        {/* <MobileComp1 /> */}
        <Nav />
        </>
    ) : (
        <>
        <Nav />
        <Comp1 />
        </>
    )}
    </div>
  )
}

export default App
