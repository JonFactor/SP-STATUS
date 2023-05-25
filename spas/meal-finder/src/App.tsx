import { useState } from 'react'
import './App.css'

function App() {
  const [data, setData] = useState([])

  const fetchData = () => {
    fetch("https://world.openfoodfacts.org/discover#reuses")
      .then(response => {
        return response.json()
      })
      .then(data => {
        setData(data)
      })
  }

  return (
    <div className=''>
      <p className=' text-4xl'>TEST - {data}</p>
    </div>
  )
}

export default App
