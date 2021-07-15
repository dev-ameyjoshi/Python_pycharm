from StringCalculator import Module1 as m1
from StringCalculator import Module2 as m2

X = m1.length(input("Enter :"))
print(f"Length of String = {X}")
print(m1.concatenation("amey", " Joshi"))
print(m1.upper_case("amey joshi"))
print(m1.reverse("ameyjoshi"))

d = input("Enter String for slicing : ")
a = int(input("start slicing : "))
b = int(input("end slicing : "))
c = int(input("step up of slicing "))
S = m1.slicing_string(a,b,c)
print(d[S])

print(m2.addition(3,8))
print(m2.multiplication(3,40))
print(m2.factorial(5))
print(m2.square(5))
print(m2.square_root(81))

