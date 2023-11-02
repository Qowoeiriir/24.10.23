# # №1
# def all_divisors(number):
#     divisors = []
#     for i in range(1, int(number ** 0.5) + 1):
#         if num % i == 0:
#             divisors.append(i)
#             if i != num // i:
#                 divisors.append(number // i)
#     divisors.sort()
#     return divisors
#
#
# number = [23436, 190187200, 380457890232]
# for number in numbers:
#     divisors = all_divisors(number)
#     print(f"Делители {number}: {divisors}")

# # №2
# def three_args(*, var1=None, var2=None, var3=None):
#     args = []
#     if var1 is not None:
#         args.append(f"var1 = {var1}")
#     if var2 is not None:
#         args.append(f"var2 = {var2}")
#     if var3 is not None:
#         args.append(f"var3 = {var3}")
#
#     if args:
#         print("Переданы аргументы:", ", ".join(args))
#     else:
#         print("Аргументы не были переданы.")

# # №4
# def get_most_common_and_longest_words(text):
#     word_counts = {}
#
#     most_common_word = ""
#     longest_word = ""
#
#     words = text.split()
#
#     for word in words:
#         if word in word_counts:
#             word_counts[word] += 1
#         else:
#             word_counts[word] = 1
#
#         if word_counts[word] > word_counts.get(most_common_word, 0):
#             most_common_word = word
#
#         if len(word) > len(longest_word):
#             longest_word = word
#
#     return most_common_word, longest_word
#
#
# text = input('Введите текст: ')
# result = get_most_common_and_longest_words(text)
# print('Наиболее часто встречающееся слово:', result[0])
# print('Самое длинное слово:', result[1])

# # №6
# def is_magic_square(matrix):
#     n = len(matrix)
#
#     expected_sum = sum(matrix[0])
#
#     for i in range(1, n):
#         if sum(matrix[i]) != expected_sum:
#             return False
#
#     for j in range(n):
#         if sum(matrix[i][j] for i in range(n)) != expected_sum:
#             return False
#
#     if sum(matrix[i][i] for i in range(n)) != expected_sum:
#         return False
#
#     if sum(matrix[i][n - i - 1] for i in range(n)) != expected_sum:
#         return False
#
#     return True
#
# matrix = [
#     [2, 7, 6],
#     [9, 5, 1],
#     [4, 3, 8]
# ]
#
# if is_magic_square(matrix):
#     print("Магический квадрат.")
# else:
#     print("Не магический квадрат.")

# # №3
# def is_palindrome(p):
#     p = p.replace(" ", "").lower()
#
#     return p == p[::-1]
#
# print(is_palindrome("Нажал кабан на баклажан"))


