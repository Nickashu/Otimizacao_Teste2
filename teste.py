import csv

NAME = "JULIA"  #5 primeiras letras do nome a ser analisado
produtoX = [1000, 0.1, 1000, 0.1, 1]   #Vetor que conterá as quantidades de nutrientes para o produto X (depende das letras do nome)

idPrudutos = [1, 15, 19, 30, 46, 52, 53, 68]  #ID dos produtos que serão usados na tabela 2

At = []   #Esta matriz será a matriz A transposta
b = [100, 0.01, 100, 0.1, 1]   #Este vetor terá os valores das restrições (depende das letras do nome)
c = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]   #Vetor para os coeficientes das variáveis de decisão na função objetivo (os coeficientes 0 representam as variáveis de folga)

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
for i in range(5):
    vetorFolga = [0, 0, 0, 0, 0]
    vetorFolga[i] = -1
    At.append(vetorFolga)

A = [list(linha) for linha in zip(*At)]   #Transpondo a matriz At para obter a matriz A
        
print(f"Vetor de restrições b: {b}\nVetor de coeficientes c: {c}\nMatriz A:")
for linha in A:
    print(" ".join(f"{elem:<10}" for elem in linha))  # Alinhamento à direita com 5 espaços por coluna