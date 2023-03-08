# Sequencia de Fibonacci

qt_termos = int(input("Informe a quantidade de termos: "))
verifica_num = int(input("Informe um número para a verificação: "))
n1 = 0
n2 = 1
cont = 0
fibonacci = []

while cont < qt_termos:
    fibonacci.append(n1)
    num = n1 + n2
    n1 = n2
    n2 = num

    cont += 1

if verifica_num not in fibonacci:
    print(f"O número {verifica_num} não está dentro da sequencia")

else:
    print(f"O número {verifica_num} está dentro da sequência")
