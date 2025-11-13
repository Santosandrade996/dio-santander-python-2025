# 📚 Módulo 2: Conhecendo a Linguagem de Programação Python

## 📋 Índice

- [Modo Interativo](#-modo-interativo)
- [Variáveis e Constantes](#-variáveis-e-constantes)
- [Tipos de Dados](#-tipos-de-dados)
- [Conversão de Tipos](#-conversão-de-tipos)
- [Funções de Entrada e Saída](#-funções-de-entrada-e-saída)
- [Exercícios Práticos](#-exercícios-práticos)

---

## 🖥️ Modo Interativo

O modo interativo permite executar código Python linha por linha, ideal para testes e aprendizado.

### Como usar

```powershell
# Entrar no modo interativo
python

# Executar arquivo e entrar no modo interativo
python -i arquivo.py
```

### Exemplos no modo interativo

```python
>>> 2 + 2
4

>>> nome = "Giselle"
>>> nome
'Giselle'

>>> def saudacao(nome):
...     return f"Olá, {nome}!"
...
>>> saudacao("Python")
'Olá, Python!'

>>> dir()  # Ver variáveis no escopo
['__builtins__', '__doc__', 'nome', 'saudacao']

>>> help(print)  # Ver documentação
>>> exit()  # Sair do modo interativo
```

### Função `dir()`

- **Sem argumento**: Retorna lista de nomes no escopo atual
- **Com argumento**: Retorna lista de atributos válidos para o objeto

```python
>>> dir()  # Mostra escopo atual
>>> dir(str)  # Mostra métodos de string
>>> dir([])  # Mostra métodos de lista
```

---

## 📦 Variáveis e Constantes

### Variáveis

Variáveis armazenam valores que podem mudar durante a execução do programa.

**Convenção de nomenclatura: snake_case (minúsculas com underline)**

```python
# Variáveis válidas
nome = "Giselle"
idade = 25
saldo_conta = 1500.50
numero_tentativas = 3
esta_ativo = True

# Múltiplas atribuições
x, y, z = 10, 20, 30
a = b = c = 0
```

### Constantes

Constantes são valores que NÃO devem mudar durante a execução.

**Convenção de nomenclatura: UPPER_CASE (maiúsculas com underline)**

```python
# Constantes
LIMITE_SAQUE = 1000
TAXA_JUROS = 0.05
VALOR_MAXIMO = 5000
PI = 3.14159
NOME_EMPRESA = "DIO Bank"

# Python não impede alteração, mas a convenção indica que não deve mudar
```

### Regras para nomes de variáveis

✅ **Permitido:**

- Letras (a-z, A-Z)
- Números (0-9) - mas não no início
- Underline (_)

❌ **NÃO permitido:**

- Começar com número
- Espaços
- Caracteres especiais (@, #, $, %, etc.)
- Palavras reservadas (if, for, while, etc.)

```python
# ✅ CORRETO
nome_completo = "Giselle Santos"
idade1 = 25
_privado = "valor"

# ❌ ERRADO
1nome = "erro"  # Começa com número
nome-completo = "erro"  # Tem hífen
nome completo = "erro"  # Tem espaço
for = 10  # Palavra reservada
```

---

## 🔢 Tipos de Dados

**Os tipos de dados definem as características e comportamentos de um valor.**

### Tipos Numéricos

```python
# int - Números inteiros
idade = 25
quantidade = 100
negativo = -50

# float - Números decimais
altura = 1.65
preco = 29.99
pi = 3.14159

# complex - Números complexos
complexo = 5 + 3j
```

### Tipo Texto

```python
# str - String (texto)
nome = "Giselle"
cidade = 'Nova Iguaçu'
mensagem = """Texto
com múltiplas
linhas"""

# Métodos de string
texto = "python"
print(texto.upper())  # PYTHON
print(texto.capitalize())  # Python
print(texto.replace("p", "P"))  # Python
```

### Tipo Booleano

```python
# bool - True ou False
esta_ativo = True
tem_saldo = False

# Operações lógicas
print(not esta_ativo)  # False
print(esta_ativo and tem_saldo)  # False
print(esta_ativo or tem_saldo)  # True
```

### Tipos de Coleção

```python
# list - Lista (mutável)
frutas = ["maçã", "banana", "laranja"]
numeros = [1, 2, 3, 4, 5]
mista = [1, "texto", True, 3.14]

# tuple - Tupla (imutável)
coordenadas = (10, 20)
dias_semana = ("segunda", "terça", "quarta")

# dict - Dicionário (chave-valor)
pessoa = {
    "nome": "Giselle",
    "idade": 25,
    "cidade": "Nova Iguaçu"
}

# set - Conjunto (valores únicos)
numeros_unicos = {1, 2, 3, 4, 5}
```

### Verificando tipos

```python
>>> type(10)
<class 'int'>

>>> type(3.14)
<class 'float'>

>>> type("texto")
<class 'str'>

>>> type(True)
<class 'bool'>

>>> type([1, 2, 3])
<class 'list'>

>>> isinstance(10, int)
True
```

---

## 🔄 Conversão de Tipos

Também conhecida como **casting** ou **type casting**.

### Conversão para int

```python
# float para int (perde a parte decimal)
numero = int(3.14)  # 3

# string para int
idade = int("25")  # 25

# bool para int
verdadeiro = int(True)  # 1
falso = int(False)  # 0

# ❌ ERRO - string não numérica
# numero = int("abc")  # ValueError
```

### Conversão para float

```python
# int para float
numero = float(10)  # 10.0

# string para float
preco = float("29.99")  # 29.99

# bool para float
valor = float(True)  # 1.0
```

### Conversão para string

```python
# int para string
texto = str(25)  # "25"

# float para string
preco = str(29.99)  # "29.99"

# bool para string
status = str(True)  # "True"

# list para string
lista = str([1, 2, 3])  # "[1, 2, 3]"
```

### Conversão para bool

```python
# Valores considerados False
print(bool(0))  # False
print(bool(0.0))  # False
print(bool(""))  # False
print(bool([]))  # False
print(bool(None))  # False

# Outros valores são True
print(bool(1))  # True
print(bool(-5))  # True
print(bool("texto"))  # True
print(bool([1, 2]))  # True
```

### Conversão para list, tuple, set

```python
# String para lista
letras = list("python")  # ['p', 'y', 't', 'h', 'o', 'n']

# Tupla para lista
lista = list((1, 2, 3))  # [1, 2, 3]

# Lista para tupla
tupla = tuple([1, 2, 3])  # (1, 2, 3)

# Lista para set (remove duplicatas)
unicos = set([1, 2, 2, 3, 3, 3])  # {1, 2, 3}
```

---

## 📥📤 Funções de Entrada e Saída

### Função `print()` - Saída

Exibe informações na tela.

```python
# Print simples
print("Olá, mundo!")

# Múltiplos valores
print("Nome:", "Giselle", "Idade:", 25)

# Separador customizado
print("Python", "é", "incrível", sep="-")  # Python-é-incrível

# Fim de linha customizado
print("Primeira linha", end=" ")
print("mesma linha")  # Primeira linha mesma linha

# Formatação com f-string
nome = "Giselle"
idade = 25
print(f"Olá, {nome}! Você tem {idade} anos.")

# Formatação com .format()
print("Olá, {}! Você tem {} anos.".format(nome, idade))

# Formatação com %
print("Olá, %s! Você tem %d anos." % (nome, idade))
```

### Função `input()` - Entrada

Recebe dados do usuário (sempre retorna string).

```python
# Input simples
nome = input("Digite seu nome: ")
print(f"Olá, {nome}!")

# Input com conversão para int
idade = int(input("Digite sua idade: "))
print(f"Você tem {idade} anos.")

# Input com conversão para float
altura = float(input("Digite sua altura: "))
print(f"Sua altura é {altura}m")

# Múltiplos inputs
nome = input("Nome: ")
idade = int(input("Idade: "))
cidade = input("Cidade: ")
```

### Exemplo completo de programa

```python
# Programa calculadora de IMC
print("=== CALCULADORA DE IMC ===")
print()

nome = input("Digite seu nome: ")
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / (altura ** 2)

print()
print(f"{nome}, seu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif imc < 25:
    print("Classificação: Peso normal")
elif imc < 30:
    print("Classificação: Sobrepeso")
else:
    print("Classificação: Obesidade")
```

---

## 💪 Exercícios Práticos

### Exercício 1: Modo Interativo

Abra o modo interativo e execute:

```python
# 1. Crie uma variável com seu nome
# 2. Crie uma variável com sua idade
# 3. Use dir() para ver as variáveis criadas
# 4. Use type() para verificar o tipo de cada variável
# 5. Crie uma função que retorne a soma de dois números
```

### Exercício 2: Variáveis e Constantes

Crie um arquivo `exercicio2.py`:

```python
# Declare as seguintes constantes:
# - TAXA_JUROS = 0.05
# - LIMITE_SAQUE_DIARIO = 3000
# - VALOR_MINIMO_INVESTIMENTO = 100

# Declare as seguintes variáveis:
# - nome_cliente com seu nome
# - saldo_conta = 5000.00
# - numero_saques_realizados = 0
# - conta_ativa = True

# Imprima todas as variáveis e constantes
```

### Exercício 3: Tipos de Dados

```python
# Crie variáveis de cada tipo:
# 1. Um inteiro com sua idade
# 2. Um float com sua altura
# 3. Uma string com seu nome completo
# 4. Um booleano indicando se está estudando
# 5. Uma lista com 3 frutas favoritas
# 6. Um dicionário com nome, idade e cidade

# Use type() para verificar cada tipo
# Use print() para exibir cada valor
```

### Exercício 4: Conversão de Tipos

```python
# 1. Converta a string "100" para int e some com 50
# 2. Converta o número 3.14159 para int (veja o que acontece)
# 3. Converta o número 42 para string e concatene com " é a resposta"
# 4. Converta a lista [1, 2, 3] para tupla
# 5. Converta a string "python" para lista
# 6. Crie uma lista [1, 1, 2, 2, 3] e converta para set
```

### Exercício 5: Calculadora Simples

```python
# Crie uma calculadora que:
# 1. Peça dois números ao usuário
# 2. Peça a operação (+, -, *, /)
# 3. Realize o cálculo
# 4. Exiba o resultado formatado

# Exemplo de saída:
# Digite o primeiro número: 10
# Digite o segundo número: 5
# Digite a operação (+, -, *, /): +
# Resultado: 10 + 5 = 15
```

### Exercício 6: Cadastro de Pessoa

```python
# Crie um programa que:
# 1. Peça nome, idade, altura e peso do usuário
# 2. Calcule o IMC (peso / altura²)
# 3. Crie um dicionário com todos os dados
# 4. Exiba os dados formatados

# Exemplo de saída:
# === CADASTRO COMPLETO ===
# Nome: Giselle Santos
# Idade: 25 anos
# Altura: 1.65m
# Peso: 60.0kg
# IMC: 22.04 (Peso normal)
```

### Exercício 7: Conversor de Temperatura

```python
# Crie um conversor que:
# 1. Peça uma temperatura em Celsius
# 2. Converta para Fahrenheit (F = C * 9/5 + 32)
# 3. Converta para Kelvin (K = C + 273.15)
# 4. Exiba todos os valores formatados com 2 casas decimais

# Exemplo de saída:
# Digite a temperatura em Celsius: 25
# 25.00°C = 77.00°F = 298.15K
```

### Exercício 8: Sistema Bancário Simples

```python
# Crie um programa que:
# 1. Defina constantes: LIMITE_SAQUE = 500, TAXA_TRANSFERENCIA = 0.01
# 2. Peça o nome do cliente
# 3. Peça o saldo inicial
# 4. Peça o valor que deseja sacar
# 5. Verifique se o saque é possível (não excede limite e saldo)
# 6. Se possível, realize o saque e mostre o novo saldo
# 7. Se não, mostre mensagem de erro

# Adicione validações e mensagens informativas
```

### Exercício Desafio: Calculadora de Investimentos

```python
# Crie um programa que:
# 1. Peça o valor inicial do investimento
# 2. Peça a taxa de juros mensal (em %)
# 3. Peça o número de meses
# 4. Calcule o montante final usando juros compostos
#    Fórmula: M = C * (1 + i)^t
#    M = montante, C = capital inicial, i = taxa, t = tempo
# 5. Exiba:
#    - Valor investido
#    - Taxa de juros
#    - Período
#    - Montante final
#    - Lucro obtido (Montante - Capital inicial)

# Exemplo de saída:
# === SIMULAÇÃO DE INVESTIMENTO ===
# Valor investido: R$ 1000.00
# Taxa de juros: 1.5% ao mês
# Período: 12 meses
# Montante final: R$ 1195.62
# Lucro obtido: R$ 195.62
```

---

## 📝 Respostas das Questões Teóricas

### Qual o retorno da função builtin dir?

**Resposta:** Sem argumento retorna a lista de nomes no escopo e com um argumento, retorna uma lista de atributos válidos para o objeto.

### Por que usamos tipos de dados?

**Resposta:** Os tipos de dados definem as características e comportamentos de um valor.

### Seguindo a convenção, qual a melhor forma de declarar a constante limite do saque em Python?

**Resposta:** `LIMITE_SAQUE = 1000`

---

## 🎯 Checklist de Aprendizado

- [ ] Sei usar o modo interativo do Python
- [ ] Entendo a diferença entre variáveis e constantes
- [ ] Conheço as convenções de nomenclatura (snake_case e UPPER_CASE)
- [ ] Conheço os principais tipos de dados (int, float, str, bool, list, dict)
- [ ] Sei usar a função `type()` e `isinstance()`
- [ ] Sei fazer conversões entre tipos (casting)
- [ ] Sei usar `input()` para receber dados do usuário
- [ ] Sei usar `print()` com formatação (f-string, .format(), %)
- [ ] Consigo criar programas simples que recebem entrada e exibem saída

---

## 📚 Referências e Próximos Passos

- **PEP 8:** Guia de estilo oficial do Python
- **Documentação oficial:** <https://docs.python.org>
- **Próximo módulo:** Operadores e Estruturas de Controle

---

**Criado por:** Giselle Santos  
**Bootcamp:** DIO - Santander 2025  
**Data:** Novembro 2024
