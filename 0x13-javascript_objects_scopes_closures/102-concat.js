#!/usr/bin/node

const fs = require('fs');
const [sourceFile1, sourceFile2, destinationFile] = process.argv.slice(2);

fs.readFile(sourceFile1, 'utf8', (err1, data1) => {
  if (err1) throw err1;

  fs.readFile(sourceFile2, 'utf8', (err2, data2) => {
    if (err2) throw err2;

    fs.writeFile(destinationFile, data1 + data2, (err3) => {
      if (err3) throw err3;
    });
  });
});
