list= [1,5,100,33,22,56,35,67]
sorted_list = []
while len(list) >0:
    max_num = max(list)
    #sorted_list.append(max_num)
    sorted_list.insert(0,max_num)
    list.remove(max_num)
print(sorted_list)