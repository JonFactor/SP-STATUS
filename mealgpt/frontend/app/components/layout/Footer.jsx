import Link from 'next/link'
import React from 'react'

const Footer = () => {
  return (
    <div className=' bg-zinc-400 w-full h-8 flex flex-row space-x-16 px-6 align-middle text-sm py-1 justify-center' >
        <Link href='/' > MealGPT </Link>
        <Link href='/' > About </Link>
        <Link href='/' > Pricing </Link>
        <Link href='/' > Products </Link>
        <Link href='/' > Dependencies </Link>
        <Link href='/' > Contact </Link>
        <Link href='/' > Help Center </Link>
    </div>
  )
}

export default Footer