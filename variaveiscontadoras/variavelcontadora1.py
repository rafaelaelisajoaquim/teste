n = int(input("Digite um número inteiro positivo: "))
if n < 2:
    print("Não é primo. O número deve ser maior ou igual a 2.")
else:
    numero = 2
    divisores = 0 #divisores é a variável contadora

while (numero <= n-1):
    if (n % numero == 0): #se n é divisivel por numero
        divisores = divisores + 1 
    numero = numero + 1

if (divisores == 0):
    print("É primo.")
elif (divisores == 1):
    print("Não é primo. Possui 1 divisor diferente de 1 e",n)
else:
    print("Não é primo. Possui", divisores,"divisores diferentes de 1 e",n)