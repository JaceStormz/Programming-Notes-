const express = require('express');
const fs = require('fs');
const cors = require('cors');
const bodyParser = require('body-parser');
const app = express();

app.use(cors());
app.use(bodyParser.json());

const USERS_FILE = './users.json';

// Register
app.post('/register', (req, res) => {
  const { username, password } = req.body;
  let users = JSON.parse(fs.readFileSync(USERS_FILE, 'utf8'));

  if (users.find(u => u.username === username)) {
    return res.status(400).json({ message: 'User already exists' });
  }

  users.push({ username, password });
  fs.writeFileSync(USERS_FILE, JSON.stringify(users, null, 2));
  res.json({ message: 'Registration successful!' });
});

// Login
app.post('/login', (req, res) => {
  const { username, password } = req.body;
  let users = JSON.parse(fs.readFileSync(USERS_FILE, 'utf8'));

  const user = users.find(u => u.username === username && u.password === password);
  if (user) res.json({ message: 'Login successful', username });
  else res.status(400).json({ message: 'Invalid credentials' });
});

app.listen(3000, () => console.log('Server running on http://localhost:3000'));