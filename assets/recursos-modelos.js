(function (root, factory) {
  const api = factory();
  if (typeof module === 'object' && module.exports) module.exports = api;
  else root.PMModelos = api;
})(typeof globalThis !== 'undefined' ? globalThis : this, function () {
  'use strict';
  const guided = {
    ocho: ['llenarB','BA','llenarB','BA','vaciarA','BA','llenarB','BA'],
    seis: ['llenarA','AB','vaciarB','AB','llenarA','AB']
  };
  function bidones(state, action) {
    let {a,b}=state; const before={a,b};
    if (!Number.isInteger(a)||!Number.isInteger(b)||a<0||a>5||b<0||b>3) throw Error('Estado inválido');
    switch(action) {
      case 'llenarA': a=5; break; case 'llenarB': b=3; break;
      case 'vaciarA': a=0; break; case 'vaciarB': b=0; break;
      case 'AB': {const amount=Math.min(a,3-b);a-=amount;b+=amount;break;}
      case 'BA': {const amount=Math.min(b,5-a);b-=amount;a+=amount;break;}
      default: throw Error('Operación desconocida');
    }
    return {a,b,changed:a!==before.a||b!==before.b};
  }
  const cpuSteps = [
    {instruction:'Antes de ejecutar',memory:'Todavía no hay datos en el modelo.',output:'Sin salida',explanation:'El programa contiene instrucciones; Java necesita compilación y un entorno de ejecución.'},
    {instruction:'Guardar precio = 150',memory:'precio = 150',output:'Sin salida',explanation:'El programa en ejecución conserva este dato temporalmente.'},
    {instruction:'Guardar cantidad = 3',memory:'precio = 150; cantidad = 3',output:'Sin salida',explanation:'Se incorpora otro dato para el cálculo.'},
    {instruction:'Calcular total = precio × cantidad',memory:'precio = 150; cantidad = 3; total = 450',output:'Sin salida',explanation:'El procesamiento utiliza los datos disponibles y conserva el resultado.'},
    {instruction:'Mostrar total',memory:'precio = 150; cantidad = 3; total = 450',output:'450',explanation:'Se comunica el resultado; el dato continúa disponible en este modelo.'}
  ];
  const javaParts = {
    clase:'La clase Main contiene el programa; su nombre coincide con Main.java.',
    main:'main es el punto de entrada: la ejecución comienza en su cuerpo.',
    llaves:'Las llaves delimitan los bloques de la clase y del método.',
    instrucciones:'println es una instrucción: muestra texto en la salida.',
    orden:'La ejecución entra en main y sigue sus instrucciones en orden.'
  };
  const programs={
    precio:[
      ['int precio = 150;', {precio:150}, 'Se declara precio con 150.'],
      ['int cantidad = 3;', {precio:150,cantidad:3}, 'Se declara cantidad con 3.'],
      ['int total = precio * cantidad;', {precio:150,cantidad:3,total:450}, 'Se calcula 150 × 3 y se guarda 450.'],
      ['precio = 200;', {precio:200,cantidad:3,total:450}, 'Solo cambia precio; total conserva 450.'],
      ['total = precio * cantidad;', {precio:200,cantidad:3,total:600}, 'Se vuelve a calcular: 200 × 3 = 600.']
    ],
    copia:[['int a = 5;', {a:5}, 'Se declara a con 5.'],['int b = a;', {a:5,b:5}, 'b recibe una copia del valor actual de a.'],['b = 10;', {a:5,b:10}, 'Solo cambia b; a conserva 5.']]
  };
  function variables(program, step) {
    const sequence=programs[program]; if(!sequence||!Number.isInteger(step)||step<0||step>sequence.length) throw Error('Paso inválido');
    return step===0 ? {values:{},instruction:'Sin instrucciones ejecutadas',explanation:'Todas las variables están sin declarar.'} : {values:{...sequence[step-1][1]},instruction:sequence[step-1][0],explanation:sequence[step-1][2]};
  }
  function ifElse(saldo,precio){const value=saldo>=precio;return {value,branch:value?'Compra autorizada':'Saldo insuficiente',explanation:value?`${saldo} >= ${precio} es verdadero; se ejecuta if y se omite else.`:`${saldo} >= ${precio} es falso; se omite if y se ejecuta else.`};}
  function grades(n,wrong=false){if(!Number.isInteger(n)||n<1||n>10)throw Error('La nota debe ser un entero entre 1 y 10.');const rules=wrong?[[6,'Aprobado'],[9,'Excelente']]:[[9,'Excelente'],[6,'Aprobado']];let selected=null;const checks=rules.map(([limit,label])=>{if(selected)return {limit,result:null,label};const result=n>=limit;if(result)selected=label;return {limit,result,label};});return {checks,branch:selected||'Debe mejorar'};}
  function logic(mode, input){
    const p=input.puntos>=10, v=input.vidas>0, permiso=!!input.permiso, edad=input.edad>=18, tiene=!!input.tiene, admin=!!input.admin, bloqueado=!!input.bloqueado;
    if(mode==='and')return {expression:'puntos >= 10 && vidas > 0',values:[p,p?v:null],result:p&&v};
    if(mode==='or')return {expression:'puntos >= 10 || permisoEspecial',values:[p,p?null:permiso],result:p||permiso};
    if(mode==='not')return {expression:'!bloqueado',values:[bloqueado],result:!bloqueado};
    if(mode==='grupo1'){const middle=edad?tiene:null, left=edad&&tiene;return {expression:'(edad >= 18 && tienePermiso) || esAdministrador',values:[edad,middle,left?null:admin],result:left||admin};}
    if(mode==='grupo2'){const inner=tiene?null:admin;return {expression:'edad >= 18 && (tienePermiso || esAdministrador)',values:[edad,edad?tiene:null,edad?inner:null],result:edad&&(tiene||admin)};}
    throw Error('Escenario desconocido');
  }
  function switchMenu(value,mode){if(!Number.isInteger(value))throw Error('Ingresa una opción entera.');const cases=['Consultar saldo','Realizar depósito','Salir','Opción inválida'];const index=value>=1&&value<=3?value-1:3;const output=mode==='sin-break'?cases.slice(index):[cases[index]];return {selected:index===3?'default':`case ${value}`,output,explanation:mode==='sin-break'?'Sin break, la ejecución continúa en los casos siguientes.':mode==='flechas'?'La alternativa con flecha ejecuta solo su bloque.':'break termina el switch tras el caso seleccionado.'};}
  return {guided,bidones,cpuSteps,javaParts,programs,variables,ifElse,grades,logic,switchMenu};
});
