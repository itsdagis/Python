stud_info = ["Efrem", 26, "efrem@example.com", True, 1.72]
print(stud_info[0])
print(stud_info[1])
print(stud_info[2])
print(stud_info[3])
print(stud_info[4])

print(stud_info[-1])

for i in range(4):
    print(stud_info[i])

for x in stud_info:
    print(x)

#Change
stud_info[0] = "Dagi"

print(stud_info)

stud_info[3] = False

print(stud_info)

stud_info.append("Bole")
print(stud_info)

stud_info.remove("Bole")
print(stud_info)

stud_info.pop(4)
print(stud_info)

stud_infos = ("Efrem", 26, "efrem@example.com", True, 1.72)



stud_infos_set = ({"Efrem", 26, "efrem@example.com", True, 26, 1.72})
print(stud_infos_set)

stud_info_dic = {
    "Name": "Efrem",
    "Email": "efrem@example.com",
    "isActive": True,
    "Age": 26,
    "Height": 1.72
}

print(stud_info_dic["Name"])

print(stud_info_dic["Age"])

print(stud_info_dic.keys())
print(stud_info_dic.values())
print(stud_info_dic.items())

for i in stud_info_dic.keys():
    print(i)

for keys,values in stud_info_dic.items():
    print(keys,values)

