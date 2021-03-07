import sys

text = sys.stdin.readline().rstrip()
croatia_text = ["c=", "c-", "d-", "lj", "nj", "s=", "z="]
redundant = "dz="
result = 0

for c in croatia_text:
    result += text.count(c)

redundant_counnt = text.count(redundant)

print(len(text) - result - redundant_counnt)
