from tkinter import *

window = Tk()
window.title("지하철 경로 찾기")
window.geometry("750x600")
l = Label(window, text= "지하철 경로 찾기", font=500)
l1 = Label(window, text="출발역")
l2 = Label(window, text="도착역")
l.place(x=275, y=200)
l1.place(x=250,y=300)
l2.place(x=250,y=280)

e1 = Entry(window, width=30)  # 출발역 텍스트 입력창의 너비를 30으로 설정
e2 = Entry(window, width=30)  # 도착역 텍스트 입력창의 너비를 30으로 설정
e1.place(x=300,y=300)
e2.place(x=300,y=280)

b2 = Button(window, text="경로 찾기")
b2.place(x=350,y=330)

window.mainloop()