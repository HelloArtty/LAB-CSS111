# def check_number(number):
#     number = str(number)
#     number = [int(i) for i in number]
#     list_number = []
#     for i in range(len(number)-1):    
#         first_num = number[i]
#         second_num = number[i+1]
#         if first_num > second_num:
#             list_number.append(True)
#         else:
#             list_number.append(False)
#     for x in range(0, len(list_number)-1):
#         if list_number[x] == list_number[x+1]:
#             output = False 
#         else:
#             output = True
#     return output


# number = int(input())
# print(check_number(number))









# # def func(int_number):
# #     number = str(int_number)
# #     number = [int(i) for i in number]
# #     for i in range(len(number)-1):
# #         if i < number[i+1]:
# #             if i % 2 == 0:
# #                 if number[i] >= number[i+1]: #เช็คตำแหน่งเลขคู่ว่ามากหรือเท่ากับข้างๆรึเปล่า ถ้ามากกว่าreturn false
# #                     return False
# #             else:
# #                 if number[i] <= number[i+1]: #เช็คตำแหน่งเลขคี่ว่าน้อยหรือเท่ากับข้างๆรึเปล่า ถ้าน้อยกว่า return false
# #                     return False
# #                 else:
# #                     return True

# # int_number = int(input()) 
# # print(func(int_number))

# def check_number(number):
#     number = str(number)
#     number = [int(i) for i in number]
#     list_number = []
#     for i in range(len(number)-1):    
#         first_num = number[i]
#         second_num = number[i+1]
#         print(first_num,second_num)
#         if first_num > second_num:
#             list_number.append(True)
#         else:
#             list_number.append(False)
#     print(list_number)

#     for x in range(0,len(list_number)-1):
#         if list_number[x] == list_number[x+1]:
#             output = False 
#             break
#         else:
#             output = True
#     return output


# number = int(input())
# print(check_number(number))
