#!/usr/bin/node

const header = document.querySelector('header');
const btn = document.querySelector('#red_header');
btn.addEventListener('click', function () {
  header.style.color = '#FF0000';
});
