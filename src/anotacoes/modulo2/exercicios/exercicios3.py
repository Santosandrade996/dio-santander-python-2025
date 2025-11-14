# Exercício 3: Tipos de Dados
from plyer import notification
notification.notify(
    title="Exercício 3: Tipos de Dados",
    message="Cada tópico citados de código acima, é para serem testados cada um, para ver como funciona cada codigo e não tudo de uma vez...",
    timeout=30
    
)

print("-" * 50) 
print("Tipos de Dados em Python")
print("-" * 50)

# Tipo de dado: Inteiro (int)

idade = 30
print(f"\n1. Inteiro (int):")
print(f"     Valor: {idade}, Tipo: {type(idade)}")

# Tipo de dado: Ponto Flutuante (float-Números Decimais)
altura = 1.75
print(f"\n2. Ponto Flutuante (float):")
print(f"     Valor: {altura}, Tipo: {type(altura)}")

# Tipo de dado: String (str-Texto)
nome_completo = "Maria Oliveira"
print(f"\n3. String (str):")
print(f"     Valor: {nome_completo}, Tipo: {type(nome_completo)}")

# Booleano (bool-Verdadeiro ou Falso-TRUE/FALSE)
ESTA_ESTUDANDO = True
print(f"\n4. Booleano (bool):")
print(f"     Valor: {ESTA_ESTUDANDO}, Tipo: {type(ESTA_ESTUDANDO)}")

#LISTA (list-coleção ordenada e mutável)
frutas_favoritas = ["maçã", "banana", "laranja"]
print(f"\n5. Lista (list):")
print(f"     Valor: {frutas_favoritas}, Tipo: {type(frutas_favoritas)}")

# DICIONÁRIO (dict-coleção de pares chave-valor)
dados_pessoais = {"nome": "Carlos", "idade": 28, "cidade": "Rio de Janeiro"}
print(f"\n6. Dicionário (dict):")
print(f"     Valor: {dados_pessoais}, Tipo: {type(dados_pessoais)}")

# Verificando tipos com isinstance()
print("\n" + "=" * 60)
print("VERIFICANDO TIPOS COM isinstance()")
print("=" * 60)

print(f"idade é int? {isinstance(idade, int)}")
print(f"altura é float? {isinstance(altura, float)}")
print(f"nome_completo é str? {isinstance(nome_completo, str)}")
print(f"esta_estudando é bool? {isinstance(ESTA_ESTUDANDO, bool)}")
print(f"frutas_favoritas é list? {isinstance(frutas_favoritas, list)}")
print(f"meus_dados é dict? {isinstance(dados_pessoais, dict)}")
print("=" * 60)

