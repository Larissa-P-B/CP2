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
  - **print_list** é um método de uma lista encadeada (linked list) que imprime todos os elementos da lista no formato [dado1, dado2, dado3].
    - Inicialização: **current = self.head** - Começa pelo primeiro nó da lista (apontado por self.head).
    - Preparação para coleta de dados: **elements = []** - Cria uma lista Python vazia para armazenar os valores dos nós.
    - Percorrendo a lista: **while current:** - Enquanto o nó atual (current) não for None (ou seja, enquanto houver elementos na lista encadeada).
**elements.append(str(current.data))** - Converte o dado do nó atual para string e adiciona à lista elements.
**current = current.next** - Move para o próximo nó da lista encadeada.
    - Impressão formatada: **print(f"[{', '.join(elements)}]")** - Junta todos os elementos com vírgulas e espaços e imprime entre colchetes.
  - Complexidade:Tempo: O(n) - Precisa percorrer todos os n elementos da lista. 
Espaço: O(n) - Armazena uma cópia dos dados em uma lista Python (para a formatação de saída).

```python
    def print_list(self):
        current = self.head  # Começa pelo nó head (início da lista)
        elements = []  # Lista vazia para armazenar os elementos
        while current:  # Percorre enquanto houver nós
            elements.append(str(current.data))  # Converte o dado para string e adiciona à lista
            current = current.next  # Avança para o próximo nó
        print(f"[{', '.join(elements)}]")  # Imprime no formato desejado
    
```

___

- Função do Código:
  - Esta função **split_by_sign** divide uma lista encadeada em duas listas separadas:Uma para números negativos
Outra para números positivos (incluindo zero)
    - Inicialização:Cria duas novas listas vazias (negative e positive)
      - Percorrendo a lista original:Começa no nó cabeça (self.head)Percorre cada nó até chegar ao final (None)
      - Classificação dos elementos: Para cada nó, verifica se o dado é negativo .Insere o elemento no final da lista apropriada
      - Resultado: Retorna um par contendo as duas novas listas.
      
    - Complexidade: Tempo: O(n) - Percorre cada elemento uma vez. Espaço: O(n) - Cria duas novas listas contendo todos os elementos originais

```python
    def split_by_sign(self):
        negative = LinkedList()  # Cria lista para negativos
        positive = LinkedList()  # Cria lista para positivos/zero
        current = self.head      # Começa pelo primeiro nó
        
        while current:           # Percorre toda a lista
            if current.data < 0:
                negative.insert_at_end(current.data)  # Insere no final da lista de negativos
            else:
                positive.insert_at_end(current.data)  # Insere no final da lista de positivos
            current = current.next  # Avança para o próximo nó
        
        return negative, positive  # Retorna as duas listas  

```
___

- Função do Código:
  - Esta função estática **(@staticmethod)** realiza a operação clássica de merge (fusão) de duas listas encadeadas ordenadas, resultando em uma nova lista também ordenada. 
É a parte fundamental do algoritmo **Merge Sort** para listas encadeadas.
    - Inicialização: Cria uma lista vazia result para o resultado .Cria um nó **dummy** (artifício comum para simplificar a lógica).Inicializa ponteiros para percorrer as listas **left** e **right**
    - Fase de Comparação:Compara os elementos atuais de ambas as listas. Adiciona o menor elemento à lista resultante
Avança o ponteiro da lista que contribuiu com o elemento 
    - Fase de Esgotamento:Quando uma lista se esgota, adiciona todos os elementos restantes da outra lista
    - Finalização:Remove o nó dummy (que era apenas auxiliar).Retorna a lista fundida ordenada
      - Exemplo Prático Entrada: left: [1, 3, 5], right: [2, 4, 6]
      Execução:

        Compara 1 e 2 → adiciona 1

        Compara 3 e 2 → adiciona 2

        Compara 3 e 4 → adiciona 3

        Compara 5 e 4 → adiciona 4

        Compara 5 e 6 → adiciona 5

        Esgota left → adiciona 6 (restante de right)
      - Saída:[1, 2, 3, 4, 5, 6]
  - Características Importantes:**Estabilidade**: Mantém a ordem de elementos iguais (importante para sort estável).
**Não destrutiva**: Não modifica as listas originais (cria novos nós).
**Uso do dummy node**: Técnica comum para simplificar a lógica de inserção. **Eficiência**: Ótima para listas encadeadas (não tem o overhead de realocação de arrays).
Esta implementação é particularmente eficaz como parte de um algoritmo Merge Sort para listas encadeadas, onde a operação de merge é a etapa fundamental.
  - Complexidade:Tempo: O(n + m) - onde n e m são os tamanhos das listas. Espaço: O(n + m) - cria uma nova lista com todos os elementos

```python
        @staticmethod
    def merge(left, right):
        result = LinkedList()  # Lista resultado
        dummy = Node(0)        # Nó auxiliar
        tail = dummy           # Ponteiro para o final
        left_ptr = left.head   # Ponteiro para a lista esquerda
        right_ptr = right.head # Ponteiro para a lista direita
    
        # Compara elementos das duas listas
        while left_ptr and right_ptr:
            if left_ptr.data <= right_ptr.data:
                tail.next = Node(left_ptr.data)
                left_ptr = left_ptr.next
            else:
                tail.next = Node(right_ptr.data)
                right_ptr = right_ptr.next
            tail = tail.next
    
        # Adiciona elementos restantes da esquerda
        while left_ptr:
            tail.next = Node(left_ptr.data)
            left_ptr = left_ptr.next
            tail = tail.next
    
        # Adiciona elementos restantes da direita
        while right_ptr:
            tail.next = Node(right_ptr.data)
            right_ptr = right_ptr.next
            tail = tail.next
    
        result.head = dummy.next  # Define o head do resultado
        return result   

```
___

- Função do Código:
  - Esta função estática implementa o algoritmo **Merge Sort** para listas encadeadas, um método de ordenação eficiente que segue a abordagem "dividir para conquistar".
A função assume que existe uma função auxiliar **split** que divide a lista ao meio .A função merge já foi explicada anteriormente
Este é um algoritmo puramente recursivo que cria novas listas em cada chamada (não é in-place)
    - Caso Base (Condição de Parada): Se a lista está vazia (not list.head) ou contém apenas um elemento (not list.head.next).Retorna a lista como está, pois não há o que ordenar
    - Divisão da Lista: Divide a lista original em duas sublistas aproximadamente iguais .A função split (não mostrada aqui) provavelmente usa o algoritmo do "ponteiro rápido e lento" para encontrar o meio da lista
    - Ordenação Recursiva: Aplica o merge sort recursivamente em cada metade. Isso continua até que todas as sublistas tenham apenas 0 ou 1 elemento (caso base)
    - Combinação (Merge): Combina as duas metades já ordenadas usando a função merge .A função merge (explicada anteriormente) intercala os elementos em ordem
  - Complexidade:Tempo: O(n log n) em todos os casos ,log n níveis de recursão .Cada nível requer O(n) operações para merge.
Espaço: O(n) (devido à criação de novas listas)
  - Exemplo Prático :
      
    Considere ordenar a lista: [4, 2, 1, 3]
        
      Divide em [4, 2] e [1, 3]
        
      Ordena [4, 2]:
        
      Divide em [4] e [2] (caso base)
        
      Merge resulta em [2, 4]
        
      Ordena [1, 3]:
        
      Divide em [1] e [3] (caso base)
        
      Merge resulta em [1, 3]
        
      Merge final de [2, 4] e [1, 3]:
        
      Resultado: [1, 2, 3, 4]

```python
    @staticmethod
    def merge_sort(list):
        if not list.head or not list.head.next: # Caso base: lista vazia ou com um único elemento
            return list

        left, right = LinkedList.split(list) # Divide a lista em duas metades
        left_sorted = LinkedList.merge_sort(left) # Ordena recursivamente cada metade
        right_sorted = LinkedList.merge_sort(right)# Ordena recursivamente cada metade
        return LinkedList.merge(left_sorted, right_sorted) # Combina as duas metades ordenadas

```

