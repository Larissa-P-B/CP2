- Nome: Larissa Pereira Biusse 
- RM: 564068 

# CP 2: Organizador de Dados em Lista Ligada

## 📖 Enunciado

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

# 📚 Explicando o código

### Import Time
- Explicação  do Código:
    - O comando import time em Python importa o módulo time, que fornece várias funções relacionadas ao tempo e à medição de tempo. 
```python
import time 
```
___

### Classe Node (Nó)
- Explicação  do Código:
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
___
### Class LinkedList
- Explicação  do Código:
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
### Função insert_at_end:
- Explicação  do Código:
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

### Função print_list:
- Explicação  do Código:
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
### Função split_by_sign:

- Explicação  do Código:
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
### Função @staticmethod Merge:
- Explicação  do Código:
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

### Função @staticmethod Merge_Sort:

- Explicação  do Código:
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
___

### Função Split:
- Explicação  do Código:
    - Esta função estática divide uma lista encadeada em duas sublistas aproximadamente iguais, usando a técnica conhecida como "algoritmo do ponteiro rápido e lento" (tortoise and hare algorithm).
Características Importantes:**Precisão**:Para listas com número par de elementos, divide exatamente ao meio
Para número ímpar, left terá um elemento a mais **Eficiência**:Mais eficiente que contar elementos e depois dividir
Requer apenas uma passagem pela lista. **Uso Típico**:Fundamental para algoritmos como Merge Sort em listas encadeadas Também útil para detectar ciclos em listas
Esta implementação é particularmente elegante porque:Não precisa saber o tamanho da lista antecipadamente 
Não modifica a estrutura original além do ponto de divisão .Mantém a ordem original dos elementos em ambas as sublistas

    - Exemplo Prático:

    Para a lista: A → B → C → D → E → None
    
    Ponteiros iniciam:
    
    slow em A
    
    fast em B
    
    Primeira iteração:
    
    slow vai para B
    
    fast vai para D
    
    Segunda iteração:
    
    slow vai para C (meio)
    
    fast tenta ir para None.next (termina o loop)
    
    Divisão:
    
    left: A → B → C → None
    
    right: D → E → None
  - Complexidade: Tempo: O(n) - Percorre a lista apenas uma vez .Espaço: O(1) - Usa espaço constante (apenas alguns ponteiros)
```python
    @staticmethod
    def split(list):
        #  Inicialização dos ponteiros
        slow = list.head        # Ponteiro lento (avança 1 nó por vez)
        fast = list.head.next   # Ponteiro rápido (avança 2 nós por vez)
    
        # Encontrando o meio da lista
        while fast and fast.next:
            slow = slow.next      # Avança um passo
            fast = fast.next.next # Avança dois passos
    
        # Criando as sublistas
        left = LinkedList()
        left.head = list.head    # Primeira metade começa no head original
        
        right = LinkedList()
        right.head = slow.next   # Segunda metade começa após o nó médio
        
        #  Separando as listas
        slow.next = None         # Divide a lista original em duas
        
        return left, right
```

___

### Função @staticmethod Radix_Sort_Negative:
- Explicação  do Código:
  - Esta função estática implementa o **Radix Sort** (ordenamento por raiz) otimizado para listas encadeadas contendo valores negativos. 
É uma variação inteligente do **Radix Sort** tradicional que lida com números negativos através de uma conversão temporária.
Observações Importantes:**Dependências:** Requer a implementação de **get_max_value()**.Requer um **counting_sort()** estável.
**Restrições:** Funciona apenas para números inteiros .Assume que todos os valores são negativos (ou precisaria de adaptação para misturar positivos e negativos).
**Eficácia:** Ideal para ordenar números negativos com muitos dígitos .Performance linear relativa ao tamanho da lista.
Esta implementação demonstra como adaptar algoritmos de ordenação tradicionais para lidar com casos especiais (valores negativos) de maneira eficiente.

    - Verificação Inicial :Verifica se a lista está vazia (not list.head).Se estiver vazia, retorna imediatamente (não há o que ordenar)
    - Conversão para Positivos: Percorre toda a lista convertendo cada valor negativo para positivo
Exemplo: [-5, -3, -9] → [5, 3, 9]
    - Radix Sort Tradicional:Encontra o valor máximo na lista convertida (get_max_value)
Ordena os números dígito a dígito, do menos significativo para o mais significativo
Usa um Counting Sort estável para cada dígito (counting_sort)
    - Conversão de Volta para Negativos : Após a ordenação, converte todos os valores de volta para negativos
Exemplo: [3, 5, 9] → [-3, -5, -9]
  
  - Complexidade :Tempo: O(d·n).Onde d é o número de dígitos do maior número
Cada **Counting Sort** tem complexidade O(n).Espaço: O(n) (para o Counting Sort)


```python
    @staticmethod
    def radix_sort_negative(list):
        # Verificação de lista vazia
        if not list.head:
            return list
        
        # Conversão para valores positivos
        current = list.head
        while current:
            current.data = -current.data  # Inverte o sinal
            current = current.next
        
        # Radix Sort tradicional
        max_num = LinkedList.get_max_value(list)
        exp = 1
        
        while max_num // exp > 0:
            LinkedList.counting_sort(list, exp)  # Ordena por dígito
            exp *= 10  # Passa para o próximo dígito
        
        # Conversão de volta para negativos
        current = list.head
        while current:
            current.data = -current.data  # Restaura o sinal
            current = current.next
        
        return list
```

___

### Função @staticmethod Get_Max_Value:

- Explicação  do Código:
  - Esta função estática (@staticmethod) tem como objetivo encontrar o maior valor armazenado em uma lista encadeada. 
Aplicação Típica:Esta função é particularmente útil:Como auxiliar para algoritmos de ordenação (como visto no Radix Sort)
Para encontrar extremos em conjuntos de dados .Em operações estatísticas básicas
Observações. Alternativas:Poderíamos manter um ponteiro para o nó máximo em vez de apenas o valor
Poderíamos retornar tanto o valor máximo quanto sua posição. Extensibilidade:Fácil de adaptar para encontrar o valor mínimo (mudando a comparação para <)
Esta implementação é eficiente e direta, seguindo o padrão clássico para encontrar extremos em estruturas encadeadas.

    - Verificação de lista vazia:
Se a lista não tem elementos (list.head é None), retorna 0 como valor padrão
    - Inicialização:Assume que o primeiro elemento (list.head.data) é o máximo inicial
    - Percorrimento da lista:Começa a percorrer a lista a partir do segundo nó (list.head.next)
Usa um ponteiro current para navegar pela lista
    - Comparação:Para cada nó, compara seu valor com o max_val atual .Se encontrar um valor maior, atualiza max_val
    - Resultado:Retorna o maior valor encontrado após percorrer toda a lista.

  - Complexidade:Tempo: O(n) - Precisa percorrer todos os n elementos da lista uma vez
Espaço: O(1) - Usa apenas espaço constante (variáveis max_val e current)
```python
    @staticmethod
    def get_max_value(list):
        # Verifica se a lista está vazia
        if not list.head:
            return 0

        # Inicializa o valor máximo com o primeiro elemento
        max_val = list.head.data

        # Percorre a lista a partir do segundo nó
        current = list.head.next

        # Compara cada elemento com o máximo atual
        while current:
            if current.data > max_val:
                max_val = current.data
            current = current.next

        # Retorna o valor máximo encontrado
        return max_val
    

```
___

### Função @staticmethod Counting_Sort:
- Explicação  do Código:
    - Esta função estática implementa o Counting Sort (ordenamento por contagem) adaptado para trabalhar com listas encadeadas, sendo especialmente usada como parte do algoritmo Radix Sort.
Características Importantes:Estabilidade: Mantém ordem de elementos com mesmo dígito. Uso no Radix Sort: Ordena por um dígito específico
Adaptação: Converte lista encadeada para array temporário
Esta implementação é crucial para o Radix Sort, permitindo ordenação eficiente de números dígito a dígito.
        - Fase de Contagem:Conta quantas vezes cada dígito (0-9) aparece na posição atual (unidade, dezena, etc.)
        - Soma Cumulativa:Transforma a contagem em posições finais no array ordenado
        - Reordenação:Percorre a lista original de trás para frente (para manter estabilidade)
Coloca cada elemento na posição correta no array de saída.
        - Reconstrução:Reconstrói a lista encadeada com os elementos já ordenados pelo dígito atual

    - Complexidade:Tempo: O(n + k) onde k é o intervalo de valores (10 para dígitos).
Espaço: O(n) para os arrays auxiliares


```python
    @staticmethod
    def counting_sort(list, exp):
        # Verifica lista vazia
        if not list.head:
            return

        # Contagem de dígitos
        count = [0] * 10  # Array para contar dígitos 0-9
        current = list.head
        while current:
            index = (current.data // exp) % 10  # Pega o dígito atual
            count[index] += 1  # Incrementa contador
            current = current.next

        #  Soma cumulativa
        for i in range(1, 10):
            count[i] += count[i - 1]  # Calcula posições finais

        #  Extrai elementos para array
        elements = []
        current = list.head
        while current:
            elements.append(current.data)
            current = current.next

        # Constrói array ordenado
        output = [0] * len(elements)
        for i in range(len(elements) - 1, -1, -1):  # Ordem reversa para estabilidade
            index = (elements[i] // exp) % 10
            output[count[index] - 1] = elements[i]
            count[index] -= 1

        # Reconstrói a lista encadeada
        list.head = None  # Limpa a lista
        for num in output:
            list.insert_at_end(num)  # Insere elementos ordenados
```
___

### Função @staticmethod Concatenate:

- Explicação  do Código:
    - Esta função estática (@staticmethod) realiza a concatenação de duas listas encadeadas (uma com números negativos e outra com positivos) em uma única lista resultante.
Características Importantes:Não-destrutiva:Não modifica as listas originais (negative e positive permanecem intactas)Cria uma nova lista com os elementos copiados
Ordem preservada:Mantém a ordem original dos elementos dentro de cada lista .Coloca todos os negativos antes dos positivos
Versatilidade:Pode concatenar quaisquer duas listas, não apenas de negativos/positivos
Útil para implementação de algoritmos como o Radix Sort para números com sinais
Eficiência:Ótima para listas encadeadas (operações no final são O(n)).Se a classe LinkedList mantivesse um ponteiro para o último nó, seria O(1) por inserção
Casos Especiais .Lista negativa vazia:Retorna cópia da lista positiva
Lista positiva vazia:Retorna cópia da lista negativa Ambas vazias:Retorna lista vazia
Esta função é particularmente útil em algoritmos de ordenação que precisam separar e depois recombinar elementos negativos e positivos, como em versões adaptadas do Radix Sort para números inteiros com sinais.

        - Inicialização:Cria uma nova lista encadeada vazia (result) que armazenará o resultado final.
        - Adição dos elementos negativos:Percorre a lista negative do início ao fim Insere cada elemento no final da lista result usando insert_at_end.
        - Adição dos elementos positivos:Percorre a lista positive do início ao fim.Insere cada elemento no final da lista result após os negativos.
        - Resultado:Retorna a nova lista contendo todos os elementos na ordem: negativos seguidos de positivos.
    - Complexidade: Tempo: O(n + m).Onde n = tamanho da lista negativa E m = tamanho da lista positiva
Percorre cada lista uma vez Espaço: O(n + m).Cria uma nova lista com todos os elementos

```python
    @staticmethod
    def concatenate(negative, positive):
        # 1. Cria uma nova lista vazia para o resultado
        result = LinkedList()
        
        # 2. Percorre e adiciona todos os elementos da lista negativa
        current = negative.head
        while current:
            result.insert_at_end(current.data)
            current = current.next
        
        # 3. Percorre e adiciona todos os elementos da lista positiva
        current = positive.head
        while current:
            result.insert_at_end(current.data)
            current = current.next
        
        # 4. Retorna a lista concatenada
        return result
```

___ 

## 💻 Chamada do Código: 

```python
# Exemplo de entrada
input_list = [-7, 23, -1, 0, 3, -99, 45, 12] # Define uma lista de exemplo contendo números inteiros positivos, negativos e zero.

# Criar lista ligada
original_list = LinkedList()# Cria uma lista encadeada vazia chamada original_list
for num in input_list:
    original_list.insert_at_end(num)# Percorre cada número na input_list e insere no final da lista encadeada usando insert_at_end

# Separar positivos e negativos .Chama o método split_by_sign() que divide a lista original em duas:
negative_list, positive_list = original_list.split_by_sign()

# Ordenar negativos com Radix Sort e medir tempo
start_time = time.time() # Inicia um cronômetro com time.time()
sorted_negative = LinkedList.radix_sort_negative(negative_list) # Ordena a lista de negativos usando Radix Sort adaptado para números negativos
radix_time = (time.time() - start_time) * 1000  # ms Para o cronômetro e calcula o tempo de execução em milissegundos

# Ordenar positivos com Merge Sort e medir tempo
start_time = time.time() # Inicia outro cronômetro
sorted_positive = LinkedList.merge_sort(positive_list) # Ordena a lista de positivos usando Merge Sort
merge_time = (time.time() - start_time) * 1000  # ms Para o cronômetro e calcula o tempo de execução em milissegundos

# Concatenar resultados
final_list = LinkedList.concatenate(sorted_negative, sorted_positive) # Combina as duas listas ordenadas (negativos primeiro, depois positivos) em uma única lista encadeada

# Exibir resultados
print(f"Entrada: {input_list}\n")
print(f"Radix Sort: ")
print("Lista negativa ordenada por Radix Sort:", end=" ")
sorted_negative.print_list() # Imprime a lista de números negativos já ordenada pelo Radix Sort
print(f"\nMerge Sort: ")
print("Lista positiva ordenada por Merge Sort:", end=" ")
sorted_positive.print_list() # Imprime a lista de números positivos já ordenada pelo Merge Sort
print(f"\nLista Final Concatenada: ")
print("Lista final concatenada:", end=" ")
final_list.print_list() # Imprime a lista final combinada (negativos ordenados + positivos ordenados)
print(f"\nComplexidade : \n")
print(f"Complexidade de Merge Sort: O(n log n)\n")
print(f"Complexidade de Radix Sort: O(nk) (onde k é o número de dígitos)\n") # Exibe a complexidade algorítmica de cada método de ordenação

# Mostra os tempos de execução medidos para cada algoritmo, com 6 casas decimais
print(f"Tempo de Execução: \n")
print(f"Tempo de execução do Radix Sort: {radix_time:.6f} ms")
print(f"Tempo de execução do Merge Sort: {merge_time:.6f} ms")
```
___

## 📝 Exemplo de Saida do Código: 

```pycon
Entrada: [-7, 23, -1, 0, 3, -99, 45, 12]

Radix Sort: 
Lista negativa ordenada por Radix Sort: [-1, -7, -99]

Merge Sort: 
Lista positiva ordenada por Merge Sort: [0, 3, 12, 23, 45]

Lista Final Concatenada: 
Lista final concatenada: [-1, -7, -99, 0, 3, 12, 23, 45]

Complexidade : 

Complexidade de Merge Sort: O(n log n)

Complexidade de Radix Sort: O(nk) (onde k é o número de dígitos)

Tempo de Execução: 

Tempo de execução do Radix Sort: 0.000000 ms
Tempo de execução do Merge Sort: 0.000000 ms

Process finished with exit code 0
```

