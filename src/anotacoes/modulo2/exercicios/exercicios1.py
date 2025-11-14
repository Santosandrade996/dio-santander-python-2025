# Exemplos para testar o modo interativo do Python

#Variáveis Simples
nome = "Ana"
idade = 25
altura = 1.68

# Função Simples
def saudacao(nome):
    return f"Olá, {nome}! Bem-vindo ao Python."

# Função de cálculo
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

#lista de exemplos

frutas = ["maçã", "banana", "laranja", "uva"]

# Dicionário de exemplo
pessoa = {
    "nome": "Carlos",
    "idade": 30,
    "cidade": "São Paulo"
}

# Função mais elaborada

def  tabuada(numero):
    resultado = {}
    for i in range(1, 11):
        resultado[i] = numero * i
    return resultado

#Mensagem final

print("Arquivo carregado com sucesso!")
print("\nVariáveis e funções disponíveis:")
print("- nome, idade, altura")
print("- saudacao(nome)")
print("- calcular_imc(peso, altura)")
print("- frutas (lista)")
print("- pessoa (dicionário)")
print("- tabuada(numero)")
print("\nExperimente usar essas funções no modo interativo!")

print("\nCada tópico citados de código acima, é para serem testados cada um, para ver como funciona cada codigo e não tudo de uma vez...")

