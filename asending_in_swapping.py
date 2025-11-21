#arranged in asending order by the help of swapping
'''var1=[5,15,6,8,1,12,24]
print(var1)
print()
var1[0],var1[1],var1[2],var1[3],var1[4],var1[5],var1[6]=var1[4],var1[0],var1[2],var1[3],var1[5],var1[1],var1[6]
print(var1)'''

var2=[5,15,6,8,1,12,24]
print(var2)
print()
for i in var2:
	if var2[0]>var2[1]:
		var2[0],var2[1]=var2[1],var2[0]
	elif var2[1]>var2[2]:
		var2[1],var2[2]=var2[2],var2[1] 
	elif var2[2]>var2[3]:
		var2[2],var2[3]=var2[3],var2[2]
	elif var2[3]>var2[4]:
		var2[3],var2[4]=var2[4],var2[3]
	elif var2[4]>var2[5]:
		var2[4],var2[5]=var2[5],var2[4]
	elif var2[5]>var2[6]:
		var2[5],var2[6]=var2[6],var2[5]
print(var2)
	

