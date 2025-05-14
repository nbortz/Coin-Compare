import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Helmet } from 'react-helmet';

const AboutPage = () => {
  // Inline styles for the page wrapper
  const pageStyles = {
    backgroundColor: '#121212',
    color: '#E0E0E0',
    paddingTop: '50px',
    minHeight: '100vh',
  };

  return (
    <>
      <Helmet>
        <meta charSet="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>About - Crypto Price Plotter</title>
        <style>{`
          .btn-link {
            color: #FFB300;
          }
          .btn-link:hover {
            color: #FFCA28;
          }
        `}</style>
      </Helmet>

      <div style={pageStyles}>
        <div className="container" style={{ maxWidth: '600px' }}>
          {/* Add your page content here */}
        </div>
      </div>
    </>
  );
};

export default AboutPage;
