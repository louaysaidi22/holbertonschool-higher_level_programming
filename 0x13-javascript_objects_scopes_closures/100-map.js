#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
const list1 = list.map((x, i) => (x * i));
console.log(list1);
