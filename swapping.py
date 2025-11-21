rajvi=[10,19,28,36,45,82]
rajvi[1],rajvi[4]=rajvi[4],rajvi[1]
print(rajvi[1],rajvi[4])


Aadrash={"name":"aman","age":"27"}
bhoome={"name":"harsh","age":"38"}
Aadrash["name"],bhoome["name"]=bhoome["name"] ,Aadrash["name"]
print(Aadrash["name"],bhoome["name"])

L1=[5,15,13,17,9]
print(L1)
print()
replace_value_1st=int(input("enter index which 1st replace value\nthere has only 0-4 index\nenter walid index:"))
print()
replace_value_2nd=int(input("enter index which 2nd replace value\nthere has only 0-4 index\nenter walid index:"))
L1[replace_value_1st],L1[replace_value_2nd]=L1[replace_value_2nd],L1[replace_value_1st]
print(L1[replace_value_1st],L1[replace_value_2nd])
print()
print(L1)

