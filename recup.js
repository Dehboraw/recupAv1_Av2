/*  COPIE E COLE ESTE ENUNCIADO NO VSCODE! (arquivo .js)
Prova prática de recuperação do nivelamento (AV1) + prova (AV2).
Pode consultar o seu GitHub ou o do professor: https://github.com/profpatrickoli
Cópia de outros colegas ou uso de outros sites na internet (Google, IA, etc) = zero na recuperação! */

/* 1) (0,5 p) Crie variáveis para armazenar seu nome, altura, série e turma. Após isso, mostre no terminal uma mensagem personalizada se apresentando. */

/* 2) (0,5 p) Crie uma lista com 3 esportes que você gosta */

/* 3) (1,0 p) Crie uma condição que verifica se você é maior que o professor Patrick, que possui 1.73 de altura */

/* 4) (1,0 p) Crie uma função que mostre os 3 esportes no terminal. Use o laço de repetição que preferir. */

/* 5) (1,0 p) Crie um código que verifica se o esporte "natação" existe na lista criada da questão 2. */

/* 6) (1,0 p) Crie um laço de repetição que conta de 0 até -10 */

/*1*/ 
const nome = "Débora"
const altura = 1.60
const serie = "3º"
const turma = "DSC"
console.log("Oii, me chamo "+ nome +", e tenho " + altura + "m de altura."+" Nesse ano eu estou na "+ serie +" série do Ensino Médio e estudo na turma " + turma + ".")
/*2*/
esportes =["Futebol", "Basquete", "Badminton"]
/*3*/
const altPatrick = 1.73
if (altura > altPatrick){
    console.log("Você é maior")
} else if (altura < altPatrick){
    console.log("Você é menor")
} else {
    console.log("Você tem a mesma alutra")
}
/*4*/
function mostrarEsportes(listaPreferida){
    console.log("# Os meus esportes preferidos #")
    for (let i = 0; i < listaPreferida.length ; i++){
        console.log(listaPreferida[i])
    }
} 
mostrarEsportes(esportes)
/*5*/
esportes.forEach((esporte) => {
    if (esporte == "Natação"){
        console.log("Existe esse esporte na lista")
    }
})
/*6*/
let contador = 0
while (contador >= -10){
    console.log(contador)
    contador = contador - 1
}