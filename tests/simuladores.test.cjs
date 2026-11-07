const test = require('node:test');
const assert = require('node:assert/strict');
const vm = require('node:vm');
const fs = require('node:fs');
const path = require('node:path');

function setup() {
  class Element {
    constructor() { this.innerHTML=''; this.textContent=''; this.value=''; this.disabled=false; this.listeners={}; this.children={}; }
    querySelector(selector) { return this.children[selector] ||= new Element(); }
    addEventListener(type, fn) { this.listeners[type]=fn; }
    trigger(type, target=this) { this.listeners[type]?.({target}); }
  }
  const mounts = {indices:new Element(),busqueda:new Element(),burbuja:new Element()};
  mounts.indices.querySelector('select').value='0';
  mounts.busqueda.querySelector('#modo').value='recorrer';
  mounts.busqueda.querySelector('#buscado').value='8';
  const document={querySelector: selector=>mounts[selector.match(/"(.+)"/)[1]]};
  vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../assets/simuladores.js'),'utf8'),{document});
  return mounts;
}
function click(el, action) { el.trigger('click',{dataset:{action}}); }
test('índices consultan valores sin cambiar el arreglo',()=>{const {indices}=setup(),s=indices.querySelector('select');s.value='2';s.trigger('change');assert.match(indices.querySelector('.status').textContent,/notas\[2\] = 8/);s.value='0';s.trigger('change');assert.match(indices.querySelector('.status').textContent,/notas\[0\] = 7/);});
test('recorrido completo y búsqueda presente o ausente, con retroceso',()=>{const {busqueda:b}=setup(),mode=b.querySelector('#modo'),target=b.querySelector('#buscado');for(let i=0;i<5;i++)click(b,'next');assert.match(b.querySelector('.status').textContent,/Recorrido completo/);assert.equal(b.querySelector('[data-action=next]').disabled,true);mode.value='buscar';mode.trigger('change');for(let i=0;i<3;i++)click(b,'next');assert.match(b.querySelector('.status').textContent,/posición 2/);assert.equal(b.querySelector('[data-action=next]').disabled,true);click(b,'prev');assert.match(b.querySelector('.status').textContent,/Índice 1/);target.value='10';target.trigger('input');for(let i=0;i<5;i++)click(b,'next');assert.match(b.querySelector('.status').textContent,/no encontrado/);});
test('burbuja compara, intercambia, ordena y permite reiniciar',()=>{const {burbuja:b}=setup();let swaps=0,compares=0;while(!b.querySelector('[data-action=next]').disabled){click(b,'next');const msg=b.querySelector('.status').textContent;if(msg.includes('comparar'))compares++;if(msg.includes('se intercambian'))swaps++;}assert.equal(compares,10);assert.equal(swaps,3);assert.match(b.querySelector('.display').innerHTML,/>5<.*>6<.*>7<.*>8<.*>9</);click(b,'prev');assert.match(b.querySelector('.status').textContent,/Pasada|intercamb|intercambio/);click(b,'reset');assert.match(b.querySelector('.status').textContent,/Arreglo inicial/);});
