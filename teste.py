import warnings
import numpy as np
import scipy.optimize as sco
from scipy.optimize import OptimizeWarning

warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=OptimizeWarning)

letras = [
    {'Letra': 'A', 'Dieta': 7, 'ProdutoX': 63},
    {'Letra': 'B', 'Dieta': 60, 'ProdutoX': 52},
    {'Letra': 'C', 'Dieta': 83, 'ProdutoX': 59},
    {'Letra': 'D', 'Dieta': 10, 'ProdutoX': 85},
    {'Letra': 'E', 'Dieta': 39, 'ProdutoX': 82},
    {'Letra': 'F', 'Dieta': 59, 'ProdutoX': 58},
    {'Letra': 'G', 'Dieta': 38, 'ProdutoX': 50},
    {'Letra': 'H', 'Dieta': 30, 'ProdutoX': 69},
    {'Letra': 'I', 'Dieta': 65, 'ProdutoX': 44},
    {'Letra': 'J', 'Dieta': 27, 'ProdutoX': 26},
    {'Letra': 'K', 'Dieta': 91, 'ProdutoX': 30},
    {'Letra': 'L', 'Dieta': 68, 'ProdutoX': 43},
    {'Letra': 'M', 'Dieta': 49, 'ProdutoX': 90},
    {'Letra': 'N', 'Dieta': 6, 'ProdutoX': 91},
    {'Letra': 'O', 'Dieta': 10, 'ProdutoX': 45},
    {'Letra': 'P', 'Dieta': 32, 'ProdutoX': 82},
    {'Letra': 'Q', 'Dieta': 51, 'ProdutoX': 98},
    {'Letra': 'R', 'Dieta': 47, 'ProdutoX': 67},
    {'Letra': 'S', 'Dieta': 20, 'ProdutoX': 97},
    {'Letra': 'T', 'Dieta': 66, 'ProdutoX': 28},
    {'Letra': 'U', 'Dieta': 78, 'ProdutoX': 54},
    {'Letra': 'V', 'Dieta': 81, 'ProdutoX': 33},
    {'Letra': 'W', 'Dieta': 81, 'ProdutoX': 59},
    {'Letra': 'X', 'Dieta': 61, 'ProdutoX': 61},
    {'Letra': 'Y', 'Dieta': 0, 'ProdutoX': 39},
    {'Letra': 'Z', 'Dieta': 86, 'ProdutoX': 83}
]
nutricao = [
    {'Numero': '1', 'Mercadoria': 'Farinhadetrigo(enriquecida)', 'Caloria': '44.7', 'Proteina': '1411', 'Calcio': '2.0', 'Ferro': '365', 'Vitamina A': '0', 'Tiamina': '55.4', 'Riboflavina': '33.3', 'Niacina': '441', 'Acido Ascorbico': '0'},
    {'Numero': '5', 'Mercadoria': 'Farinha de milho', 'Caloria': '36.0', 'Proteina': '897', 'Calcio': '1.7', 'Ferro': '99', 'Vitamina A': '30.9', 'Tiamina': '17.4', 'Riboflavina': '7.9', 'Niacina': '106', 'Acido Ascorbico': '0'},
    {'Numero': '15', 'Mercadoria': 'Leite evaporado (lata)', 'Caloria': '8.4', 'Proteina': '422', 'Calcio': '15.1', 'Ferro': '9', 'Vitamina A': '26.0', 'Tiamina': '3.0', 'Riboflavina': '23.5', 'Niacina': '11', 'Acido Ascorbico': '60'},
    {'Numero': '17', 'Mercadoria': 'Margarina', 'Caloria': '20.6', 'Proteina': '17', 'Calcio': '0.6', 'Ferro': '6', 'Vitamina A': '55.8', 'Tiamina': '0.2', 'Riboflavina': '0', 'Niacina': '0', 'Acido Ascorbico': '0'},
    {'Numero': '19', 'Mercadoria': 'Queijo (cheddar)', 'Caloria': '7.4', 'Proteina': '448', 'Calcio': '16.4', 'Ferro': '19', 'Vitamina A': '28.1', 'Tiamina': '0.8', 'Riboflavina': '10.3', 'Niacina': '4', 'Acido Ascorbico': '0'},
    {'Numero': '21', 'Mercadoria': 'Pasta de amendoim', 'Caloria': '15.7', 'Proteina': '661', 'Calcio': '1.0', 'Ferro': '48', 'Vitamina A': '0', 'Tiamina': '9.6', 'Riboflavina': '8.1', 'Niacina': '471', 'Acido Ascorbico': '0'},
    {'Numero': '24', 'Mercadoria': 'Bacon', 'Caloria': '41.7', 'Proteina': '0', 'Calcio': '0', 'Ferro': '0', 'Vitamina A': '0.2', 'Tiamina': '0', 'Riboflavina': '5', 'Niacina': '5', 'Acido Ascorbico': '0'},
    {'Numero': '30', 'Mercadoria': 'Fígado (boi)', 'Caloria': '2.2', 'Proteina': '333', 'Calcio': '0.2', 'Ferro': '139', 'Vitamina A': '169.2', 'Tiamina': '6.4', 'Riboflavina': '50.8', 'Niacina': '316', 'Acido Ascorbico': '525'},
    {'Numero': '34', 'Mercadoria': 'Lombo de porco assado', 'Caloria': '4.4', 'Proteina': '249', 'Calcio': '0.3', 'Ferro': '37', 'Vitamina A': '0', 'Tiamina': '18.2', 'Riboflavina': '3.6', 'Niacina': '79', 'Acido Ascorbico': '0'},
    {'Numero': '40', 'Mercadoria': 'Salmão. rosa (lata)', 'Caloria': '5.8', 'Proteina': '705', 'Calcio': '6.8', 'Ferro': '45', 'Vitamina A': '3.5', 'Tiamina': '1.0', 'Riboflavina': '4.9', 'Niacina': '209', 'Acido Ascorbico': '0'},
    {'Numero': '45', 'Mercadoria': 'Feijão verde', 'Caloria': '2.4', 'Proteina': '138', 'Calcio': '3.7', 'Ferro': '80', 'Vitamina A': '69.0', 'Tiamina': '4.3', 'Riboflavina': '5.8', 'Niacina': '37', 'Acido Ascorbico': '862'},
    {'Numero': '46', 'Mercadoria': 'Repolho', 'Caloria': '2.6', 'Proteina': '125', 'Calcio': '4.0', 'Ferro': '36', 'Vitamina A': '7.2', 'Tiamina': '9.0', 'Riboflavina': '4.5', 'Niacina': '26', 'Acido Ascorbico': '5369'},
    {'Numero': '50', 'Mercadoria': 'Cebola', 'Caloria': '5.8', 'Proteina': '166', 'Calcio': '3.8', 'Ferro': '59', 'Vitamina A': '16.6', 'Tiamina': '4.7', 'Riboflavina': '5.9', 'Niacina': '21', 'Acido Ascorbico': '1184'},
    {'Numero': '51', 'Mercadoria': 'Batatas', 'Caloria': '14.3', 'Proteina': '336', 'Calcio': '1.8', 'Ferro': '118', 'Vitamina A': '6.7', 'Tiamina': '29.4', 'Riboflavina': '7.1', 'Niacina': '198', 'Acido Ascorbico': '2522'},
    {'Numero': '52', 'Mercadoria': 'Espinafre', 'Caloria': '1.1', 'Proteina': '106', 'Calcio': '0', 'Ferro': '138', 'Vitamina A': '918.4', 'Tiamina': '5.7', 'Riboflavina': '13.8', 'Niacina': '33', 'Acido Ascorbico': '2755'},
    {'Numero': '53', 'Mercadoria': 'Batata-doce', 'Caloria': '9.6', 'Proteina': '138', 'Calcio': '2.7', 'Ferro': '54', 'Vitamina A': '290.7', 'Tiamina': '8.4', 'Riboflavina': '5.4', 'Niacina': '83', 'Acido Ascorbico': '1912'},
    {'Numero': '64', 'Mercadoria': 'Pêssegos. secos', 'Caloria': '8.5', 'Proteina': '87', 'Calcio': '1.7', 'Ferro': '173', 'Vitamina A': '86.8', 'Tiamina': '1.2', 'Riboflavina': '4.3', 'Niacina': '65', 'Acido Ascorbico': '257'},
    {'Numero': '65', 'Mercadoria': 'Ameixas secas', 'Caloria': '12.8', 'Proteina': '99', 'Calcio': '2.5', 'Ferro': '154', 'Vitamina A': '85.7', 'Tiamina': '3.9', 'Riboflavina': '4.3', 'Niacina': '65', 'Acido Ascorbico': '257'},
    {'Numero': '68', 'Mercadoria': 'Feijão verde. seco', 'Caloria': '17.4', 'Proteina': '1055', 'Calcio': '3.7', 'Ferro': '459', 'Vitamina A': '5.1', 'Tiamina': '26.9', 'Riboflavina': '38.2', 'Niacina': '93', 'Acido Ascorbico': '0'},
    {'Numero': '69', 'Mercadoria': 'Feijão branco. seco', 'Caloria': '26.9', 'Proteina': '1691', 'Calcio': '11.4', 'Ferro': '792', 'Vitamina A': '0', 'Tiamina': '38.4', 'Riboflavina': '24.6', 'Niacina': '217', 'Acido Ascorbico': '0'}
]

def printA(A):   #Função para printar uma matriz formatada
    for linha in A:
        print(" ".join(f"{elem:<10}" for elem in linha))  #Alinhamento à direita com 5 espaços por coluna

NAME = input("Digite um nome: ")
if len(NAME) >= 5:
    NAME = NAME[:5].upper()   #5 primeiras letras do nome a ser analisado
else:
    NAME = "NICOL"

idPrudutos = [1, 15, 19, 30, 46, 52, 53, 68]  #ID dos produtos que serão usados na tabela 2
produtoX = np.array([1000, 0.1, 1000, 0.1, 1])   #Vetor que conterá as quantidades de nutrientes para o produto X (depende das letras do nome)
At = []   #Esta matriz será a matriz A transposta
b = np.array([100, 0.01, 100, 0.1, 1])   #Este vetor terá os valores das restrições (depende das letras do nome)
c = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1])   #Vetor para os coeficientes das variáveis de decisão na função objetivo
c_folga = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0])   #Vetor c com as variáveis de folga

#Adicionando as linhas correspondentes aos produtos na matriz:
for row in nutricao:
    if int(row['Numero']) in idPrudutos:
        At.append([float(row['Caloria']) * 1000, float(row['Calcio']) * 1, float(row['Vitamina A']) * 1000, float(row['Riboflavina']) * 1, float(row['Acido Ascorbico']) * 1])   #Adicionando uma linha na matriz A

#Adicionando a linha correspondente aos valores do produto X na matriz:
letraAtual = 0
while letraAtual < len(NAME):
    for row in letras:
        if row['Letra'] == NAME[letraAtual]:
            b[letraAtual] = b[letraAtual] * float(row['Dieta'])
            produtoX[letraAtual] = produtoX[letraAtual] * float(row['ProdutoX'])
            letraAtual += 1
            break
At.append(produtoX)

At = np.array(At)  #Matriz transposta como numpy array
A = At.T           #Transposição para obter matriz A

#Fazendo uma versão da matriz A com as variáveis de folga (não é necessário, já que o linprog consegue resolver um problema do tipo Ax<=b):
A_folga = A
for i in range(5):
    vetorFolga = np.array([[0], [0], [0], [0], [0]])
    vetorFolga[i] = -1
    A_folga = np.hstack((A_folga, vetorFolga))

#Restrições de não negatividade:
x_bounds = (0, None)

#O módulo linprog resolve para Ax<=b, mas atualmente temos Ax>=b. Para fazer a transformação, basta multiplicar as restrições por -1:
result = sco.linprog(c, A_ub=-A, b_ub=-b, bounds=x_bounds, method='simplex')
result_folga = sco.linprog(c_folga, A_eq=A_folga, b_eq=b, bounds=x_bounds, method='simplex')   #Usando variáveis de folga, teremos Ax=b

print(f"Usando o nome {NAME}\nVetor de restrições b: {b}\nVetor de coeficientes c: {c}\nMatriz A:")
printA(A)
print("\n====RESULTADOS=====\na)")
print(f"Valor mínimo a ser gasto: {result.fun} (resultado sem usar variáveis de folga)\nValor mínimo a ser gasto: {result_folga.fun} (resultado usando variáveis de folga)\n\nDólares gastos na farinha de trigo (enriquecida): {result.x[0]}\n\
Dólares gastos no leite evaporado: {result.x[1]}\nDólares gastos no queijo cheddar: {result.x[2]}\n\
Dólares gastos no fígado bovino: {result.x[3]}\nDólares gastos no repolho: {result.x[4]}\n\
Dólares gastos no espinafre: {result.x[5]}\nDólares gastos na batata doce: {result.x[6]}\n\
Dólares gastos no feijão verde (seco): {result.x[7]}\nDólares gastos no Produto X: {result.x[8]}")


#letra B
print("\nb)")
c_letraB = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

#Vitamina A pura:
precoVitaminaA = 0.00000001
vitaminaAPorDolar = 1/precoVitaminaA
new_elements = np.array([[0], [0], [vitaminaAPorDolar], [0], [0]])
A_vitA = np.hstack((A, new_elements))
old_result = sco.linprog(c_letraB, A_ub=-A_vitA, b_ub=-b, bounds=x_bounds, method='simplex')
vantajoso = True
while True:
    precoVelho = precoVitaminaA
    precoVitaminaA += 0.00000001
    vitaminaAPorDolar = 1/precoVitaminaA
    new_elements = np.array([[0], [0], [vitaminaAPorDolar], [0], [0]])
    A_vitA = np.hstack((A, new_elements))
    result = sco.linprog(c_letraB, A_ub=-A_vitA, b_ub=-b, bounds=x_bounds, method='simplex')
    if result.x[9] == 0:
        if old_result.x[9] == 0:
            vantajoso = False
        break
    old_result = result
if vantajoso:
    print(f"Para o nome {NAME}, seria vantajoso pagar até {precoVelho} dólares por U.I de vitamina A pura.")
else:
    print(f"Para o nome {NAME}, não seria vantajoso comprar a vitamina A pura.")

#Riboflavina pura:
precoRiboflavina = 0.0001
riboflavinaPorDolar = 1/precoRiboflavina
new_elements = np.array([[0], [0], [0], [riboflavinaPorDolar], [0]])
A_rib = np.hstack((A, new_elements))
old_result = sco.linprog(c_letraB, A_ub=-A_rib, b_ub=-b, bounds=x_bounds, method='simplex')
vantajoso = True
while True:
    precoVelho = precoRiboflavina
    precoRiboflavina += 0.0001
    riboflavinaPorDolar = 1/precoRiboflavina
    new_elements = np.array([[0], [0], [0], [riboflavinaPorDolar], [0]])
    A_rib = np.hstack((A, new_elements))
    result = sco.linprog(c_letraB, A_ub=-A_rib, b_ub=-b, bounds=x_bounds, method='simplex')
    if result.x[9] == 0:
        if old_result.x[9] == 0:
            vantajoso = False
        break
    old_result = result
if vantajoso:
    print(f"Para o nome {NAME}, seria vantajoso pagar até {precoVelho} dólares por mg de riboflavina pura.")
else:
    print(f"Para o nome {NAME}, não seria vantajoso comprar a riboflavina pura.")