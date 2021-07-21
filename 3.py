text = input().split()
print(max(text, key=text.count))
print(max(text, key=len))
