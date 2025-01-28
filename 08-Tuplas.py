"""
las tuplas son inmutables 
se declara con ()
"""

tupla=("uno","dos","tres")

print(tupla)

tuplasVariosDAtos=(12,True,23.5,"el gato", 12+4j)

print(tuplasVariosDAtos)


tuplasConTutplas=(1,2,3,4,(1,2,3))

print(tuplasConTutplas)

print(tuplasVariosDAtos[3])
print(tuplasVariosDAtos[-2])
print(tuplasVariosDAtos[0:2])

a,b,c=tupla

print(a,b,c)

