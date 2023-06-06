list = [1,2,3,4,5,6,7,8,9,0]
reversed_list = []
for value in list:
  reversed_list = [value] + reversed_list
print(reversed_list)
