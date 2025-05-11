# Nome: Larissa Pereira Biusse
# RM: 564068

import time

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(f"[{', '.join(elements)}]")

    def split_by_sign(self):
        negative = LinkedList()
        positive = LinkedList()
        current = self.head
        while current:
            if current.data < 0:
                negative.insert_at_end(current.data)
            else:
                positive.insert_at_end(current.data)
            current = current.next
        return negative, positive

    @staticmethod
    def merge(left, right):
        result = LinkedList()
        dummy = Node(0)
        tail = dummy
        left_ptr = left.head
        right_ptr = right.head

        while left_ptr and right_ptr:
            if left_ptr.data <= right_ptr.data:
                tail.next = Node(left_ptr.data)
                left_ptr = left_ptr.next
            else:
                tail.next = Node(right_ptr.data)
                right_ptr = right_ptr.next
            tail = tail.next

        while left_ptr:
            tail.next = Node(left_ptr.data)
            left_ptr = left_ptr.next
            tail = tail.next

        while right_ptr:
            tail.next = Node(right_ptr.data)
            right_ptr = right_ptr.next
            tail = tail.next

        result.head = dummy.next
        return result

    @staticmethod
    def merge_sort(list):
        if not list.head or not list.head.next:
            return list

        left, right = LinkedList.split(list)
        left_sorted = LinkedList.merge_sort(left)
        right_sorted = LinkedList.merge_sort(right)
        return LinkedList.merge(left_sorted, right_sorted)

    @staticmethod
    def split(list):
        slow = list.head
        fast = list.head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        left = LinkedList()
        left.head = list.head
        right = LinkedList()
        right.head = slow.next
        slow.next = None
        return left, right

    @staticmethod
    def radix_sort_negative(list):
        if not list.head:
            return list

        # Convert to positive
        current = list.head
        while current:
            current.data = -current.data
            current = current.next

        # Perform radix sort
        max_num = LinkedList.get_max_value(list)
        exp = 1

        while max_num // exp > 0:
            LinkedList.counting_sort(list, exp)
            exp *= 10

        # Convert back to negative
        current = list.head
        while current:
            current.data = -current.data
            current = current.next

        return list

    @staticmethod
    def get_max_value(list):
        if not list.head:
            return 0

        max_val = list.head.data
        current = list.head.next

        while current:
            if current.data > max_val:
                max_val = current.data
            current = current.next

        return max_val

    @staticmethod
    def counting_sort(list, exp):
        if not list.head:
            return

        count = [0] * 10
        current = list.head

        while current:
            index = (current.data // exp) % 10
            count[index] += 1
            current = current.next

        for i in range(1, 10):
            count[i] += count[i - 1]

        # Extract elements to array
        elements = []
        current = list.head
        while current:
            elements.append(current.data)
            current = current.next

        # Build output array
        output = [0] * len(elements)
        for i in range(len(elements) - 1, -1, -1):
            index = (elements[i] // exp) % 10
            output[count[index] - 1] = elements[i]
            count[index] -= 1

        # Rebuild linked list
        list.head = None
        for num in output:
            list.insert_at_end(num)

    @staticmethod
    def concatenate(negative, positive):
        result = LinkedList()
        current = negative.head
        while current:
            result.insert_at_end(current.data)
            current = current.next
        current = positive.head
        while current:
            result.insert_at_end(current.data)
            current = current.next
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



