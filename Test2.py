#Test Case 2
def anagrams(a, b):
    return sorted(a) == sorted(b)
print(anagrams("listen", "silent"))
print(anagrams("hello", "world"))