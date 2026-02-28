msgcod = input()
result = " "
i = 0
n = len(msgcod)

while i < n:
    if msgcod[i] == "p" and i + 1 < n and msgcod[i+1] != " ":
        result += msgcod[i+1]
        i+=2
    else:
        result += msgcod[i]
        i +=1

print(result) 