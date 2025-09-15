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