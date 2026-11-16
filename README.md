# 🎓 Desafio de Aprendizado: Sistema de Notas de Alunos com Funções

## 📖 Sobre o Projeto

Este projeto foi desenvolvido como parte de uma **jornada de aprendizado em Python**, com o objetivo de consolidar o uso de **funções**, **modularização de código**, **parâmetros e retorno de valores**, além de combinar conceitos anteriores como **listas**, **loops aninhados** e **tratamento de exceções**.

O programa simula um sistema acadêmico simples, onde o usuário cadastra alunos com 3 notas cada. O sistema calcula a média, determina a situação (Aprovado/Recuperação/Reprovado) e exibe um relatório formatado, tudo organizado em funções reutilizáveis.

---

## 🎯 Objetivo do Desafio

Praticar e fixar os seguintes conceitos:
- ✅ Definição de funções com `def` e parâmetros
- ✅ Uso de `return` para devolver valores processados
- ✅ Separação de responsabilidades (cada função faz UMA coisa)
- ✅ Composição de funções (uma função recebe o resultado de outra)
- ✅ Loops aninhados para validação granular de entrada
- ✅ Combinação de funções com listas e estruturas de controle

---

## 🧩 Elementos do Código e Seus Objetivos

### Funções

| Função | Parâmetros | Retorno | Objetivo Principal |
|---|---|---|---|
| `calcular_media(notas)` | Lista de notas | `float` (média) | Calcula a média aritmética das notas usando `sum()` e `len()`. |
| `verificar_situacao(media)` | Média (`float`) | `str` (situação) | Classifica o aluno como "Aprovado", "Recuperação" ou "Reprovado" conforme a média. |
| `exibir_relatorio(nome, media, situacao)` | Nome, média e situação | Nenhum (só imprime) | Formata e exibe um relatório visual com os dados do aluno. |

### Programa Principal

| Elemento | Objetivo Principal |
|---|---|
| `while True:` (externo) | Controla o cadastro contínuo de alunos até o usuário digitar "sair". |
| `notas = []` | Inicializa uma lista vazia para armazenar as 3 notas de cada aluno. |
| `for i in range(1, 4):` | Itera exatamente 3 vezes para coletar as 3 notas de cada aluno. |
| `while True:` (interno) | Garante que cada nota seja válida antes de avançar para a próxima. |
| `try/except ValueError` | Captura entradas inválidas (letras, símbolos) e orienta o usuário. |
| `break` (interno) | Sai do loop de validação quando a nota for válida. |
| `calcular_media(notas)` | Chama a função de cálculo e armazena o resultado em `media`. |
| `verificar_situacao(media)` | Chama a função de classificação e armazena o resultado em `situacao`. |
| `exibir_relatorio(...)` | Chama a função de exibição passando os 3 dados coletados. |

---

## 💻 Como Executar

### Pré-requisitos
- Python 3.x instalado ([python.org](https://www.python.org/))

### Passos
```bash
# Salve o código em um arquivo, por exemplo: sistema_notas.py
# Execute no terminal:
python sistema_notas.py
```

---

## 🖥️ Exemplo de Execução

```text
Digite aqui o nome do Aluno(Ou para encerrar 'Sair'): João
Digite aqui a nota 1 do aluno: 8.5
Digite aqui a nota 2 do aluno: abc
Erro! digite apenas números para as notas!
Digite aqui a nota 2 do aluno: 7.0
Digite aqui a nota 3 do aluno: 9.0

=== RELATÓRIO ===
Aluno: João
Média: 8.17
Situação: Aprovado
=================

Digite aqui o nome do Aluno(Ou para encerrar 'Sair'): Maria
Digite aqui a nota 1 do aluno: 6.0
Digite aqui a nota 2 do aluno: 5.5
Digite aqui a nota 3 do aluno: 6.5

=== RELATÓRIO ===
Aluno: Maria
Média: 6.00
Situação: Recuperação
=================

Digite aqui o nome do Aluno(Ou para encerrar 'Sair'): sair
Saindo do sistema... até mais...
```

---

## 📚 Conceitos Aprendidos

1. **Funções como Blocos Reutilizáveis:** Cada função encapsula uma lógica específica, facilitando leitura, teste e manutenção.
2. **Separação de Responsabilidades:** Uma função calcula, outra classifica, outra exibe — cada uma faz UMA coisa bem feita.
3. **Composição de Funções:** O resultado de uma função alimenta a próxima (`notas → media → situacao → relatório`).
4. **Validação Robusta com Loops Aninhados:** O loop interno garante qualidade dos dados antes de permitir avanço no fluxo principal.
5. **Parâmetros e Retorno:** Diferença entre funções que devolvem valores (`return`) e funções que apenas executam ações (`print`).

---

## 👨‍💻 Autor

**Victor** — Estudante de Programação Python

## 📜 Licença

Projeto desenvolvido para fins educacionais. Livre para estudo e adaptação.
