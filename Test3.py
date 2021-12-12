s = input()
max_length = 0
length= 0
l = 0 
for i in s:
    if i == '(':
        l +=1
    else:
        if l >0:
            l -= 1
            length += 2
        else:
            max_length = max(max_length, length)
            length = 0

print(max(max_length, length))
    