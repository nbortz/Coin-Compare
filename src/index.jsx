import React from 'react';
import { createRoot } from 'react-dom/client';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

// Import your page components (ensure the file names match exactly)
import SearchPage from './components/SearchPage';
import CorrelationScoresPage from './components/CorrelationScoresPage';

const App = () => (
  <Router>
    <Routes>
      {/* Define the client-side routes */}
      <Route path="/" element={<SearchPage />} />
      <Route path="/result" element={<CorrelationScoresPage />} />
    </Routes>
  </Router>
);

const container = document.getElementById('root');
if (container) {
  const root = createRoot(container);
  root.render(<App />);
} else {
  console.error("No element with id 'root' found.");
}