const express = require('express');
const mysql = require('mysql2');
const app = express();
const PORT = 3000;

// Create a MySQL connection pool
const pool = mysql.createPool({
  host: 'your-database-host',
  user: 'your-database-user',
  password: 'your-database-password',
  database: 'your-database-name',
  connectionLimit: 10,
});

app.use(express.static('public'));

app.get('/content/:section', (req, res) => {
  const section = req.params.section;

  // Query the database for content based on the section
  pool.query('SELECT content FROM your_table WHERE section = ?', [section], (error, results) => {
    if (error) {
      console.error('Error fetching content from the database:', error);
      res.status(500).json({ error: 'Internal Server Error' });
    } else {
      const content = results.length > 0 ? results[0].content : 'Content not found';
      res.json({ section, content });
    }
  });
});

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});

