name=input("enter the name")
marks=int(input("enter the number"))
grade=input("enter the grade")
if name == "anjali":
    print("correct name")
    if marks>=350:
        print("good marks")
    if grade=="A,B":
        print("congratulations")
    else:
        print("bad grade")
else:
    print("your marks very poor")
print("Thank you")