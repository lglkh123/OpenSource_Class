x = int(input("x좌표를 입력하세요 = "))
y = int(input("y좌표를 입력하세요 = "))

if  (x>0)and(y>0) :
    print("제일사분면입니다.")
elif (x<0)and(y>0) :
    print("제이사분면입니다.")
elif (x<0)and(y<0) :
    print("제삼사분면입니다.")
else :
    print("제사사분면입니다.")
