#!/usr/bin/node

const ul = document.querySelector('.my_list');
const btn = document.querySelector('#add_item');
btn.addEventListener('click', function () {
  const li = document.createElement('li');
  ul.appendChild(li);
  li.textContent = 'Item';
});
