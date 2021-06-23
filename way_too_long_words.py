n = int(input())

for i in range(n):
    word = input()
    if len(word) < 11:
        print(word)
    else:
        print(f"{word[0]}{len(word)-2}{word[len(word)-1]}")