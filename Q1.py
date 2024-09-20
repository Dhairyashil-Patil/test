marks=int(input("ENTER YOUR MARKS:"))
if marks < 0:
    print("INVALID MARKS EXCEPTION:MARKS MUST BE FORM OF 0 TO 100")
    
if marks > 100:
    print("INVALID MARKS EXCEPTION:MARKS MUST BE FORM OF 0 TO 100")
else:
    print("YOU GOT",marks,"MARKS!")
