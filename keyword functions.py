def greet(name="user"):
    print("Hello",name)

greet()

greet("Tanushk")
def details(name,rollno):
    print(name,rollno)

details(rollno=123,name="Rohan")


details("Rohan",123)

details(123,"Rohan")

def sum(*numbers):
    sum=0

    for num in numbers:
        sum=sum+num 
    print(sum)

sum(1,2,3,4)

sum(15,17)

def details(**details):
    print(details)

details(name="Rohan",
        section="2J",
        Rollno=123)


