import React, { useState } from 'react';
import axios from 'axios';

const PredictionForm = () => {
  const [age, setAge] = useState('');
  const [experience, setExperience] = useState('');
  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  // Handle input changes
  const handleAgeChange = (e) => setAge(e.target.value);
  const handleExperienceChange = (e) => setExperience(e.target.value);

  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();

    setLoading(true);
    setError('');
    
    try {
      // Send a POST request to the backend (adjust the URL as needed)
      const response = await axios.get(`http://localhost:5001/prediction?age=${age}&exp=${experience}`);
      
      setPrediction(response.data);
    } catch (err) {
      setError('Failed to get prediction. Please try again later.');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="prediction-form">
      <h1>Salary Prediction</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Age:</label>
          <input
            type="number"
            value={age}
            onChange={handleAgeChange}
            required
            min="18"
          />
        </div>
        <div>
          <label>Experience (in years):</label>
          <input
            type="number"
            value={experience}
            onChange={handleExperienceChange}
            required
            min="0"
          />
        </div>
        <button type="submit" disabled={loading}>Submit</button>
      </form>

      {loading && <p>Loading...</p>}

      {error && <p style={{ color: 'red' }}>{error}</p>}

      {prediction !== null && (
        <div>
          <h3>Prediction:</h3>
          <p>{prediction}</p>
        </div>
      )}
    </div>
  );
};

export default PredictionForm;
