list=[2,3,4,5,3,4,6,2,6,7,8]
for i in range (len(list)):
	  for k in range(len(list)):
if i == k:
	continue
			elif list[i] == list[k]:
				del list[k]
				 list.append("0")
				
				print(list)