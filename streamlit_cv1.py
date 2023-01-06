# Streamlit Image-Comparison Component Example

import streamlit as st
from streamlit_image_comparison import image_comparison
from PIL import Image
import base64

# set page config
st.set_page_config(page_title="Image-Comparison Example", layout="centered")

st.header("Computer Vision 기능 개선(안)")

st.write("")
st.markdown("#### (개요) 댐방류 전 댐하류 보행자 판별 시행 > 경고 방송 등 대피 안내")
" - 하천 CCTV 원거리 포커싱으로 보행자 검출 어려움 (20~40m 최적조건)"
" - 도림천 DT 적용 Yolo 알고리즘의 한계 : 작은 물체 검출률 낮다 "
image = Image.open('image/distance.PNG')
st.image(image, caption='거리')
st.write("")

st.markdown("#### (목표) Computer Vision 기능 강화 (SAHI 알고리즘)")
"SAHI (Slicing Aided Hyper Interface) 분할된 영역 대상으로 개별 판별 과정 후 전체 결과로 도출"
" - 작은 슬라이스로 나누면 분석 이미지의 작은 객체의 픽셀 영역이 상대적으로 확대"
" - 기존 방식 대비 6.8% ~ 14.5% 효율 증가"
" - 매개변수 : Slice_size (256, 512), overlap_ratio (0.00 ~ 1.00), etc"
image = Image.open('image/ex1.PNG')
st.image(image, caption='이론')

st.write("")
"A lightweight vision library for performing large scale object detection & instance segmentation"

#file_ = open('image/sahi.gif', "rb")
#contents = file_.read()
#data_url = base64.b64encode(contents).decode("utf-8")
#file_.close()

#st.markdown(
#    f'<img src="data:image/gif;base64,{data_url}" alt="sample gif">',
#    unsafe_allow_html=True,
#)
st.markdown("![Alt Text](https://raw.githubusercontent.com/obss/sahi/main/resources/sliced_inference.gif)")

st.write("")
st.markdown("### 낙동강 홍수통제소 CCTV : 대구시(강창교)")
image1 = Image.open('image/local.PNG')
st.image(image1, caption='위치')

st.write("")
st.markdown("### CV Algorithm Comparison")
image_comparison(
    img1='image/2-1.png',
    img2='image/2-2.png',
    label1="Yolov7",
    label2="SAHI + Yolov5",
    width=1080,
)
