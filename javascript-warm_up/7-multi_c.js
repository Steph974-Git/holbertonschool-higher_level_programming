#!/usr/bin/node

const { argv } = require('node:process');
const args = argv.slice(2);
const a = parseInt(args[0]);
if (isNaN(a)) {
    console.log("Missing number of occurrences");
}
for (let a = 0; a < args; a++) {
    console.log("C is fun");
}