#!/usr/bin/node

const fs = require('fs').promises;

async function writeFile(file, content) {
  try {
    await fs.writeFile(file, content, 'utf-8');
    console.log('File written successfully.');
  } catch (error) {
    console.error('Error writing to the file:', error);
  }
}

const file = process.argv[2];
const content = process.argv[3];

if (file && content) {
  writeFile(file, content);
} else {
  console.error('Usage: node script.js <file-path> <content>');
}
