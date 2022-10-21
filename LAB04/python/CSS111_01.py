def my_replace(str, old, new):
    new_string = str.split() #แยกข้อความเป็น list
    count = 0 #สร้างตัวแปรรับค่าจำนวนที่ดูว่ามีกี่ตัวที่เปลี่ยน
    for i in range(len(new_string)): #loop เก็บค่าจำนวนคำ
        if old in new_string[i]: #เช็ค old ในแต่ระตำแหน่งของ new_string
            old_check = new_string[i].find(old) #หาคำที่ input เข้ามาจากตัวแปร old ใน new_string แล้วเก็บไว้ในตัวแปร old_check
            new_string[i] = new_string[i][:old_check] + new + new_string[i][old_check+len(old):] #นำค่าต่างๆมาเรียงข้อความ
            count += 1 #บวกจำนวนคำที่เจอ
    return' '.join(new_string),count #รีเทิร์นค่า

str = input() #รับค่าข้อความ
old = input() #รับค่าตัวที่จะเปลี่ยน
new = input() #รับค่าตัวที่จะให้เปลี่ยนเป็น
new_string, sum = (my_replace(str, old, new)) 
print(new_string)
print(sum)




























# def my_replace(str, old, new):
#     str_list = str.split()
#     #count = 0
#     for i in range(str_list):
#         if old in str[i]:
#             old_check= str[i].find(old)
#             #print(old_check)
#             str[i] = str[i][:old_check] + new + str[i][old_check+len(old)]
#             #count += 1
#         return
#     print(str_list)
#         #return count

# str = input(":")
# old = input(":")
# new = input(":")

# my_replace(str, old, new)
# #print(sum)


# def my_replace(str, old, new):
#     new_string = str.split()
#     for i in range(len(new_string)):
#         if old in new_string[i]:
#             for j in range(0,len(new_string[i])-len(old)+1):
#                 if old == new_string[i][j:j+len(old)]:
#                     new_string[i] = new_string[i][:j] + new + new_string[i][j+len(old):]
#     return ' '.join(new_string),str.count(old)

# str = input(":")
# old = input(":")
# new = input(":")
# new_string, sum = my_replace(str, old, new)
# print(new_string)
# print(sum)

