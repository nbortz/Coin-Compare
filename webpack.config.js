// webpack.config.js
const path = require('path');

module.exports = {
  entry: './src/index.jsx', // Your React entry file
  output: {
    path: path.resolve(__dirname, 'static'),
    filename: 'bundle.js'     // Output will be placed here as static/bundle.js
  },
  resolve: {
    extensions: ['.js', '.jsx'] // Allow importing without specifying extensions.
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,  // For .js and .jsx files
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: [
              '@babel/preset-env',   // Transpile modern JavaScript
              '@babel/preset-react'  // Transform JSX syntax
            ]
          }
        }
      }
    ]
  },
  mode: 'development' // Change to 'production' for production builds
};