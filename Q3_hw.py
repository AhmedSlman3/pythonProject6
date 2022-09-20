#Q1_dict
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
d_c = zip (keys,values)
n_dc = dict(d_c)
print (n_dc)

#Q2_dict
sample_dict = { "name": "Kelly","age": 25,"salary": 8000,"city": "New york"}

dele_c =  ["name", "salary"]
for ch in dele_c:
    del sample_dict [ch]
print (sample_dict )

