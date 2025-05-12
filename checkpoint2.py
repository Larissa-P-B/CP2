# Nome: Larissa Pereira Biusse
# RM: 564068

import time # O comando import time em Python importa o módulo time, que fornece várias funções relacionadas ao tempo e à medição de tempo.

class Node:
    def __init__(self, data):
        self.data = data # Armazena o valor do nó
        self.next = None # Referência para o próximo nó (inicialmente None)
class LinkedList:
    def __init__(self):
        self.head = None # Inicializa a lista vazia

    def is_empty(self): # Método para verificar se a lista está vazia
        return self.head is None

    def insert_at_end(self, data):
        new_node = Node(data)  # Cria um novo nó com os dados fornecidos
        if self.is_empty():  # Verifica se a lista está vazia
            self.head = new_node  # Se vazia, o novo nó se torna o head
            return
        last = self.head  # Começa pelo head para percorrer a lista
        while last.next:  # Percorre até encontrar o último nó
            last = last.next
        last.next = new_node  # Faz o último nó apontar para o novo nó

    def print_list(self):
        current = self.head  # Começa pelo nó head (início da lista)
        elements = []  # Lista vazia para armazenar os elementos
        while current:  # Percorre enquanto houver nós
            elements.append(str(current.data))  # Converte o dado para string e adiciona à lista
            current = current.next  # Avança para o próximo nó
        print(f"[{', '.join(elements)}]")  # Imprime no formato desejado

    def split_by_sign(self):
        negative = LinkedList()  # Cria lista para negativos
        positive = LinkedList()  # Cria lista para positivos/zero
        current = self.head  # Começa pelo primeiro nó

        while current:  # Percorre toda a lista
            if current.data < 0:
                negative.insert_at_end(current.data)  # Insere no final da lista de negativos
            else:
                positive.insert_at_end(current.data)  # Insere no final da lista de positivos
            current = current.next  # Avança para o próximo nó

        return negative, positive  # Retorna as duas listas

    @staticmethod
    def merge(left, right):
        result = LinkedList()  # 1. Lista resultado
        dummy = Node(0)  # 2. Nó auxiliar
        tail = dummy  # 3. Ponteiro para o final
        left_ptr = left.head  # 4. Ponteiro para a lista esquerda
        right_ptr = right.head  # 5. Ponteiro para a lista direita

        # 6. Compara elementos das duas listas
        while left_ptr and right_ptr:
            if left_ptr.data <= right_ptr.data:
                tail.next = Node(left_ptr.data)
                left_ptr = left_ptr.next
            else:
                tail.next = Node(right_ptr.data)
                right_ptr = right_ptr.next
            tail = tail.next

        # 7. Adiciona elementos restantes da esquerda
        while left_ptr:
            tail.next = Node(left_ptr.data)
            left_ptr = left_ptr.next
            tail = tail.next

        # 8. Adiciona elementos restantes da direita
        while right_ptr:
            tail.next = Node(right_ptr.data)
            right_ptr = right_ptr.next
            tail = tail.next

        result.head = dummy.next  # 9. Define o head do resultado
        return result


    @staticmethod
    def merge_sort(list):
        if not list.head or not list.head.next: # Caso base: lista vazia ou com um único elemento
            return list

        left, right = LinkedList.split(list) # Divide a lista em duas metades
        left_sorted = LinkedList.merge_sort(left) # Ordena recursivamente cada metade
        right_sorted = LinkedList.merge_sort(right)# Ordena recursivamente cada metade
        return LinkedList.merge(left_sorted, right_sorted) # Combina as duas metades ordenadas

    @staticmethod
    def split(list):
        # 1. Inicialização dos ponteiros
        slow = list.head  # Ponteiro lento (avança 1 nó por vez)
        fast = list.head.next  # Ponteiro rápido (avança 2 nós por vez)

        # 2. Encontrando o meio da lista
        while fast and fast.next:
            slow = slow.next  # Avança um passo
            fast = fast.next.next  # Avança dois passos

        # 3. Criando as sublistas
        left = LinkedList()
        left.head = list.head  # Primeira metade começa no head original

        right = LinkedList()
        right.head = slow.next  # Segunda metade começa após o nó médio

        # 4. Separando as listas
        slow.next = None  # Divide a lista original em duas

        return left, right

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



# Exemplo de entrada
input_list = [-7, 23, -1, 0, 3, -99, 45, 12]

# Criar lista ligada
original_list = LinkedList()
for num in input_list:
    original_list.insert_at_end(num)

# Separar positivos e negativos
negative_list, positive_list = original_list.split_by_sign()

# Ordenar negativos com Radix Sort e medir tempo
start_time = time.time()
sorted_negative = LinkedList.radix_sort_negative(negative_list)
radix_time = (time.time() - start_time) * 1000  # ms

# Ordenar positivos com Merge Sort e medir tempo
start_time = time.time()
sorted_positive = LinkedList.merge_sort(positive_list)
merge_time = (time.time() - start_time) * 1000  # ms

# Concatenar resultados
final_list = LinkedList.concatenate(sorted_negative, sorted_positive)

# Exibir resultados
print("Lista negativa ordenada por Radix Sort:", end=" ")
sorted_negative.print_list()
print("Lista positiva ordenada por Merge Sort:", end=" ")
sorted_positive.print_list()
print("Lista final concatenada:", end=" ")
final_list.print_list()
print(f"Complexidade de Merge Sort: O(n log n)")
print(f"Complexidade de Radix Sort: O(nk) (onde k é o número de dígitos)")
print(f"Tempo de execução do Radix Sort: {radix_time:.6f} ms")
print(f"Tempo de execução do Merge Sort: {merge_time:.6f} ms")



