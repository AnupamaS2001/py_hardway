def add (a,b):
    print(f"Adding {a} + {b}")
    return a + b

def substract(a,b):
    print(f"Substracting {a} - {b}")
    return a-b

def multiply(a,b):
    print(f"Multiplying {a} *{b}")
    return a*b

def division(a,b):
    print(f"division {a} / {b}")
    return a / b

print(f"Let's do some math with just functions!")

age=add(30,5)
height=substract(78,4)
weight=multiply(90,2)
iq=division(100,2)

print(f"Age: {age}, height:{height}, weight:{weight},IQ:{iq}")
print(f"here is a puzzle")
what=add (age,substract(height,multiply(weight,division(iq,2))))
print("that becomes: ",what,"Can you do it by hand?")