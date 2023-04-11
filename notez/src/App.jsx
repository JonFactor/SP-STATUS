import { useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import editNoteModal from './components/editNoteModal'
import './App.css'

function App() {

  const colors = ['bg-yellow-200', 'bg-orange-200', 'bg-blue-200', 'bg-green-200', 'bg-red-200']
  const backroundColors = []
  const [wasClicked, setWasClicked] = useState(false)
  const [repositioning, setRepositioning] = useState(false)



  useEffect(() => {
    // cusror following
    const cursor = document.getElementById('cursor')

    document.onmousemove = (e) => {
      const x = e.pageX
      const y = e.pageY
      setTimeout(() => {
        cursor.style.transform = `translate(${x}px, ${y}px)`
      }, [100])
    }

    
    const note = document.getElementById('note')

    // note clicking
    note.onclick = (e) => {
      if (!wasClicked) {
        cursor.style["display"] = "flex"
        cursor.style.backgroundColor = "rgb(254 240 138)"
        setWasClicked(true)
      } else {
        cursor.style["display"] = "none"
        setWasClicked(false)
      }
    }

    const grid = document.getElementById('content')

    // GRID clicking
    grid.onclick = (e) => {

      const placedElement = document.createElement("div")
      // create new
      if (wasClicked) {
        const x = e.offsetX
        const y = e.offsetY

        placedElement.style.width = "170px"
        placedElement.style.height = "200px"
        placedElement.style.backgroundColor = cursor.style.backgroundColor
        placedElement.style.position = "absolute"
        placedElement.style.transform = `translate(${x}px, ${y}px)`
        placedElement.onmousedown = () => {
          setRepositioning(true)
        }

        grid.appendChild(placedElement)

        cursor.style["display"] = "none"
        setWasClicked(false)
        
      }

    }

  })

  return (
    <div>
      <div className=' absolute aspect-square w-8 rounded-md hidden bg-black border-[2px] border-black z-10' id='cursor'/>
      <div id='toolbar' className=' bg-zinc-200 flex flex-row justify-center align-middle w-full h-12 text-lg space-x-6 py-2'>
        <h1>NOTEZ</h1>
        <div>
          <button className=' bg-yellow-200 px-4 rounded-md'>Sticky</button>
        </div>
      </div>
      <div id='right-tool' className=' w-24 h-[500px] ml-4 mx-12 float-left'>
        {colors.map((color) => (
          <div className={` ${color} h-40 w-40 rounded-lg mt-4 ml-2 cursor-pointer `} id='note'/>
        ))}
      </div>
      <div id='content'  
      className=' bg-purple-200 w-3/4 h-[1000px] mx-20 my-12 rounded-lg resize-y grid float-right relative overflow-hidden'
      >
        
      </div>
      <div id='bottom'>

      </div>
    </div>
  )
}

export default App
