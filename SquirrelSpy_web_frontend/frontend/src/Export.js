import React from 'react'
import './style/mian.css'
import {useEffect, useState, useRef} from 'react';

const Export = () =>{
    const [squirrels, setSquirrels] = useState([]);

    const getSquirrels = async () => {
            const response = await fetch('/squirrels');
            const json = await response.json();
        if (response.ok) {
            console.log(json);
            setSquirrels(json);
        }
        else{
            console.log('Failed to fetch')
        }
    }

    useEffect(
        () => {
            getSquirrels()
        },[]
    )

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
                    <a className="" href='/verify'> Verify</a>
                </div>

                <div className="add-btn">
                    <a className="" href='/edit'> Edit</a>
                </div>
            </div>

            <div className="container">
                <ul className="horizontal-list">
                    <li>Name:</li>
                    <li>ID:</li>
                    <li>Age:</li>
                    <li>Sex:</li>
                    <li>Species:</li>
                    <li>Serial_num:</li>
                    <li>Weight:</li>
                    <li>Left_ear_color:</li>
                    <li>Right_ear_color:</li>
                    <li>Image:</li>
                </ul>
                <ul className="list">
                    {squirrels.map((squirrel, index) => (
                        <li key={index} className="squirrel-item">
                            <div className="grid-container">
                                <div className="item"><span>{squirrel.name}</span></div>
                                <div className="item"><span>{squirrel.id}</span></div>
                                <div className="item"><span>{squirrel.age}</span></div>
                                <div className="item"><span>{squirrel.sex}</span></div>
                                <div className="item"><span>{squirrel.species}</span></div>
                                <div className="item"><span>{squirrel.serial_num}</span></div>
                                <div className="item"><span>{squirrel.weight}</span></div>
                                <div className="item"><span>{squirrel.left_ear_color}</span></div>
                                <div className="item"><span>{squirrel.right_ear_color}</span></div>
                                <div className="item"><span>{squirrel.image}</span></div>
                            </div>
                        </li>
                    ))}
                </ul>
            </div>
        </div>
    )

}


export default Export;