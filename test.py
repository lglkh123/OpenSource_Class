x = int(input("x좌표를 입력하세요 = "))
y = int(input("y좌표를 입력하세요 = "))

if  (x>0)and(y>0) :
    print("제1사분면입니다.")
elif (x<0)and(y>0) :
    print("제2사분면입니다.")
elif (x<0)and(y<0) :
    print("제3사분면입니다.")
else :
    print("제4사분면입니다.")
