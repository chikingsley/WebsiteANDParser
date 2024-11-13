const express = require('express');
const spdy = require('spdy');
const fs = require('fs');
const path = require('path');
const compression = require('compression');

const app = express();

// Enable gzip compression
app.use(compression());

// Serve static files
app.use(express.static('dist'));

// Handle all routes for SPA
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'dist', 'index.html'));
});

// SSL certificates for HTTP/2
const options = {
  key: fs.readFileSync(path.join(__dirname, 'ssl', 'server.key')),
  cert: fs.readFileSync(path.join(__dirname, 'ssl', 'server.crt'))
};

// Create HTTP/2 server
spdy.createServer(options, app)
  .listen(3000, (error) => {
    if (error) {
      console.error(error);
      return process.exit(1);
    }
    console.log('Server running on port 3000 with HTTP/2 enabled');
  });
