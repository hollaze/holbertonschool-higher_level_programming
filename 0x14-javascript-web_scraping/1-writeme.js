#!/usr/bin/node

const fs = require('fs');
const fileName = process.argv[2];
const string = process.argv[3];

fs.writeFile(fileName, string, 'utf-8', (err, data) => {
  if (err) throw err;
});
