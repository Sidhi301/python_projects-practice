# Find common elements between two lists using set.
# a = {1, 2, 3}
# b = {2, 3, 4}

# print(a & b)  # Output: {2, 3}

# Remove duplicate words from a sentence using set.
# sentence = "i am sidhi in sidhi world in a happy world"
# words = sentence.split()
# unique_words = list(set(words))
# print(unique_words)

# Check if two strings are anagrams using set and logic.
# str1 = "listen"
# str2 = "silent"

# if set(str1) == set(str2) and len(str1) == len(str2):
#     print("Anagrams")
# else:
#     print("Not Anagrams")


# Find elements present in first list but not in second using set.

# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7]

# diff = list(set(list1) - set(list2))
# print(diff)


# Check if all characters in a string are unique using set.
# string = "python"

# if len(set(string)) == len(string):
#     print("All unique")
# else:
#     print("some are duplicates")


# Count number of distinct elements in a list using set.

# lst = [1, 2, 2, 3, 4, 4, 4, 5]
# print(len(set(lst)))


# Find symmetric difference between two sets without built-in functions.

# Remove common characters from two strings using set.
# str1 = "abcdef"
# str2 = "bdfxyz"

# result = "".join([ch for ch in str1 if ch not in set(str2)])
# print(result)


# Check if one set is a subset of another without built-in functions.

# Find repeated elements in a list using set.

def sum(a,b):
   
    print(a+b+c)
sum(1,2)