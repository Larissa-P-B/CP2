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
        
___
```python
class LinkedList:
    def __init__(self):
        self.head = None # Inicializa a lista vazia
        
    def is_empty(self):  # Método para verificar se a lista está vazia
        return self.head is None
```
___
- Função do Código:
  - **insert_at_end** é um método de uma lista encadeada (linked list) que insere um novo nó no *final* da lista.
    - Criação do novo nó:**new_node = Node(data)** - Cria um novo nó contendo o valor data.
    - Verificação se a lista está vazia:**if self.is_empty():** - Se a lista não tem elementos (self.head é None), o novo nó se torna o head.
    - Caso a lista não esteja vazia:**last = self.head** - Começa pelo primeiro nó (head).
**while last.next:** - Percorre a lista até encontrar o último nó (aquele cujo next é None).
**last.next = new_node** - Faz o último nó apontar para o novo nó, que agora é o novo final da lista.
    - Complexidade:Tempo: O(n) (linear), pois no pior caso precisamos percorrer toda a lista para encontrar o último nó. 
Espaço: O(1) (constante), pois só criamos um novo nó e usamos um ponteiro auxiliar (last).

```python
    def insert_at_end(self, data):
        new_node = Node(data)      # Cria um novo nó com os dados fornecidos
        if self.is_empty():        # Verifica se a lista está vazia
            self.head = new_node   # Se vazia, o novo nó se torna o head
            return
        last = self.head           # Começa pelo head para percorrer a lista
        while last.next:           # Percorre até encontrar o último nó
            last = last.next
        last.next = new_node       # Faz o último nó apontar para o novo nó
```

___

- Função do Código:
  - **print_list** é um método de uma lista encadeada (linked list) que imprime todos os elementos da lista no formato [dado1, dado2, dado3]
```python
    def print_list(self):
        current = self.head  # Começa pelo nó head (início da lista)
        elements = []  # Lista vazia para armazenar os elementos
        while current:  # Percorre enquanto houver nós
            elements.append(str(current.data))  # Converte o dado para string e adiciona à lista
            current = current.next  # Avança para o próximo nó
        print(f"[{', '.join(elements)}]")  # Imprime no formato desejado
    
```



```python
    def split_by_sign(self):
        negative = LinkedList()  # 1. Cria lista para negativos
        positive = LinkedList()  # 2. Cria lista para positivos/zero
        current = self.head      # 3. Começa pelo primeiro nó
        
        while current:           # 4. Percorre toda a lista
            if current.data < 0:
                negative.insert_at_end(current.data)  # 5. Insere no final da lista de negativos
            else:
                positive.insert_at_end(current.data)  # 6. Insere no final da lista de positivos
            current = current.next  # 7. Avança para o próximo nó
        
        return negative, positive  # 8. Retorna as duas listas  

```