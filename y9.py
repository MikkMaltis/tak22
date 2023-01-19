x = int(input("x:"))
y = int(input("y:"))
z = int(input("z:"))

if x == y == z:
    print("Võrdkülgne kolmnurk")

elif x == y or y == z or z == x:
    print("Võrdhaarne kolmnurk")

else: 
    print("Erikülgne kolmnurk")

else:
    print("Ei eksisteeri")