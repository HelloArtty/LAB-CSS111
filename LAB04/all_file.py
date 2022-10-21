########################################################

#1
def myreplace(str, old, new):
    new_string = str.split()
    count = 0
    for i in range(len(new_string)):
        if old in new_string[i]:
            old_check = new_string[i].find(old)
            new_string[i] = new_string[i][:old_check] + \
                new + new_string[i][old_check+len(old):]
            count += 1
    return ' '.join(new_string), count


str = input()
old = input()
new = input()
new_string, sum = (myreplace(str, old, new))
print(new_string)
print(sum)

########################################################

#2
def check_number(number):
    number = str(number)
    number = [int(i) for i in number]
    list_number = []
    for i in range(len(number)-1):    
        first_num = number[i]
        second_num = number[i+1]
        if first_num > second_num:
            list_number.append(True)
        else:
            list_number.append(False)
    for x in range(0, len(list_number)-1):
        if list_number[x] == list_number[x+1]:
            output = False 
        else:
            output = True
    return output


number = int(input())
print(check_number(number))

########################################################

#3
r = int(input(""))
n = int(input("")) 
q_r = [] 
q_n = ["period  "]
for i in range(1, r+1): q_n.append(f"{i}%     ")
print(*q_n)

for x in range(1, n+1):
    q_list = []
    q_list.append(f"{x}     ")
    for i in range(1, r+1):
        q_list.append('{:.3f}  '.format((1+i*0.01)**x))
    print(*q_list)

########################################################