time=(input("enter the time"))
if time<"6:00am":
    print("get up in the morning")
elif time>="6:00am" and time<"7:00am":
    print("exercise")
elif time>="7:00am" and time<"8:00am":
    print("take bath")
elif time>="8:00am" and time<"9:00am":
    print("take breakfast")
elif time>="9:00am" and time<"10:00":
    print("english activity")
elif time>="10:00" and time<"1:00am":
    print("coding")
elif time>="1:00pm" and time<"3:00pm":
    print("lunch break")
elif time>="3:00pm" and time<"5:30pm":
    print("coding time")
elif time>="5:30pm" and time<"6:00pm":
    print("snacks break")
elif time>="6:00pm" and time<"7:00":
    print("cultural activity")
elif time>="7:00pm" and time<"8:00pm":
    print("break")
elif time>="8:00pm" and time<"9:00pm":
    print("dinner time")
elif time>="9:00pm" and time<"10:00pm":
    print("milk")
else:
    print("sleep")