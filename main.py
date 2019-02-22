from linked_list import Set

set1 = Set([1,2,2,4,3])
print(set1)

set1 = Set([1, 4, 5, 8])
set2 = Set([2, 8, 6, 5])
print(set1.union(set2))
print(set1.intersection(set2))
set1 = Set([3, 2, 1])
set2 = Set([2, 3, 4])
print(set1.subset(set2))

set1 = Set(['Gulnaz', 'Akerke', 'Korkem'])
set1.add('Meruert')
print(set1)
set1.remove('Korkem')
print(set1)
print(len(set1))
for d in set1:
   print(d)
   break
