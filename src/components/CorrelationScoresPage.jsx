import React from 'react';
import { Helmet } from 'react-helmet';
import { useLocation, useNavigate } from 'react-router-dom';

const CorrelationScoresPage = () => {
  const navigate = useNavigate();
  const { state } = useLocation();
  // Sets a default empty array if state is undefined
  const outputArray = (state && state.outputArray) || [];

  // ... (rest of your component rendering the scores)

  return (
    <>
      <Helmet>
        <meta charSet="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Correlation Scores</title>
      </Helmet>
      {/* Render your results page UI */}
      <div>
        {/* Example: */}
        <h1>Results</h1>
        {outputArray.map((coinData, idx) => (
          <div key={idx}>
            {/* Render coinData */}
          </div>
        ))}
        <button onClick={() => navigate('/')}>Go Back</button>
      </div>
    </>
  );
};

export default CorrelationScoresPage;