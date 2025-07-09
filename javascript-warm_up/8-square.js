const { argv } = require('node:process');
const args = argv.slice(2);
const a = parseInt(args[0]);
if (isNaN(a)) {
    console.log("Missing size");
} else {
for (let i = 0; i < a; i++) 
    console.log("X".repeat(a));
}
