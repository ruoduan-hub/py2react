import React, { useEffect, useState } from 'react';
import './App.css';

function App() {

  const [data, setData] = useState<{ title?: string, info?: string  }>({})

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


  useEffect(() => {
    getName()
  }, [])

  return (
    <div className="App">
      <h1>{data.title}</h1>
      <p dangerouslySetInnerHTML={{ __html: data.info as string }}></p>
    </div>
  );
}

export default App;
