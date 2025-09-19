from sqrtmath import num_root
def cal_num(a,b:float)->float:
    if not isinstance(a, float) or not isinstance(b, float):
        raise TypeError("num must be  int")
    print("1-> ADD,2-> <-> , 3->MUL,4->div,5->pow,sqrt->6")
    choice=int(input("please enter your number:"))
    if choice==1:
        return a+b
    elif choice==2:
        return a-b
    elif choice==3:
        return a*b
    elif choice==4:
        return a/b
    elif choice==5:
        return a**b
    elif choice==6:
        return num_root(a,b)


print(cal_num(8,3))
