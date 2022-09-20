#Q1 hw
sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]
sample_set.update(sample_list)
print (sample_set)

#Q2
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.intersection(set2))

#Q3
tuple1 = (10, 20, 30, 40, 50)
tuple1 = tuple1[::-1]
print(tuple1)

#Q4
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
itm_2 = tuple1[1]
print (itm_2[1])

#Q5
tuple1 = (10, 20, 30, 40)
a,b,c,d, = tuple1
print(a)
print(b)
print(c)
print(d)
