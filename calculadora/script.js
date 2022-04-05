var visor = document.querySelector('.visor')

function num(numero){
  let num = document.querySelector('.visor').innerHTML
  visor.innerHTML = String(num) + String(numero)
  
}

function clean(){
  visor.innerHTML = ''
}

function back(){
  let resultado = visor.innerHTML
  visor.innerHTML = resultado.substring(0, resultado.length -1)
}

function calcular(){
  let res = document.querySelector('.visor').innerHTML
  if(res){
    document.querySelector('.visor').innerHTML = eval(res);
  }else{
    visor.innerHTML = 'Nada para calcular!'
  }
}