#!/usr/bin/node

const args = process.argv.slice(2);
const a = parseInt(args[0]);
if (isNaN(a)) {
    console.log('Not a number');
} else {
    console.log('My number: ' + a)
}
