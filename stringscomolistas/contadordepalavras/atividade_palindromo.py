string = input("Digite um texto: ")  # Solicita ao usuário para inserir um texto
inversa = ""  # Inicializa a string que vai ser armazenada a versão invertida

stringlower = string.lower()  # Converte a string para minúsculas
pontuacao = [".", "," , ":" , ";" , "!" , "?"]  # Lista de caracteres de pontuação que serão removidos

# Remove as pontuações
for p in pontuacao:
    stringlower = stringlower.replace(p, "")

# Inverte a string
for x in stringlower:
    inversa = x + inversa

print(inversa)  # Exibe a versão invertida

# Verifica se a string original é igual a versão invertida
if stringlower == inversa:
    print("É palíndromo")  # Se for um palíndromo
else:
    print("Não é palíndromo")  # Caso não for um palíndromo
