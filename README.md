# Problema dos Vasos de Água com Busca em Grafo

Este projeto implementa uma solução para o clássico problema dos **vasos de água**, usando **busca em largura** (BFS) em um **grafo direcionado** para encontrar o menor número de passos até atingir um volume específico de água em um dos recipientes.

## 📋 Descrição

Dado um conjunto de vasos com capacidades específicas, o objetivo é encontrar a menor sequência de ações (encher, esvaziar ou transferir água entre vasos) que leva a um estado onde **pelo menos um vaso contenha exatamente `X` litros de água**.

Este programa:

- Gera todos os estados possíveis a partir de uma configuração inicial;
- Cria um grafo de transições entre estados;
- Utiliza a biblioteca **NetworkX** para encontrar o menor caminho até o objetivo;
- Exibe o caminho encontrado e o visualiza graficamente com **Matplotlib**.

---

## 🚀 Como Executar

### Pré-requisitos

Certifique-se de ter instalado as bibliotecas:

```bash
pip install networkx matplotlib
```

### Rodando o script

Você pode executar o script diretamente em um ambiente Python:

```python
python vasos.py
```

### Exemplo

No final do script, a função é chamada com:

```python
vasos([0, 0, 0], [3, 5, 8], 4)
```

Ou seja:

- Estado inicial: todos os vasos estão vazios
- Capacidades: 3L, 5L e 8L
- Objetivo: encontrar um estado onde algum vaso tenha exatamente 4 litros de água

---

## 🔧 Funções principais

### `gerar_vizinhos(estado, capacidades)`

Gera todos os possíveis estados a partir de um dado estado, considerando as operações:
- Encher um vaso
- Esvaziar um vaso
- Transferir de um vaso para outro

### `vasos(vasos, capacidades, alvo)`

Resolve o problema:
- Constrói o grafo de transições de estados
- Busca o caminho até o estado desejado usando `shortest_path`
- Imprime os passos e gera uma visualização do grafo com o caminho destacado

---

## 🧠 Exemplo de Saída

```
Alvo 4 encontrado em 7 passos:
(0, 0, 0)
(0, 0, 8)
(0, 5, 3)
(3, 5, 0)
(3, 0, 5)
(0, 3, 5)
(0, 5, 3)
(3, 4, 1)
```

---

## 📊 Visualização

O programa gera um grafo visual destacando o caminho da solução em vermelho. Os nós representam os estados dos vasos (ex: `(3, 4, 1)`), e as arestas as operações realizadas entre eles.

---

## 📁 Organização do Código

- `vasos.py`: Código principal com a lógica do problema e visualização.

---

## 🧩 Possíveis Extensões

- Suporte a mais vasos
- Otimizações de performance
- Interface gráfica
- Exportar a solução como animação

---

## 🧑‍💻 Autor

Desenvolvido por Mateu e Maria.