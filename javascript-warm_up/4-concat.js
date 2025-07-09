#!/usr/bin/node

const { argv } = require('node:process');
const args = argv.slice(2);
const a = (process.argv[2]);
const b = (process.argv[3]);
console.log(a + " is " + b);
