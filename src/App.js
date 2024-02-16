import React, { useState } from 'react';
import './App.css';

function App() {
  const [file, setFile] = useState(null);
  const [filename, setFilename] = useState(null);
  const [uploadComplete, setUploadComplete] = useState(false);

  const onFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const onFormSubmit = (event) => {
    event.preventDefault();

    const formData = new FormData();
    formData.append('file', file);

    fetch('/api/upload/', {
      method: 'POST',
      body: formData
    })
    .then(response => response.json())
    .then(data => {
      setFilename(data.file_name);
      setUploadComplete(true);
    });
  };

  const downloadFile = async () => {
    const response = await fetch(`/api/download/${filename}`);
    const blob = await response.blob();
    const url = window.URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.setAttribute('download', filename);
    document.body.appendChild(link);
    link.click();
    link.parentNode.removeChild(link);
  };


  return (
    <div className="App">
      <h2 className="title">Upload .hol File</h2>
      <form onSubmit={onFormSubmit} className="upload-form">
        <input type="file" onChange={onFileChange} className="file-input" />
        <button type="submit" className="upload-button">Upload</button>
      </form>
      {uploadComplete && <button onClick={downloadFile} className="download-button">Download .ics File</button>}
    </div>
  );
}

export default App;
