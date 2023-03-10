from remain_square import reaminder_func   #from 파이선파일이름 import 함수이름
from remain_square import square_func

##함수
def mul_func(n1, n2):
    return n1 * n2

def div_func(n1, n2):
    return n1 / n2

##전역
num1, num2, res = 100, 200, 0


##메인 코드실행부
res = mul_func(num1, num2)
print(f"곱하기 결과 : {res}")

res = div_func(num1, num2)
print(f"나누기 결과 : {res}")

res = remainder_func(num1, num2)
print(f"나머지 결과 : {res}")

res = square_func(num1, num2)
print(f"제곱 결과 : {res}")
