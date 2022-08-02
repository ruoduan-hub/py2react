import React, { useEffect, useState } from 'react';
import './App.css';

function App() {

  const [data, setData] = useState<{ title?: string, info?: string }>({})

  const getName = async () => {
    const response: Response = await fetch('http://localhost:5000/hello')
    if (!response?.ok) {
      throw new Error(`错误代码：${response.status}`);
    }

    response.json().then(res => {

      setData(res)
    })

    console.log()
  }

  const gifAction = () => {
    let ig = new Image(1, 11)
    ig.src = 'http://localhost:5000/mgtest.gif?name=啊啊啊啊啊'
    document.querySelector('#root')?.appendChild(ig)

  }


  useEffect(() => {
    getName()
  }, [])

  return (
    <div className="App">
      <h1>{data.title}</h1>
      <p dangerouslySetInnerHTML={{ __html: data.info as string }}></p>
      <button onClick={gifAction}>gif埋点</button>
    </div>
  );
}

export default App;
