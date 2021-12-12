input_list =input().replace('[','').replace(']', '').replace(',', ' ')

int_list =list(map(int, input_list.split(' ')))

if all(i < 0 for i in int_list):
    print(max(int_list))
else:
    mx= int_list[0]
    a = 0
    for i in range(len(int_list)):
        a =max(0, a+int_list[i])
        mx = max(a, mx)

    print(mx)

