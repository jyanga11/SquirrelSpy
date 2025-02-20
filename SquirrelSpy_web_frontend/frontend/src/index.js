import React from 'react'
import ReactDOM from 'react-dom/client'
import './style/mian.css'
import App from './App'
import Moderate from './Moderate'
import Verify from './Verify'
import Edit from './Edit'
import Export from './Export'
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";


const router = createBrowserRouter([
  {
    path: "/",
    element: <App/>,
  },
    {
    path: "/moderate",
    element: <Moderate/>,
  },
      {
    path: "/export",
    element: <Export/>,
  },
      {
    path: "/edit",
    element: <Edit/>,
  },
      {
    path: "/verify",
    element: <Verify/>,
  },
]);

const root = ReactDOM.createRoot(document.getElementById('root'))
root.render(
    <RouterProvider router={router} />
)