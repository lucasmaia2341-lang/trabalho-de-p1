# 🎮 Sistema de Fichas de Personagem (RPG)

Projeto desenvolvido em **Python** com o objetivo de criar um sistema simples de **gerenciamento de fichas de personagens**, utilizando conceitos básicos de programação.

O programa permite criar, listar e apagar fichas de personagens, além de salvar os dados em um arquivo JSON.

---

## 📌 Funcionalidades

- Criar até **3 fichas de personagens**
- Cada ficha possui:
  - Nome
  - Arma
  - Item
- Listar todas as fichas criadas
- Apagar uma ficha escolhida pelo usuário
- Salvar os dados em arquivo (`jogadores.json`)
- Menu interativo no terminal

---

## 🧠 Conceitos utilizados

Este projeto utiliza os seguintes conceitos de programação:

- Menu interativo com `input()`
- Estruturas condicionais (`if / elif / else`)
- Laços de repetição (`while`)
- Listas
- Dicionários
- Funções (`def`)
- Manipulação de arquivos (leitura e escrita)
- Formato JSON
- Organização de código

---

## 🗂 Estrutura dos dados

Cada personagem é representado por um **dicionário**:

```python
{
  "nome": "Teak",
  "arma": "Foice",
  "item": "Poção"
}
