import React, { useState } from 'react';
import { Helmet } from 'react-helmet';
import { useNavigate } from 'react-router-dom';

const CoinPairPage = () => {
  const navigate = useNavigate();
  const [userValue, setUserValue] = useState('');

  // Inline styles (unchanged)
  const pageStyles = {
    minHeight: '100vh',
    margin: 0,
    padding: 0,
    fontFamily: "'Open Sans', sans-serif",
    background: `linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)),
      url('/static/coinpairlogo.jpg') no-repeat center center fixed`,
    backgroundSize: 'cover',
    color: '#fff',
  };

  const menuLinkStyles = {
    backgroundColor: 'rgba(0, 204, 0, 0.9)',
    padding: '8px 12px',
    borderRadius: '8px',
    color: '#fff',
    textDecoration: 'none',
    fontSize: '16px',
    marginRight: '20px',
  };

  const formContainerStyles = {
    backgroundColor: 'rgba(0, 204, 0, 0.9)',
    width: '1200px',
    padding: '20px',
    borderRadius: '15px',
    boxSizing: 'border-box',
    color: '#000',
  };

  const contentContainerStyles = {
    maxWidth: '1200px',
    margin: '40px auto',
    padding: '20px',
    backgroundColor: 'rgba(0, 0, 0, 0.7)',
    borderRadius: '10px',
  };

  // Handle form submission via JS
  const handleSubmit = async (e) => {
    e.preventDefault(); // Prevent the default POST behavior

    // Optionally, call your API endpoint to get the output data:
    const response = await fetch('/api/get_token_data', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ mintAdd: userValue }), // send the contract address
    });
    const resultData = await response.json();
    console.log('Result:', resultData.data);

    // Navigate to the result page with state passing the output data
    navigate('/result', { state: { outputArray: resultData.data } });
  };

  return (
    <>
      <Helmet>
        <meta charSet="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>CoinPair</title>
        <link
          href="https://fonts.googleapis.com/css2?family=Open+Sans&display=swap"
          rel="stylesheet"
        />
        <style>{`
          .btn-link {
            color: #00FF00;
            text-decoration: none;
            font-weight: bold;
          }
          .btn-link:hover {
            text-decoration: underline;
          }
        `}</style>
      </Helmet>

      <div style={pageStyles}>
        {/* Top-left menu */}
        <div style={{ position: 'absolute', top: '20px', left: '20px' }}>
          <a href="/" style={menuLinkStyles}>Home</a>
          <a href="https://coinpair.gitbook.io/coinpair-docs/" style={menuLinkStyles}>Docs</a>
        </div>

        {/* Main form area */}
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', height: '100vh' }}>
          <div style={formContainerStyles}>
            <div style={{ width: '600px', margin: '0 auto' }}>
              {/* Remove action and method so the browser doesn't try to load a new page */}
              <form onSubmit={handleSubmit}>
                <label htmlFor="user_value" style={{ display: 'block', marginBottom: '10px', fontWeight: 'bold' }}>
                  Enter a Solana contract address:
                </label>
                <input
                  type="text"
                  id="user_value"
                  name="user_value"
                  value={userValue}
                  onChange={(e) => setUserValue(e.target.value)}
                  style={{ width: '100%', padding: '10px', fontSize: '16px', marginBottom: '20px', boxSizing: 'border-box' }}
                />
                <button
                  type="submit"
                  style={{
                    backgroundColor: '#000',
                    color: '#fff',
                    border: 'none',
                    borderRadius: '8px',
                    padding: '10px 20px',
                    fontSize: '16px',
                    cursor: 'pointer',
                    display: 'block',
                    margin: '0 auto',
                  }}
                >
                  Submit
                </button>
              </form>
            </div>
          </div>
        </div>

        {/* Bottom content */}
        <div style={contentContainerStyles}>
          <h1 style={{ textAlign: 'center', marginTop: 0 }}>About CoinPair</h1>
          <p>
            Coin Pair is a tool that allows you to compare coins based on factors that may have similarities to historically high performing coins. We built an algorithm based on information we found useful when examining coins. This informational site is funded primarily by developer funds and our crypto currency "Coin Pair" which is available for purchase at (put link here).
          </p>
        </div>
        <div style={contentContainerStyles}>
          <h1 style={{ textAlign: 'center', marginTop: 0 }}>Important Disclaimer</h1>
          <p>
            The information provided in this crypto analysis project is for informational purposes only and does not constitute financial advice. All content, including analysis, opinions, and data, is based on sources believed to be reasonably accurate and reliable at the time of accessing. However, we do not guarantee the completeness, accuracy, or timeliness of the information provided.
          </p>
          <p>
            Investing in cryptocurrencies involves significant risk, and you should conduct your own research and seek advice from a qualified financial advisor before making any investment decisions. We are not responsible for any losses or damages resulting from the use of this information.
          </p>
          <p>
            Nothing that appears on this site should be considered an endorsement, recommendation, promise, or guarantee.
          </p>
          <p>
            By using this project, you acknowledge and agree that you are solely responsible for your own investment decisions.
          </p>
        </div>
      </div>
    </>
  );
};

export default CoinPairPage;