import streamlit as st

# 사이드바 설정
st.sidebar.title("학생 관리 시스템")
menu = ["학생 관리", "출석 체크", "과제 관리", "성적 분석", "보충 자료", "학부모 커뮤니케이션"]
choice = st.sidebar.radio("메뉴 선택", menu)

# 메인 페이지 내용
if choice == "학생 관리":
    st.header("학생 관리")
    st.write("학생 정보를 추가하고 관리하는 페이지입니다.")
    
elif choice == "출석 체크":
    st.header("출석 체크")
    st.write("학생들의 출석을 체크하는 페이지입니다.")
    
elif choice == "과제 관리":
    st.header("과제 관리")
    st.write("과제를 관리하고 채점하는 페이지입니다.")
    
elif choice == "성적 분석":
    st.header("성적 분석")
    st.write("학생 성적을 분석하고 결과를 시각화하는 페이지입니다.")
    
elif choice == "보충 자료":
    st.header("보충 자료")
    st.write("학생들에게 보충 자료를 제공하는 페이지입니다.")
    
elif choice == "학부모 커뮤니케이션":
    st.header("학부모 커뮤니케이션")
    st.write("학부모와의 소통을 위한 페이지입니다.")
