#!/usr/bin/node

const header = document.querySelector('header');
const btn = document.querySelector('#red_header');
btn.addEventListener('click', function () {
  header.classList.add('red');
});
