

import time

class Node:
    def __init__(self, data):
        self.data = data # Armazena o valor do nó
        self.next = None # Referência para o próximo nó (inicialmente None)

class LinkedList:
    def __init__(self):
        self.head = None # Inicializa a lista vazia

    def append(self, data):
        # Cria um novo nó com o dado fornecido
        new_node = Node(data)
        #  Se a lista está vazia, o novo nó se torna a cabeça (head)
        if not self.head:
            self.head = new_node
            return
        # Caso contrário, percorre a lista até o último nó
        last = self.head
        while last.next:
            last = last.next
        # Conecta o novo nó ao último nó encontrado
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
                negative.append(current.data)
            else:
                positive.append(current.data)
            current = current.next

        return negative, positive

    @staticmethod
    def merge(left, right):
        result = LinkedList()
        left_ptr = left.head
        right_ptr = right.head

        # Create dummy node to build the result
        dummy = Node(0)
        tail = dummy

        while left_ptr and right_ptr:
            if left_ptr.data <= right_ptr.data:
                tail.next = Node(left_ptr.data)
                left_ptr = left_ptr.next
            else:
                tail.next = Node(right_ptr.data)
                right_ptr = right_ptr.next
            tail = tail.next

        # Append remaining elements
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

        # Split the list into two halves
        left, right = LinkedList.split(list)

        # Recursively sort each half
        left_sorted = LinkedList.merge_sort(left)
        right_sorted = LinkedList.merge_sort(right)

        # Merge the sorted halves
        return LinkedList.merge(left_sorted, right_sorted)

    @staticmethod
    def split(list):
        slow = list.head
        fast = list.head.next

        # Fast moves twice as fast as slow
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Split the list at slow
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

        # First, invert the sign of negative numbers to make them positive
        current = list.head
        while current:
            current.data = -current.data
            current = current.next

        # Perform radix sort on the positive numbers
        max_num = LinkedList.get_max_value(list)
        exp = 1

        while max_num // exp > 0:
            LinkedList.counting_sort(list, exp)
            exp *= 10

        # Convert the numbers back to negative
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

        # Initialize count array
        count = [0] * 10
        output = LinkedList()

        # Store count of occurrences in count[]
        current = list.head
        while current:
            index = (current.data // exp) % 10
            count[index] += 1
            current = current.next

        # Change count[i] so it contains actual position of this digit in output[]
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Build the output linked list in reverse order
        # Since we can't easily traverse backward in a singly linked list,
        # we'll first extract all elements to an array
        elements = []
        current = list.head
        while current:
            elements.append(current.data)
            current = current.next

        output_elements = [0] * len(elements)

        for i in range(len(elements) - 1, -1, -1):
            index = (elements[i] // exp) % 10
            output_elements[count[index] - 1] = elements[i]
            count[index] -= 1

        # Rebuild the linked list with sorted elements
        list.head = None
        for num in output_elements:
            list.append(num)

    @staticmethod
    def concatenate(negative, positive):
        result = LinkedList()

        # Add negative elements first
        current = negative.head
        while current:
            result.append(current.data)
            current = current.next

        # Add positive elements
        current = positive.head
        while current:
            result.append(current.data)
            current = current.next

        return result


# Example input
input_data = [-7, 23, -1, 0, 3, -99, 45, 12]

# Create linked list from input
original_list = LinkedList()
for num in input_data:
    original_list.append(num)

print("Lista original:")
original_list.print_list()
print()

# Split into negative and positive lists
negative_list, positive_list = original_list.split_by_sign()

# Sort negative list with Radix Sort
print("Ordenando lista negativa com Radix Sort...")
start_time = time.time()
negative_sorted = LinkedList.radix_sort_negative(negative_list)
radix_time = (time.time() - start_time) * 1000  # convert to milliseconds

print("Lista negativa ordenada por Radix Sort:", end=" ")
negative_sorted.print_list()

# Sort positive list with Merge Sort
print("\nOrdenando lista positiva com Merge Sort...")
start_time = time.time()
positive_sorted = LinkedList.merge_sort(positive_list)
merge_time = (time.time() - start_time) * 1000  # convert to milliseconds

print("Lista positiva ordenada por Merge Sort:", end=" ")
positive_sorted.print_list()

# Concatenate the sorted lists
final_list = LinkedList.concatenate(negative_sorted, positive_sorted)

# Print results
print("\nLista final concatenada:", end=" ")
final_list.print_list()

print("\nComplexidade teórica:")
print("- Merge Sort: O(n log n)")
print("- Radix Sort: O(nk) (onde k é o número de dígitos)")

print("\nTempo de execução:")
print(f"- Radix Sort: {radix_time:.6f} ms")
print(f"- Merge Sort: {merge_time:.6f} ms")

