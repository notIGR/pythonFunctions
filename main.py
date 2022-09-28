# max_num()

def max_num(a,b,c):
  return max([a,b,c])

print(max_num(5,10,15))
print(max_num(100,69,3))
print(max_num(71,30,8))

# mult_list()
def mult_list(lst):
  if len(lst) == 0:
    return 0
  prod = lst[0]

  if len(lst) > 1:
    for i in lst[1:]:
      prod = prod * i

  return prod

print(mult_list([2,4,6]))
print(mult_list([]))
print(mult_list([11]))

#rev_string()
def rev_string(my_str):
  return my_str[::-1]

print(rev_string("Racecar"))
print(rev_string("Hannah"))
print(rev_string("Bob"))

#num_within()
def num_within(x,a,b):
  return x in range(a,b+1)
     
print(num_within(1,2,3))     
print(num_within(5,10,15))     
print(num_within(69,13,69))