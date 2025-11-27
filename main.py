# # Search Algorithms
# # Linear Search
# my_list = [5, 14, 10, 22, 2, 29, 31, 4]
# search_num = 2
# found = False
# for i in my_list:
#     if i == search_num:
#         print(f"საძიებელი რიცხვი ნაპოვნია: {search_num}")
#         found = True
#         break
# if not found:
#     print("საძიებელი რიცხვი არ აღმოძნდა ლისტში")

# # Binary search
# def binary_search(sorted_list, target):
#     left = 0
#     right = len(sorted_list) - 1
#     if len(sorted_list) == 0:
#         print("რიცხვი ვერ მოიძებნა!")
#         return
#     mid = (left + right) // 2
#     if target == sorted_list[mid]:
#         print(f"რიცხვი ნაპოვნია და მისი ინდექსია {mid}")
#     elif target > sorted_list[mid]:
#         binary_search(sorted_list[mid+1:], target)
#     else:
#         binary_search(sorted_list[:mid], target)
# binary_search(sorted([5, 14, 10, 22, 2, 29, 31, 4, 7]),99)

#Linear time complexity
# def total(number):
#     summery = 0
#     for element in range(number):
#         summery += element
#     return summery
# print(total(100))

#constant time complexity
# def meanless_function(value):
#     total = 0
#     return value
# print(meanless_function(10))

#quadratic time complexity
# def weird_function(array_2D):
#     total = 0
#     for array in array_2D:
#         for element in array:
#             total += element
#     return total
# print(weird_function([[10,34],[100,345]]))

#single recursion
# def factorial(value):
#     if value == 0 or value == 1:
#         return 1
#     else:
#         return value * factorial(value - 1)
# print(factorial(5))

#multiple recursion
# cache = {}
#
# def fib_a(n):
#     if n in cache:
#         return cache[n]
#     if n <= 1:
#         return n
#     result = fib_a(n-1) + fib_a(n-2)
#     cache[n] = result
#     return result
#
# print(fib_a(10))
# print(cache)


# def fibonacci(value):
#     if value == 0:
#         return []
#     elif value == 1:
#         return [0]
#     elif value == 2:
#         return [0,1]
#     else:
#         index = 2
#         my_list = [0,1]
#         while index < (value):
#             my_list.append(my_list[index - 1] + my_list[index - 2])
#             index += 1
#         return my_list
# print(fibonacci(100))

# direct recursion
# def foo(value):
#     if value == 1:
#         return 1
#
#     return foo(value-1)
# print(foo(199))

#არაპირდაპირი რეკურსია
# def is_even(n):
#     if n == 0:
#         return True
#     else:
#         return is_odd(n-1)
#
# def is_odd(n):
#     if n == 0:
#         return True
#     else:
#         return is_even(n - 1)


#How fast is set?
# from timeit import timeit
#
# my_list = list(range(1_000_000))
# my_set = set(range(1_000_000))
#
# list_time = timeit('999_999 in my_list', number=1000, globals=globals())
# print(f"list time {list_time:.6} seconds")
#
# set_time = timeit('999_999 in my_set', number=1000, globals=globals())
# print(f"set time {set_time:.6f} seconds")
#
# print(list_time/set_time)

# x = {1,2,3}
# x.add(2)
# print(x)

# def foo(value):
#     if value == 1:
#         return 'base case'
#     else:
#         print('else')
#         return foo(value - 1)
#
# print(foo(2))

# def foo(value):
#     if value == 1:
#         return 1
#     else:
#         print('else')
#         return value + foo(value - 1)
#
# print(foo(2))

# def func_1(value):
#     if value == 0:
#         return True
#     else:
#         return func_2(value - 1)
# def func_2(value):
#     if value == 1 or value == 0:
#         return False
#     else:
#         return func_1(value - 1)
#
# print(func_1(1))

# def function(value):
#     if value == 0:
#         return False
#     else:
#         function(value - 1)
# function(2)

# x = 1
# print(hash(x))
# y = 'Hello'
# print(hash(y))
# dict და list და set არაა ჰეშირებადი

# my_set = {1,'Luka',()}
# print(my_set)

# a = {1,2,3}
# b = {4,5,6}
# print(a.union(b))
# print(a | b)
# print(a.intersection(b))
# print(a & b)
# print(a.difference(b))
# print(a - b)
# print(a.symmetric_difference(b))
# print(a ^ b)

# from queue import Queue
#
# q = Queue(maxsize=3)
#
# q.put(1)
# q.put(2)
# q.put(3)
# q.put(4, timeout=5)
#
# print(q.full())
#
# while not q.empty():
#     print(q.get())

# from queue import PriorityQueue
#
# q = PriorityQueue(maxsize=3)
#
# q.put((1, 5))
# q.put((100, 100))
# q.put((50, True))
#
# print(q.full())
#
# while not q.empty():
#     print(q.get())

# from queue import LifoQueue
#
# q = LifoQueue(maxsize=3)
#
# q.put(1)
# q.put(2)
# q.put(3)
#
# print(q.full())
#
# while not q.empty():
#     print(q.get())

# x = [1,2,3]
#
# val = x.pop()
# print(val)

# x = []
# x.append(1)
# x.append(2)
# x.append(3)
# print(x)

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def append(self,data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return
#         last_node = self.head
#         while last_node.next:
#             last_node = last_node.next
#         last_node.next = new_node
#
#     def prepend(self,data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node
#
#     def delete_node(self,key):
#         current_node = self.head
#         if current_node and current_node.data == key:
#             self.head = current_node.next
#             current_node = None
#             return
#         prev = None
#         while current_node and current_node.data != key:
#             prev = current_node
#             current_node = current_node.next
#         if current_node is None:
#             return
#         prev.next = current_node.next
#         current_node = None
#
#     def print_list(self):
#         current_node = self.head
#         while current_node:
#             print(current_node.data, end=' -> ')
#             current_node = current_node.next
#         print('None')
#
# # Example usage
# if __name__ == "__main__":
#     linked_list = LinkedList()
#     linked_list.append(1)
#     linked_list.append(2)
#     linked_list.append(3)
#     linked_list.append(4)
#     linked_list.prepend(0)
#     linked_list.print_list()
#     linked_list.delete_node(3)
#     linked_list.print_list()


# def dfs(graph,start):
#     visited = set()
#     stack = [start]
#
#     while stack:
#         vertex = stack.pop()
#
#         if vertex not in visited:
#             visited.add(vertex)
#             stack.extend(graph[vertex] - visited)
#
#     return visited
#
# graph = {
#     'A': {'B', 'C'},
#     'B': {'A', 'D', 'E'},
#     'C': {'A', 'F'},
#     'D': {'B'},
#     'E': {'B', 'F'},
#     'F': {'C', 'E'}
# }
#
# print(dfs(graph,'A'))

# from collections import deque
#
# def bfs(graph, start):
#     visited = set()
#     queue = deque([start])
#     visited.add(start)
#
#     while queue:
#         vertex = queue.popleft()
#         print(vertex, end=" ")
#
#         for neighbor in graph[vertex]:
#             if neighbor not in visited:
#                 visited.add(neighbor)
#                 queue.append(neighbor)
#
# graph = {
#     'A': {'B', 'C'},
#     'B': {'A', 'D', 'E'},
#     'C': {'A', 'F'},
#     'D': {'B', 'W'},
#     'E': {'B', 'F'},
#     'F': {'C', 'E', 'G'},
#     'G': {'F', 'W'},
#     'W': {'D', 'G'}
# }
#
# bfs(graph=graph, start='A')