def reverse():
    
    print("This is puzzle favored by Einstein.You will be asked to enter\n a three digit number,where the hundred's digit differs from the \n one's digit by at least two.The procedure will always yield 1089")
    num=int(input("Give me a number:"))
    if len(str(num))==3:
        rev_num=str(num)[::-1]
        print(f"For the number: {int(num)} the reverse number is: {int(rev_num)}")
        rev_rev_num=str(rev_num)[::-1]
        dif=abs(int(rev_rev_num)-int(rev_num))
        print(f"The difference between {int(rev_rev_num)} and {int(rev_num)} is {dif} ")
        rev_dif=str(dif)[::-1]
        print(f"The reverse differnce is:{rev_dif}")
        total=int(rev_dif)+int(dif)
        print(f"The sum of:{dif} and revDiff is:{total}")

reverse()    