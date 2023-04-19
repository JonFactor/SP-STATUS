import React from 'react'

const page = () => {
  return (
    <div className=' justify-center flex p-12'>
        <div className=' bg-orange-100 w-2/5 h-[600px] rounded-2xl flex flex-col overflow-hidden'>
            <div className=' w-full py-2 justify-center flex bg-purple-200  '>
                <h2 className=' text-3xl '>Login</h2>
            </div>
            <form className='  rounded-md h-full p-4 space-y-8 mt-12 ml-6'>
                <div className=' flex flex-row'>
                    <h3 className=' text-xl'>Email: </h3>
                    <input 
                        className=' ml-6 w-full rounded-md'
                        name='email'
                        type='email'
                        placeholder='JohnSmith@gmail.com'
                    />                    
                </div>
                <div className=' flex flex-row'>
                    <h3 className=' text-xl'>Password: </h3>
                    <input 
                        className=' ml-6 w-full rounded-md'
                        name='pass'
                        type='password'
                        placeholder='drowssaP'
                    />                    
                </div>
                <div className=' w-full justify-center h-fit flex'>
                    <div className=' flex flex-row space-x-8'>
                        <button type='submit' className=' py-2 px-6 bg-zinc-200 rounded-lg'> Submit </button>
                        <button type='button' className=' py-2 px-6 bg-zinc-200 rounded-lg'> Google </button>
                    </div>                    
                </div>

            </form>
        </div>
        
    </div>
  )
}

export default page