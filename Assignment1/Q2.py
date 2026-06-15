a = 10
b = 10

print(id(a)) #2285790888464
print(id(b)) #2285790888464



a = [10]
b = [10]

print(id(a)) #2285795749440
print(id(b)) #2285795702336

# int in first case is immutable & in python instead of creating separate obj python points both variables a,b to same memory address
#In second case List are mutable so even though both list contains same value they are stored in different memory address