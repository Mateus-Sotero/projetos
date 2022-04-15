function calcular(){
  let oposto = document.getElementById('oposto')
  let adjacente = document.querySelector('#adjacente')
  let opo = Number(oposto.value)
  let adj = Number(adjacente.value)

  let valor = opo**2 + adj**2

  return document.querySelector('.resultado').innerHTML = Math.sqrt(valor)
}
