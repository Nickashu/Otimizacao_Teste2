import csv
import numpy as np
import scipy.optimize as sco

NAME = input("Digite um nome: ")
if len(NAME) >= 5:
    NAME = NAME[:5].upper()   #5 primeiras letras do nome a ser analisado
else:
    NAME = "NICOL"

idPrudutos = [1, 15, 19, 30, 46, 52, 53, 68]  #ID dos produtos que serão usados na tabela 2

produtoX = np.array([1000, 0.1, 1000, 0.1, 1])   #Vetor que conterá as quantidades de nutrientes para o produto X (depende das letras do nome)

At = []   #Esta matriz será a matriz A transposta
b = np.array([100, 0.01, 100, 0.1, 1])   #Este vetor terá os valores das restrições (depende das letras do nome)
#c = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0])   #Vetor para os coeficientes das variáveis de decisão na função objetivo (os coeficientes 0 representam as variáveis de folga)
c = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1])

#Adicionando as linhas correspondentes aos produtos na matriz:
with open("nutricao.csv", newline='', encoding='utf-8') as nutricao:
    readerNutricao = csv.DictReader(nutricao)
    for i, row in enumerate(readerNutricao):
        if int(row['Numero']) in idPrudutos:
            At.append([float(row['Caloria']) * 1000, float(row['Calcio']) * 1, float(row['VitaminaA']) * 1000, float(row['Riboflavina']) * 1, float(row['AcidoAscorbico']) * 1])   #Adicionando uma linha na matriz A

#Adicionando a linha correspondente aos valores do produto X na matriz:
letraAtual = 0
while letraAtual < len(NAME):
    with open("letras.csv", newline='', encoding='utf-8') as letras:
        readerLetras = csv.DictReader(letras)
        for row in readerLetras:
            if row['Letra'] == NAME[letraAtual]:
                b[letraAtual] = b[letraAtual] * float(row['Dieta'])
                produtoX[letraAtual] = produtoX[letraAtual] * float(row['ProdutoX'])
                letraAtual += 1
                break
At.append(produtoX)

#Adicionando as variáveis de folga na matriz:
"""
for i in range(5):
    vetorFolga = [0, 0, 0, 0, 0]
    vetorFolga[i] = -1
    At.append(vetorFolga)
"""

At = np.array(At)  #Matriz transposta como numpy array
A = At.T           #Transposição para obter matriz A

#Restrições de não negatividade:
x_bounds = (0, None)

#O módulo linprog resolve para Ax<=b, mas atualmente temos Ax>=b. Para fazer a transformação, basta multiplicar as restrições por -1
result = sco.linprog(c, A_ub=-A, b_ub=-b, bounds=x_bounds, method='simplex')
#result = sco.linprog(c, A_eq=A, b_eq=b, bounds=x_bounds, method='simplex')   #Usando variáveis de folga, temos Ax=b

print(f"Usando o nome {NAME}\nVetor de restrições b: {b}\nVetor de coeficientes c: {c}\nMatriz A:")
for linha in A:
    print(" ".join(f"{elem:<10}" for elem in linha))  # Alinhamento à direita com 5 espaços por coluna
#print(f"Resultado: {result}")
print(f"Valor mínimo a ser gasto: {result.fun}\n\nDólares gastos na farinha de trigo (enriquecida): {result.x[0]}\n\
Dólares gastos no leite evaporado: {result.x[1]}\nDólares gastos no queijo cheddar: {result.x[2]}\n\
Dólares gastos no fígado bovino: {result.x[3]}\nDólares gastos no repolho: {result.x[4]}\n\
Dólares gastos no espinafre: {result.x[5]}\nDólares gastos na batata doce: {result.x[6]}\n\
Dólares gastos no feijão verde (seco): {result.x[7]}\nDólares gastos no Produto X: {result.x[8]}")