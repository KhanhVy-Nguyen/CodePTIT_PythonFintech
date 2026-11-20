import re 
from collections import Counter
n = int(input())

text = ""
for _ in range(n):
    text += input() + " "

words = re.findall(r"\w+", text.lower())
counts = Counter(words)
sorted_words = sorted(counts.items(), key= lambda x : (-x[1], x[0]))
for word, freq in sorted_words:
    print(word, freq)