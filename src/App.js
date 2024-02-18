import React, { useState, useEffect} from 'react';
import './App.css';

function App() {
  useEffect(() => {
    document.title = 'Convert .hol to .ics';
  }, []);

  const [file, setFile] = useState(null);
  const [filename, setFilename] = useState(null);
  const [uploadComplete, setUploadComplete] = useState(false);

  const onFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const onFormSubmit = (event) => {
    event.preventDefault();

    // check if file is selected
    if (!file) {
      alert('Please select a file');
      return;
    }
    // check if file is .hol
    if (!file.name.endsWith('.hol')) {
      alert('Please select a .hol file');
      return;
    }
    // check if file is less than 1MB
    if (file.size > 1000000) {
      alert('File size must be less than 1MB');
      return;
    }

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
      <div className="description-card">
        <h2>Welcome</h2>
        <p>Convert .hol file to ics file</p>
      </div>
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
