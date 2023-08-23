s1 = {1,2,5,6}
s2 = {3,6,7}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1,s2)
s1.update(s2)
print(s1)
print(s1.symmetric_difference(s2)) ##(s1 union s2) - (s1 intersection s2)
