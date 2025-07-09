#!/usr/bin/node

const args = process.argv.slice(2);
const a = parseInt(args[0]);
const b = parseInt(args[1]);
const result = add(a, b)
function add(a, b) {
    return a + b;
}


if (isNaN(a) || isNaN(b)) {
    console.log("NaN");
} else {
    console.log(result);
}
