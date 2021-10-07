  a= int (input("enter a number"))
#   int num1,num2;
#  print("emter two numbers:");
#  scanf("%d%d",&num1, &num2);

num1=int(input("take a number"))
num2=int(input("take a number"))
if(num1>num2):
  print("%d is maximum",num1)
    if(num2>num1):
      print("%d is maximum",num2)
      if(num2>num1):
        print("%d is maximum",num2)
        if(num1==num2):
          print("both are equal")
        else:
          print("1")
      else:
        print("2")
    else:
      print("3")
else:
  print("4")