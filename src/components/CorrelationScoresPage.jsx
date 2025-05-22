import React from 'react';
import { Helmet } from 'react-helmet';
import { useLocation, useNavigate } from 'react-router-dom';

const CorrelationScoresPage = () => {
  const navigate = useNavigate();
  const { state } = useLocation();
  // outputArray comes from navigation state; default to empty array if undefined
  const outputArray = (state && state.outputArray) || [];

  // Define your coin names (these replace the Jinja-set coin_names)
  const coinNames = [
    "Bonk",
    "Wif",
    "Fartcoin",
    "Fwog",
    "Giga",
    "Goatseus Maximus",
    "Chill Guy",
    "User Token"
  ];

  // Style objects corresponding to your original CSS
  const pageStyles = {
    backgroundColor: 'black',
    fontFamily: 'Arial, sans-serif',
    textAlign: 'center',
    background: 'linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url("/static/coinpairlogo.jpg") no-repeat center center fixed',
    backgroundSize: 'cover',
    color: 'white',
    minHeight: '100vh',
    margin: 0,
    paddingTop: '3em',
  };

  const resultsContainer = {
    backgroundColor: 'rgba(64, 64, 64, 0.7)',
    width: '80%',
    margin: '20px auto',
    padding: '20px',
    borderRadius: '15px',
  };

  const resultsHeader = {
    backgroundColor: 'rgba(64, 64, 64, 0.7)',
    color: 'white',
    borderRadius: '10px',
    width: '100%',
    marginBottom: '20px',
    height: '3em',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    fontWeight: 'bold',
    fontSize: '1.5em',
  };

  const containerStyle = {
    display: 'flex',
    flexWrap: 'wrap',
    justifyContent: 'center',
    gap: '20px',
    marginTop: '20px',
  };

  const resultBox = {
    backgroundColor: 'black',
    color: 'lime',
    padding: '20px',
    borderRadius: '15px',
    width: '312px',
    fontSize: '16px',
    fontWeight: 'bold',
    textAlign: 'left',
  };

  const tickerBox = {
    backgroundColor: '#f8f8f8',
    color: 'black',
    padding: '5px 10px',
    borderRadius: '10px',
    display: 'inline-block',
    marginBottom: '10px',
  };

  const info = {
    marginTop: '10px',
  };

  const debugText = {
    marginTop: '20px',
    textAlign: 'left',
  };

  const backButton = {
    display: 'inline-block',
    marginTop: '30px',
    padding: '10px 20px',
    backgroundColor: 'rgba(64, 64, 64, 0.7)',
    color: 'white',
    fontWeight: 'bold',
    borderRadius: '10px',
    textDecoration: 'none',
    cursor: 'pointer',
  };

  return (
    <>
      <Helmet>
        <meta charSet="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Correlation Scores</title>
      </Helmet>
      <div style={pageStyles}>
        <div style={resultsHeader}>Results</div>
        <div style={resultsContainer}>
          <div style={containerStyle}>
            {outputArray.map((coinData, idx) => (
              <div style={resultBox} key={idx}>
                {coinData.length === 5 ? (
                  <>
                    <div style={tickerBox}>
                      {coinNames[idx]}
                    </div>
                    <div style={info}>
                      Correlation: {coinData[4].toFixed(2)}<br /><br />
                      MCAP Diff: {coinData[0].toFixed(2)}%<br />
                      VOL Diff: {coinData[1].toFixed(2)}%<br /><br />
                      MCAP: {coinData[2].toFixed(2)}<br />
                      VOL: {coinData[3].toFixed(2)}
                    </div>
                  </>
                ) : (
                  <>
                    <div style={tickerBox}>
                      {coinData[3]}
                    </div>
                    <div style={info}>
                      MCAP: {coinData[0].toFixed(2)}<br />
                      VOL: {coinData[1].toFixed(2)}<br />
                      User Impressions: {coinData[2] != null ? coinData[2].toFixed(2) : 'N/A'}
                    </div>
                  </>
                )}
              </div>
            ))}
          </div>
          <div style={debugText}>
            <p>
              Our correlation scores are calculated using the volume, marketcap, and impressions differentials between your submitted token and our benchmark tokens, when they were the same age. A negative percent differential means that the benchmark token had that much more volume, marketcap, or impressions at the same age as the submitted token. A positive percent differential means the submitted token has that much more in volume, marketcap, or impressions than the benchmark did at the same age.
            </p>
          </div>
          <button style={backButton} onClick={() => navigate('/')}>
            Go Back
          </button>
        </div>
      </div>
    </>
  );
};

export default CorrelationScoresPage;