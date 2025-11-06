# 📘 Módulo 1 - Introdução ao Python

## 📋 Sobre o Módulo

Este módulo apresenta os fundamentos da linguagem Python, configuração do ambiente de desenvolvimento e a criação do primeiro programa.

**Carga Horária:** [X horas]  
**Status:** 🔄 Em andamento

---

## 📚 Conteúdo Programático

### 1. Introdução ao Python

#### O que é Python?

Python é uma linguagem de programação de alto nível, interpretada e de propósito geral, criada por Guido van Rossum em 1991.

#### Características Principais

- **Sintaxe Simples e Legível:** Código limpo e fácil de entender
- **Interpretada:** Não precisa compilar antes de executar
- **Multiplataforma:** Funciona em Windows, Linux e MacOS
- **Multiparadigma:** Suporta programação orientada a objetos, funcional e procedural
- **Grande Comunidade:** Vasta biblioteca de pacotes e frameworks

#### Por que Python?

- Fácil de aprender para iniciantes
- Amplamente utilizada em:
  - Desenvolvimento Web (Django, Flask)
  - Ciência de Dados e Machine Learning
  - Automação e Scripts
  - Desenvolvimento de APIs
  - Análise de Dados

#### Versões do Python

- **Python 2.x:** Descontinuada (não usar em novos projetos)
- **Python 3.x:** Versão atual e recomendada

---

### 2. Configuração do Ambiente de Desenvolvimento

#### Instalação do Python

**Windows:**

1. Acesse [python.org](https://www.python.org/downloads/)
2. Baixe o instalador da versão mais recente
3. Execute o instalador
4. ⚠️ **IMPORTANTE:** Marque a opção "Add Python to PATH"
5. Clique em "Install Now"

**Linux (Ubuntu/Debian):**

```bash

sudo apt update
sudo apt install python3 python3-pip
```

**MacOS:**

```bash

brew install python3
```

#### Verificando a Instalação

Abra o terminal/prompt e digite:

```bash

python --version
# ou
python3 --version
```

Deve retornar algo como: `Python 3.x.x`

#### Instalando o Visual Studio Code

1. Acesse [code.visualstudio.com](https://code.visualstudio.com/)
2. Baixe e instale o VS Code
3. Abra o VS Code
4. Instale a extensão do Python:
   - Clique no ícone de extensões (quadrado na barra lateral)
   - Pesquise por "Python"
   - Instale a extensão da Microsoft

#### Extensões Recomendadas para o VS Code

- **Python** (Microsoft) - Essencial
- **Pylance** - IntelliSense avançado
- **Python Indent** - Indentação automática
- **autoDocstring** - Geração de docstrings
- **Better Comments** - Comentários coloridos

#### Configurando o Interpretador Python no VS Code

1. Abra um arquivo `.py`
2. Pressione `Ctrl+Shift+P` (ou `Cmd+Shift+P` no Mac)
3. Digite "Python: Select Interpreter"
4. Selecione a versão do Python instalada

---

### 3. Primeiro Programa

#### Hello World - O Clássico

Crie um arquivo chamado `hello.py`:

```python
print("Hello, World!")
```

**Executando o programa:**

```bash

python hello.py
# ou
python3 hello.py
```

**Saída esperada:**

```

Hello, World!

```

#### Programa Interativo - Solicitando Nome

```python
# Programa que pergunta o nome do usuário
nome = input("Digite seu nome: ")
print(f"Olá, {nome}! Bem-vindo ao Python!")
```

**Exemplo de execução:**

```
Digite seu nome: João
Olá, João! Bem-vindo ao Python!

```

#### Programa com Cálculo Simples

```python
# Calculadora de soma simples
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

soma = numero1 + numero2

print(f"A soma de {numero1} + {numero2} = {soma}")
```

#### Entendendo o Código

- `print()`: Função para exibir mensagens na tela
- `input()`: Função para receber entrada do usuário (retorna string)
- `int()`: Converte string para número inteiro
- `f"..."`: F-string, permite inserir variáveis dentro de strings
- `#`: Comentário de uma linha

---

## 💻 Projetos Práticos Desenvolvidos

### Projeto 1: Hello World

- **Arquivo:** `hello.py`
- **Objetivo:** Primeiro programa em Python
- **Conceitos:** Função print()

### Projeto 2: Programa Interativo

- **Arquivo:** `saudacao.py`
- **Objetivo:** Interagir com o usuário
- **Conceitos:** input(), variáveis, f-strings

### Projeto 3: Calculadora Simples

- **Arquivo:** `calculadora.py`
- **Objetivo:** Realizar operações matemáticas básicas
- **Conceitos:** Conversão de tipos, operadores aritméticos

---

## 📝 Anotações Importantes

### Dicas de Boas Práticas

- Use nomes de variáveis descritivos (ex: `nome_usuario` ao invés de `n`)
- Sempre comente seu código para facilitar o entendimento
- Siga a PEP 8 (guia de estilo do Python)
- Indentação é fundamental em Python (use 4 espaços)

### Comandos Úteis no Terminal

```bash
# Executar arquivo Python
python arquivo.py

# Abrir Python interativo
python

# Instalar pacotes
pip install nome_pacote

# Ver versão do pip
pip --version

# Listar pacotes instalados
pip list
```

### Atalhos Úteis no VS Code

- `Ctrl + Enter`: Executar linha atual no terminal Python
- `Shift + Enter`: Executar linha e ir para próxima
- `Ctrl + /`: Comentar/descomentar linha
- `F5`: Iniciar debug

---

## 🎯 Conceitos Aprendidos

- ✅ O que é Python e suas características
- ✅ Instalação do Python e VS Code
- ✅ Configuração do ambiente de desenvolvimento
- ✅ Função `print()` para exibir saída
- ✅ Função `input()` para receber entrada do usuário
- ✅ Variáveis e tipos de dados básicos
- ✅ Conversão de tipos (type casting)
- ✅ F-strings para formatação de texto
- ✅ Operações matemáticas básicas
- ✅ Comentários no código

---

## 🔗 Links Úteis

- [Documentação Oficial do Python](https://docs.python.org/pt-br/3/)
- [PEP 8 - Guia de Estilo](https://peps.python.org/pep-0008/)
- [Python para Iniciantes](https://www.python.org/about/gettingstarted/)
- [Real Python - Tutoriais](https://realpython.com/)
- [W3Schools Python](https://www.w3schools.com/python/)

---

## 📚 Próximos Passos

No próximo módulo, vamos aprender sobre:

- Tipos de dados em Python
- Modo interativo
- Variáveis e constantes
- conversão de tipos
- Funções de entrada e saída

---

## ✅ Checklist de Conclusão

- [ ] Python instalado e funcionando
- [ ] VS Code configurado com extensão Python
- [ ] Hello World executado com sucesso
- [ ] Programa interativo funcionando
- [ ] Calculadora simples criada
- [ ] Ambiente pronto para próximos módulos

---
---
