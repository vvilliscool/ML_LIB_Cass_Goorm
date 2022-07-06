# 08_tk_dict01A.py 에서 파일 읽어와서 단어의 뜻을 확인하기
# import tkinter_12
from tkinter import *
import pandas as pd
import os

global dat

print(os.getcwd())
path = 'C:\\pythonStudy\\Class_goorm\\folder_20220706'
os.chdir(path)
print(os.getcwd())

dat = pd.read_excel("./dic_excel.xlsx")
print(dat.shape, dat)

# 메인 :
window = Tk()
window.title("My Dictionary")

# 01 입력 상자 설명 레이블 
label = Label(window, text="원하는 단어 입력 후, 엔터 키 누르기")
label.grid(row=0, column=0, sticky=W)

# 02 텍스트 입력이 가능한 상자(Entry)
entry = Entry(window, width=15, bg="light green")
entry.grid(row=1, column=0, sticky=W)

# 03 제출 버튼 추가
btn = Button(window, text="제출", width=5, command=click)
btn.grid(row=2, column=0, sticky=W)

# 04 설명 레이블
lable2 = Label(window, text="\n의미:")
lable2.grid(row=3, column=0, sticky=W)

# 05 텍스트 박스 입력 상자
# columnspan=2 는 (4,0)~(4,1) 위치까지 분포
output = Text(window, width=50, height=6, wrap=WORD, background="light green")
output.grid(row=4, column=0, columnspan=2, sticky=W)

# 메인 반복문 실행
window.mainloop()