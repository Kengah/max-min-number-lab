def findMaxMin(my_list):
  ary = []
  if (min(my_list)) == (max(my_list)):
    ary.append(len(my_list))
    return ary
    
  else:
    ary.append(min(my_list))
    ary.append(max(my_list))
    return ary