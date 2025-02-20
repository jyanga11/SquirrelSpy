import React from 'react'
import './style/mian.css'

const Edit = () =>{
    return(
        <div>
            <div className="header">
                <div className="logo">
                    <p className="title"> SquirrelSpy</p>
                </div>

                <div className="add-btn">
                    <a className="" href='/export'> Export</a>
                </div>

                <div className="add-btn">
                    <a className="" href='/moderate'> Moderate</a>
                </div>

                <div className="add-btn">
                    <a className="" href='/verity'> Verify</a>
                </div>

                <div className="add-btn">
                    <a className="" href='/edit'> Edit</a>
                </div>
            </div>

             <div className="container">
                <ul className="list">
                    <li>Item 1</li>
                    <li>Item 2</li>
                    <li>Item 3</li>
                    <li>Item 4</li>
                    {/* Add more list items as needed */}
                </ul>
            </div>
        </div>
    )

}


export default Edit;