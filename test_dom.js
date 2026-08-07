const fs = require('fs');
const html = fs.readFileSync('public/python_basic_reference.html', 'utf8');
const scriptMatch = html.match(/<script>([\s\S]*?)<\/script>/);

let code = scriptMatch[1];

const dom = `
const document = {
  getElementById: (id) => {
    return {
      style: {},
      classList: { toggle: ()=>{}, add: ()=>{}, remove: ()=>{} },
      innerHTML: '',
      addEventListener: ()=>{},
      appendChild: ()=>{},
      querySelectorAll: () => [],
      querySelector: () => ({ addEventListener: ()=>{}, appendChild: ()=>{} }),
      textContent: ''
    }
  },
  createElement: () => {
    return {
      style: {},
      className: '',
      classList: { toggle: ()=>{}, add: ()=>{}, remove: ()=>{} },
      innerHTML: '',
      addEventListener: ()=>{},
      appendChild: ()=>{},
      querySelectorAll: () => [],
      querySelector: () => ({ addEventListener: ()=>{}, appendChild: ()=>{} }),
      textContent: ''
    }
  }
};
const window = { scrollTo: ()=>{} };
`;

fs.writeFileSync('temp_test2.js', dom + code);
