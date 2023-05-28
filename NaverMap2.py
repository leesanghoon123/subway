from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO

def open_naver_map():
    # 네이버 맵 API 요청 URL 생성
    url = "https://naveropenapi.apigw.ntruss.com/map-static/v2/raster?w=800&h=600&center=127.105834,37.359031&level=13&X-NCP-APIGW-API-KEY-ID=kfavfen9ll"

    try:
        # API 요청 보내기
        response = requests.get(url)
        response.raise_for_status()  # 요청이 실패하면 예외 발생

        # 이미지 데이터 가져오기
        image_data = response.content

        # 이미지 열기
        image = Image.open(BytesIO(image_data))

        # 이미지 리사이즈
        image = image.resize((800, 600))

        # 이미지를 tkinter에서 표시하기 위한 PhotoImage 객체 생성
        photo = ImageTk.PhotoImage(image)

        # 이미지를 표시할 Label 생성
        map_label = Label(window, image=photo)
        map_label.image = photo  # PhotoImage 객체에 대한 참조를 유지해야 함
        map_label.pack()

    except requests.exceptions.HTTPError as e:
        print(f"API 요청이 실패했습니다: {e}")
    except requests.exceptions.RequestException as e:
        print(f"요청 중 오류가 발생했습니다: {e}")

window = Tk()

# 지도 표시 버튼
button = Button(window, text="지도 열기", command=open_naver_map)
button.pack()

window.mainloop()
