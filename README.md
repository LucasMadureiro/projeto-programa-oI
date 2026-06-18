# 📦 Sistema de Gerenciamento de Estoque

---

## 👥 Integrantes do Grupo

- Lucas Madureiro Matias
- Mateus Alexandre Moreno Simplicio

---

## 📋 Descrição do Projeto

Este projeto é um **sistema de gerenciamento de estoque** desenvolvido em **Python**, com armazenamento de dados em arquivo **JSON**.

O programa roda diretamente no terminal e permite que o usuário cadastre produtos, registre vendas, remova itens e consulte o estoque em tempo real. Todas as alterações são salvas automaticamente em um arquivo local, garantindo que os dados não sejam perdidos ao fechar o programa.

O sistema também conta com **alertas visuais automáticos** para produtos com estoque baixo ou zerado, tornando o controle mais prático e eficiente.

---

## 🗂️ Estrutura do Projeto

```
📁 projeto-estoque/
├── projeto_de_estoque.py      # Arquivo principal do programa
└── arquivo do estoque.json    # Banco de dados local dos produtos

---

## ⚙️ Funcionalidades

| Opção | Funcionalidade |
|-------|----------------|
| **1** | Adicionar novo produto ou aumentar quantidade de produto existente |
| **2** | Remover um produto do estoque pelo ID |
| **3** | Reduzir a quantidade de um produto (registrar venda) |
| **4** | Consultar todos os produtos com total geral |
| **5** | Salvar e sair do programa |

### Alertas automáticos
- ⚠️ **ESTOQUE BAIXO** — quantidade igual ou menor que 3 unidades
- ❌ **ESTOQUE ZERADO** — quantidade igual a 0

---

## 🚀 Instruções de Execução (Passo a Passo)

### ✅ Passo 1 — Verifique se o Python está instalado

Abra o terminal (Prompt de Comando no Windows, Terminal no Linux/Mac) e digite:

```bash
python --version
```

Se aparecer algo como `Python 3.x.x`, está pronto. Caso contrário, baixe em: https://www.python.org/downloads/

---

### ✅ Passo 2 — Baixe os arquivos do projeto

Certifique-se de que os dois arquivos abaixo estão na **mesma pasta** no seu computador:

```
projeto_de_estoque.py
arquivo do estoque.json
```

---

### ✅ Passo 3 — Abra o terminal na pasta do projeto

- **Windows:** Abra a pasta, clique na barra de endereço, digite `cmd` e pressione Enter
- **Linux/Mac:** Clique com o botão direito na pasta e selecione "Abrir terminal aqui"

---

### ✅ Passo 4 — Execute o programa

Digite o comando abaixo e pressione **Enter**:

```bash
python projeto_de_estoque.py
```

---

### ✅ Passo 5 — Utilize o sistema

O programa exibirá a lista de produtos cadastrados e perguntará se deseja acessar o menu:

```
_____ PRODUTOS _____

ID: 1 | aviao --- 598 unidades
ID: 2 | agua  --- 567 unidades

Deseja acessar o Menu ?
Digite S (para Sim) ou N (para Não):
```

Digite **S** para abrir o menu e escolha uma das opções disponíveis (1 a 5).

---

## 📚 Bibliotecas Utilizadas

| Biblioteca | Tipo | Para que foi usada |
|------------|------|--------------------|
| `json` | Nativa do Python (não precisa instalar) | Leitura e escrita do arquivo de dados `.json` |

> 💡 Este projeto utiliza **apenas bibliotecas nativas** do Python. Não é necessário instalar nenhum pacote externo.

---

## 🤝 Divisão de Responsabilidades

O projeto foi desenvolvido de forma **colaborativa**, ambos integrantes participando em conjunto de todas as etapas:

| Etapa | Responsáveis |
|-------|-------------|
| Planejamento da lógica do sistema | Lucas e Mateus |
| Desenvolvimento do código Python | Lucas e Mateus |
| Criação e estruturação do arquivo JSON | Lucas e Mateus |
| Testes e validação do programa | Lucas e Mateus |
| Documentação (README) | Lucas e Mateus |

---

## 💾 Formato do Arquivo de Dados

Os produtos ficam armazenados em `arquivo do estoque.json`:

```json
{
  "1": { "produto": "aviao", "quantidade": 598 },
  "2": { "produto": "agua",  "quantidade": 567 }
}
```

Cada produto possui:
- **ID** — número de identificação único, gerado automaticamente
- **produto** — nome do item cadastrado
- **quantidade** — número de unidades disponíveis em estoque
