def tem_digitos_adjacentes(numero): # Converte o número em valor absoluto para lidar com negativos
    num_str = str(abs(numero)) # Verifica se há dois dígitos adjacentes iguais
    return any(num_str[i] == num_str[i + 1] for i in range(len(num_str) - 1))

n = int(input("Digite a quantidade de números: ")) # Pede a quantidade de números para ser lidos

i = 0

while(i < n):
   if any(tem_digitos_adjacentes(int(input("Digite um número: "))) for _ in range(n)): #Verifica se um dos números informados tem adjacentes iguais
       print("Um dos números tem adjacentes iguais.") 
   else:
       print("Nenhum dos números tem adjacentes iguais.")

i = i + 1
