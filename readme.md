# CP 2: Organizador de Dados em Lista Ligada

## Enunciado

**Você foi contratado para implementar um sistema de organização de
grandes volumes de dados representados como números inteiros.
Esses dados são armazenados em uma lista ligada (não em arrays) e
precisam ser ordenados de acordo com dois critérios:**
___ 
**1. Critério 1 (Primário): Se os números forem positivos, use Merge Sort.**

**2. Critério 2 (Secundário): Se os números forem negativos, use Radix Sort adaptado para negativos (considere que o Radix padrão só lida com números positivos, 
então será necessário adaptar ou inverter os sinais temporariamente).**
___
### Além disso, ao final da ordenação, o sistema deve:
- Imprimir a lista ligada ordenada completa (com positivos e
negativos juntos, mantendo os negativos antes dos positivos);
- Exibir a complexidade teórica de tempo de cada algoritmo usado;
- Medir e exibir o tempo real de execução de cada algoritmo
separadamente.


___

# 📝	Explicando o código

### Classe Node (Nó)
- Função do Código:
     - **self.data = data**,Armazena o valor (dado) que o nó contém.
Pode ser qualquer tipo de dado (inteiro, string, objeto, etc.).
     - **self.next = None**
Inicializa o ponteiro/referência para o próximo nó da lista ligada.
Por padrão, um novo nó é criado sem conexão (None significa "não aponta para nada").
Quando inserimos um novo nó na lista, next é ajustado para apontar para o próximo elemento.

```python
class Node:
    def __init__(self, data):
        self.data = data # Armazena o valor do nó
        self.next = None # Referência para o próximo nó (inicialmente None)
```
- Função do Código:
  - **def __init__(self):** É o construtor da classe, chamado automaticamente quando um objeto LinkedList é criado.

  - **self.head = None** Inicializa o atributo head (cabeça da lista) como None, indicando que a lista está vazia no momento da criação.
head será o primeiro nó da lista. Se head é None, a lista não tem elementos.

  - **def is_empty(self):** Método para verificar se a lista está vazia
        

```python
class LinkedList:
    def __init__(self):
        self.head = None # Inicializa a lista vazia
        
    def is_empty(self):  # Método para verificar se a lista está vazia
        return self.head is None
```
___
- Função do Código:
  - Esta função **insert_at_start** é um método típico de uma lista encadeada (linked list) 
que insere um novo nó no início da lista.Esta operação tem complexidade O(1) (tempo constante)
, pois envolve um número fixo de operações independentemente do tamanho da lista.
```python
    def insert_at_start(self, data):
        new_node = Node(data) # Cria um novo nó com os dados fornecidos
        new_node.next = self.head # Faz o novo nó apontar para o atual primeiro nó
        self.head = new_node # Faz o head da lista apontar para o novo nó
```

```python
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
```