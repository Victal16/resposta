#(1)-------------------------------------------------------
# É um loop que soma os numeros de 1 até 13

INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print(SOMA)

# A saída será:
#91



#(2)--------------------------------------------------------
# Verificar se um número pertence à sequência de Fibonacci

def fibonacci(n):
    fib_sequence = [0, 1]
    while fib_sequence[-1] < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def pertence_fibonacci(num):
    fib_sequence = fibonacci(num)
    if num in fib_sequence:
        return f"O número {num} pertence à sequência de Fibonacci."
    else:
        return f"O número {num} não pertence à sequência de Fibonacci."

# Exemplo de uso
numero = int(input("Informe um número: "))
print(pertence_fibonacci(numero))

# A saída será:
#Informe um número: 5
#O número 5 pertence à sequência de Fibonacci.




#(3)--------------------------------------------------------
# Cálculo de faturamento diário que lê dados de um arquivo JSON

import json

# Exemplo de dados em JSON
data = '''
{
    "faturamento": {
        "1": 100.0,
        "2": 200.0,
        "3": 0.0,
        "4": 150.0,
        "5": 300.0,
        "6": 0.0,
        "7": 250.0
    }
}
'''

# Carregar dados do JSON
faturamento = json.loads(data)["faturamento"]

# Cálculo
valores = list(faturamento.values())
menor = min(valores)
maior = max(valores)
media = sum(valores) / len([v for v in valores if v > 0])  # Ignorar dias sem faturamento
dias_acima_media = len([v for v in valores if v > media])

print(f"Menor faturamento: R${menor:.2f}")
print(f"Maior faturamento: R${maior:.2f}")
print(f"Número de dias acima da média: {dias_acima_media}")

# A saída será:
#Menor faturamento: R$0.00
#Maior faturamento: R$300.00
#Número de dias acima da média: 2



#(4)--------------------------------------------------------
# Cálculo do percentual de representação por estado

# Faturamento mensal por estado
faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

total = sum(faturamento.values())

percentuais = {estado: (valor / total) * 100 for estado, valor in faturamento.items()}

for estado, percentual in percentuais.items():
    print(f"Percentual de {estado}: {percentual:.2f}%")

# A saída será:
#Percentual de SP: 37.53%
#Percentual de RJ: 20.29%
#Percentual de MG: 16.17%
#Percentual de ES: 15.03%
#Percentual de Outros: 10.98%



#(5)--------------------------------------------------------
# Inversão de caracteres de uma string

def inverter_string(s):
    string_invertida = ""
    for char in s:
        string_invertida = char + string_invertida  # Adiciona o caractere no início
    return string_invertida

# Exemplo de uso
entrada = input("Informe uma string: ")
print("String invertida:", inverter_string(entrada))

# A saída será:
#Informe uma string: 35
#String invertida: 53