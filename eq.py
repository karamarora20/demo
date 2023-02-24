from Equation import Expression
import regex as re
w=input(f'enter the constraint for edge: ')

w=re.sub('\W|\d','',w)
l=[]
for i in w:
    if i.isalpha():
        l.append(i)
w= list(set(l))
print(w)
fn = Expression("sin(x+y^2)",["y","x"])
print(fn(4,3))
