#!/usr/bin/node

const { argv } = require('node:process');
const args = argv.slice(2);
const a = parseInt(args[0]);
if (isNaN(a)) {
    console.log("Not a number");
} else {
    console.log("My number: " + a)
}
