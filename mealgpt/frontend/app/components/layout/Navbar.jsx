import Link from 'next/link'
import React from 'react'

const Navbar = () => {
  return (
    <div className=' w-full h-12 flex flex-row py-1 px-4 space-x-11'>
        <Link href='/' className=' font-semibold text-lg' >MealGPT</Link>
        <Link href='/login' className='  text-lg' >Login</Link>
        <Link href='/register' className='  text-lg' >REggie</Link>
        <Link href='/' className='  text-lg' >MealGPT</Link>
    </div>
  )
}

export default Navbar