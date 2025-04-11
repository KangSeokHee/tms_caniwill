import streamlit as st
import pandas as pd
from fpdf import FPDF

# 데이터 파일 경로 설정 (CSV 파일)
STUDENT_DB_FILE = "student_db.csv"
GRADE_DB_FILE = "grade_db.csv"
ASSIGNMENT_DB_FILE = "assignment_db.csv"
ATTENDANCE_DB_FILE = "attendance_db.csv"
ATTENDANCE_CODE_FILE = "attendance_codes.csv"  # 출결 코드 관리 파일

# 기본 관리자 계정 설정
ADMIN_EMAIL = "admin@example.com"
ADMIN_PASSWORD = "admin123"

# 데이터 파일 불러오기
def load_data():
    if not pd.io.common.file_exists(STUDENT_DB_FILE):
        student_df = pd.DataFrame(columns=["학생명", "전화번호", "이메일", "학부모 연락처", "학교명", "학년", "기존성적"])
        student_df.to_csv(STUDENT_DB_FILE, index=False)
    else:
        student_df = pd.read_csv(STUDENT_DB_FILE)
    
    if not pd.io.common.file_exists(GRADE_DB_FILE):
        grade_df = pd.DataFrame(columns=["이름", "시험명", "점수"])
        grade_df.to_csv(GRADE_DB_FILE, index=False)
    else:
        grade_df = pd.read_csv(GRADE_DB_FILE)
    
    if not pd.io.common.file_exists(ASSIGNMENT_DB_FILE):
        assignment_df = pd.DataFrame(columns=["과제명", "과제 내용", "학생 이름", "제출 여부", "피드백", "제출 일자", "과제 상태"])
        assignment_df.to_csv(ASSIGNMENT_DB_FILE, index=False)
    else:
        assignment_df = pd.read_csv(ASSIGNMENT_DB_FILE)
    
    if not pd.io.common.file_exists(ATTENDANCE_DB_FILE):
        attendance_df = pd.DataFrame(columns=["이름", "출석 여부", "날짜"])
        attendance_df.to_csv(ATTENDANCE_DB_FILE, index=False)
    else:
        attendance_df = pd.read_csv(ATTENDANCE_DB_FILE)
    
    if not pd.io.common.file_exists(ATTENDANCE_CODE_FILE):
        attendance_codes_df = pd.DataFrame(columns=["출결 코드", "생성 시간", "유효 시간"])
        attendance_codes_df.to_csv(ATTENDANCE_CODE_FILE, index=False)
    else:
        attendance_codes_df = pd.read_csv(ATTENDANCE_CODE_FILE)
    
    return student_df, grade_df, assignment_df, attendance_df, attendance_codes_df

# 학생 관리 섹터 1 - 학생 정보 표
def student_management_info(student_df, grade_df, assignment_df, attendance_df):
    st.title("학생 관리")
    
    # 학생 관리 표
    student_summary = pd.merge(student_df, grade_df, left_on="학생명", right_on="이름", how="left")
    student_summary = pd.merge(student_summary, assignment_df[['학생 이름', '과제명', '제출 여부']], left_on="학생명", right_on="학생 이름", how="left")
    student_summary = pd.merge(student_summary, attendance_df[['이름', '출석 여부']], left_on="학생명", right_on="이름", how="left")
    
    st.markdown("<div style='background-color:#333333; padding:10px; color:white;'>학생 관리</div>", unsafe_allow_html=True)
    st.dataframe(student_summary)

# 출석 체크 섹터 2
def attendance_check(attendance_df, student_df):
    st.title("출석 체크")
    
    # 출석 체크
    student_name = st.selectbox("출석 체크를 할 학생을 선택하세요", student_df["학생명"])
    student_attendance = attendance_df[attendance_df['이름'] == student_name]
    
    st.write(f"{student_name}의 출석 체크")
    st.dataframe(student_attendance)

# 과제 관리 섹터 3
def assignment_management(assignment_df, student_df):
    st.title("과제 관리")
    
    # 과제 현황
    student_name = st.selectbox("과제 현황을 볼 학생을 선택하세요", student_df["학생명"])
    student_assignments = assignment_df[assignment_df['학생 이름'] == student_name]
    
    st.markdown("<div style='background-color:#333333; padding:10px; color:white;'>과제 현황</div>", unsafe_allow_html=True)
    st.dataframe(student_assignments)

# 과제 분석 섹터 4
def assignment_analysis(assignment_df, student_df):
    st.title("과제 분석")
    
    # 과제 분석
    student_name = st.selectbox("과제 분석을 할 학생을 선택하세요", student_df["학생명"])
    student_assignments = assignment_df[assignment_df['학생 이름'] == student_name]
    
    # 과제 제출 여부 분석
    assignment_status = student_assignments['제출 여부'].value_counts()
    st.bar_chart(assignment_status)

# 보충 영상 자료 섹터 5
def supplementary_video(assignment_df, student_df):
    st.title("보충 영상 자료")
    # 보충 영상 자료를 추가하는 섹터
    st.write("보충 영상 자료를 이곳에 추가할 수 있습니다.")

# 손필기 자료 섹터 6
def handwritten_material(student_df):
    st.title("손필기 자료")
    # 손필기 자료를 추가하는 섹터
    st.write("손필기 자료를 이곳에 추가할 수 있습니다.")

# 성적 분석 섹터 7
def grade_analysis(grade_df):
    st.title("성적 분석")
    
    # 성적 분석
    grade_summary = grade_df.groupby('시험명')['점수'].describe()
    st.dataframe(grade_summary)

# 학부모 커뮤니케이션 섹터 8
def parent_communication(student_df):
    st.title("학부모 커뮤니케이션")
    # 학부모와의 커뮤니케이션을 위한 섹터
    st.write("학부모 커뮤니케이션 관련 자료를 이곳에 추가할 수 있습니다.")

# 메인 페이지
def main():
    student_df, grade_df, assignment_df, attendance_df, attendance_codes_df = load_data()
    
    # 사이드바 메뉴 선택
    menu = [
        "학생 관리", "출석 체크", "과제 관리", "과제 분석", 
        "보충 영상 자료", "손필기 자료", "성적 분석", "학부모 커뮤니케이션"
    ]
    choice = st.sidebar.radio("메뉴", menu)
    
    # 각 메뉴에 해당하는 내용 표시
    if choice == "학생 관리":
        student_management_info(student_df, grade_df, assignment_df, attendance_df)
    elif choice == "출석 체크":
        attendance_check(attendance_df, student_df)
    elif choice == "과제 관리":
        assignment_management(assignment_df, student_df)
    elif choice == "과제 분석":
        assignment_analysis(assignment_df, student_df)
    elif choice == "보충 영상 자료":
        supplementary_video(assignment_df, student_df)
    elif choice == "손필기 자료":
        handwritten_material(student_df)
    elif choice == "성적 분석":
        grade_analysis(grade_df)
    elif choice == "학부모 커뮤니케이션":
        parent_communication(student_df)

if __name__ == "__main__":
    main()
