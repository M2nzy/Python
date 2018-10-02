# gugudan.py
dan = input("구구단을 출력할 숫자를 입력하세요(2~9) >>> ")
dan = int(dan)
for i in range(1,10):
    print(dan*i, end=' ')