# COPIE E COLE ESTE ENUNCIADO NO TERMINAL EM UM ARQUIVO .py. 
# Para executar no terminal use "python3 nome_arquivo.py"
# Use somente o Classroom e o GitHub. Uso do Google ou qualquer tipo de IA = zero!
# Link GitHub professor: https://github.com/profpatrickoli/1TRI-DesSistemas

# 1) (0,5 p) Crie variáveis para armazenar seu nome, nota da prova escrita, série e turma. Após isso, mostre no terminal uma mensagem personalizada se apresentando.
nome = "Débora"
nota_prova = 2.4
serie = "3º"
turma = "DSC"
print("Oiii :), meu nome é",nome, ". Estudo na", serie, "série e na turma", turma, ". Na prova de DS, eu obtive a seguinte nota:", nota_prova)
# 2) (0,5 p) Crie uma lista com 3 atividades que você gosta de fazer no final de semana.
finaldesemana = ["Dormir","Assitir","Estudar"]

# 3) (1,0 p) Crie uma condição que verifica se sua nota da prova é maior que a média 1,8.
media = 1.8

if nota_prova > 1.8:
    print("A nota esta acima da média.")
elif nota_prova < 1.8:
    print("A nota esta abaixo da média.")
else:
    print("A nota é exatamente igual a média.")

# 4) (1,0 p) Crie uma função mostra no terminal a quantidade de litros de água que devem ser consumidos diariamente por uma pessoa. Depois execute a função colocando um peso como parâmetro.
# Para calcular, siga a fórmula: qtd_litros = 0,035 * peso.
def calcularAgua(peso):
    qtd_litros = 0.035 * peso
    print("Para esse peso se deve consumir diariamente", qtd_litros, "litros de água.")

calcularAgua(59)
# 5) (1,0 p) Crie um código que verifica se "estudar" existe na lista criada da questão 2. Use o laço de repetição que preferir.
for atividade in finaldesemana:
    if "Estudar" == atividade:
        print("Essa atividade existe na lista.")

# 6) (1,0 p) Crie um laço de repetição que conta de 1 a 128, mas ao invés de somar 1 no contador, multiplique-o por 2.
contador = 1
while contador <= 128:
    print(contador)
    contador = contador * 2
