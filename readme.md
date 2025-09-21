# Membros do grupo:
- Ana Laura - RM 554375
- Gerônimo Augusto - RM 557170
- Ianny raquel - RM 559096
- Murilo Cordeiro - RM 556727
- Vitor Augusto - RM 555469

# Controle de Consumo de Insumos em Unidades de Diagnóstico

Este projeto simula o **registro e análise do consumo diário de insumos** (reagentes, descartáveis, etc.) em unidades de diagnóstico.  
O objetivo é aplicar **estruturas de dados clássicas** (fila, pilha, buscas, ordenações) para organizar as informações de forma eficiente.

---

## 📌 Funcionalidades

### 1. Fila (Queue) – Registro de Consumo
- Implementada para armazenar os consumos em **ordem cronológica**.  
- Cada entrada contém o `material` e o `horário` do consumo.
- Operações principais:
  - `adicionar_consumo(material, horario, fila)` → adiciona ao final da fila.
  - `ler_consumos(fila)` → remove e exibe os consumos na ordem de entrada (FIFO).

✅ Exemplo: registrar o uso de gaze às 2h, seringa às 6h, agulha às 12h.

---

### 2. Pilha (Stack) – Consultas em Ordem Inversa
- Simula consultas onde os **últimos registros são acessados primeiro**.  
- Útil para revisar os últimos exames realizados.  
- Operações principais:
  - `adicionar_consulta(consulta, consumo, pilha)` → adiciona uma consulta.
  - `ler_consultas(pilha)` → remove e exibe em ordem inversa (LIFO).

✅ Exemplo: último exame cadastrado é exibido primeiro.

---

### 3. Estruturas de Busca
- **Busca Linear** (`busca_linear`): percorre toda a lista até encontrar o insumo desejado.  
- **Busca Binária** (`busca_binaria`): procura de forma mais eficiente, **mas exige a lista previamente ordenada**.

✅ Exemplo: encontrar a posição da `"gaze"` em uma lista de insumos.

---

### 4. Ordenação
- **Merge Sort** (`merge_sort`) → algoritmo estável, divide a lista e depois intercala.  
- **Quick Sort** (`quick_sort`) → mais rápido em muitos casos, mas instável.  
- Ambos permitem ordenar insumos por **quantidade consumida** ou por **validade**.

✅ Exemplo: organizar insumos por quantidade em estoque.

---

## 📊 Testes Implementados
A função `testar()` demonstra todos os módulos:
1. Registro de consumos em fila.  
2. Registro de consultas em pilha.  
3. Buscas linear e binária em uma lista de insumos.  
4. Ordenação dos insumos por quantidade com Merge Sort e Quick Sort.  

### Saída ilustrativa (resumida):
Teste da fila:  
- gaze (2:00)  
- seringa (6:00)  
- agulha (12:00)  

Teste da pilha (último primeiro):  
- Exame de urina → potinho  
- Ultrassom → gel  
- Exame de sangue → seringa  

---

## 🚀 Como Executar
1. Clone este repositório:
   git clone https://github.com/Vitorr-AF/sprint-3-dynamic-programming 

2. Entre na pasta do projeto:
   cd sprint-3-dynamic-programming  

3. Execute o script:
   python main.py  

---

## 📖 Estruturas e Algoritmos no Contexto do Problema
- **Fila** → mantém o histórico de consumo em ordem cronológica (controle diário).  
- **Pilha** → permite consultar rapidamente os últimos consumos realizados.  
- **Busca Linear** → útil para listas pequenas e não ordenadas.  
- **Busca Binária** → útil para grandes listas de insumos já ordenados.  
- **Merge Sort e Quick Sort** → auxiliam na organização por critérios como validade ou quantidade, fundamentais para prever reposição e evitar desperdício.