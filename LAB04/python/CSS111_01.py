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
