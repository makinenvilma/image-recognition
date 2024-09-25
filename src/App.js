import React, {useState} from 'react';
import './App.css';

function App() {
  const [file, setFile] = useState(null);
  const [breed, setBreed] = useState('');
  const [error, setError] = useState('');

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
    setBreed(''); // Nollataan aiemmat tiedot
    setError('');
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) {
      setError('Please select a file first');
      return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await fetch('http://localhost:5000/api/predict', {
        method: 'POST',
        body: formData,
      });

      const data = await response.json();
      if (response.ok) {
        setBreed(data.breed);
      } else {
        setError(data.error || 'Something went wrong');
      }
    } catch (err) {
      setError('Failed to connect to the server');
    }
  };

  return (
    <div className='App'>
      <h1>Dog Breed Identifier</h1>
      <form onSubmit={handleSubmit}>
        <input type='file' onChange={handleFileChange} accept='image/*' />
        <button type='submit'>Identify Breed</button>
      </form>

      {breed && <h2>Identified Breed: {breed}</h2>}
      {error && <p style={{color: 'red'}}>{error}</p>}
    </div>
  );
}

export default App;
