r = int(input("")) # ดอกเบี้ย %
n = int(input("")) # จำนวนปี
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