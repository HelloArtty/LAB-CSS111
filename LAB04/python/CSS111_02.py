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
