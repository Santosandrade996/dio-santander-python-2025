#Exemplos para testar o modo interativo do python programando e no terminal...

#variáveis simples
nome  = "Giselle"
idade = 25 
altura = 1.78

#Função simples
def saudacao(nome):
    return f"Olá, {nome}! Bem-Vinda á loucura!"

#função de cálculo
def calcular_imc(peso, altura):
    imc= peso / (altura ** 2)
    return round(imc, 2)

#lista de exemplo
frutas = ["maça" , "tangerina" , "mamão"]

#Dicionário de exemplo 
pessoa = {
    "nome": "Santos",
    "cidade": "Tokio",
    "estado": "Japão"
}

#Função elaborada

def tabuada(numero):
    print(f"\nTabuada do {numero}:")
    for i in range(1, 11):
        resultado = numero  * i
        print(f"{numero} x {i} = {resultado}")
        

#mensagem Inicial 
print("Arquivo carregado com sucesso!")
print("\nVariáveis e funções disponíveis:")
print("- nome, idade, altura")