# Exercício 2: Variáveis e Constantes

# Declarando CONSTANTES (maiúsculas)
TAXA_JUROS = 0.05  # 5% de taxa de juros anual
LIMITE_SAQUE_DIARIO = 500.00  # Limite diário de saque em reais
VALOR_MINIMO_INVESTIMENTO = 1000.00  # Valor mínimo para investimento em reais

#Imprimindo as COnstantes. 

print("-" * 50)
print("Constantes:")
print("-" * 50)
print(f"TAXA_JUROS: {TAXA_JUROS}")
print(f"LIMITE_SAQUE_DIARIO: R$ {LIMITE_SAQUE_DIARIO:.2f}")
print(f"VALOR_MINIMO_INVESTIMENTO: R$ {VALOR_MINIMO_INVESTIMENTO:.2f}")

# Declarando variáveis (minúsculas)
nome_cliente = "João Silva"
saldo_conta = 1500.75  # Saldo atual da conta em reais
numero_saques_realizados = 2  # Número de saques realizados hoje
conta_ativa = True  # Indica se a conta está ativa

# Imprimindo as variáveis
print("-" * 50)
print("DADOS DA CONTA:")
print("-" * 50)
print(f"Nome do Cliente: {nome_cliente}")
print(f"Saldo da Conta: R$ {saldo_conta:.2f}")
print(f"Número de Saques Realizados Hoje: {numero_saques_realizados}")
print(f"Conta Ativa: {'Sim' if conta_ativa else 'Não'}")
print("-" * 50)

