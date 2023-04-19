import Footer from './components/layout/Footer'
import Navbar from './components/layout/Navbar'
import './globals.css'


export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head />
      <body className=' bg-zinc-200 text-black'>
        <Navbar />
        {children}
        <Footer />
      </body>
    </html>
  )
}
