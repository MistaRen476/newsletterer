import random

out = ""
words = open("names.txt").read().split("\n")

for i in range(1000):
  out += random.choice(words)

print(out)