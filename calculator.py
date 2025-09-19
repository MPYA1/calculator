

from sqrtmath import num_root
def cal_num(a:int|float,b:int|float)->int|float:
    if not isinstance(a,(int,float)) or not isinstance(b,(float,int)):
        raise TypeError("num must be  int or float")
    print("1-> ADD,2-> <->,3->MUL,4->div,5->pow,sqrt->6")
    choice=int(input("please enter your number:"))
    if choice == 1:
        return a+b
    elif choice==2:
        return a-b
    elif choice==3:
        return a*b
    elif choice==4:
        if b==0:
            raise ValueError("Your number is 0")
        return a/b
    elif choice==5:
        return a**b
    elif choice==6:
        return num_root(a,b)
    else:
        raise ValueError("We expect number between 1 to 6")
print(cal_num(-8,b=2))
