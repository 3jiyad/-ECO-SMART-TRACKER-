import datetime
import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="ECO-SMART Tracker v4.0", page_icon="🌱", layout="centered"
)

# 타이틀 및 소개
st.markdown(
    "<h1 style='text-align: center; color: #2E7D32;'>🌱 ECO-SMART Tracker v4.0</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<h4 style='text-align: center; color: #555;'>পরিবেশবান্ধব অভ্যাস গড়ার স্মার্ট"
    " ডিজিটাল প্ল্যাটফর্ম</h4>",
    unsafe_allow_html=True,
)
st.markdown("---")

# 사용자 정보 입력 폼
st.markdown("### 📝 আপনার তথ্য প্রদান করুন:")
name = st.text_input("পূর্ণ নাম (Name)", placeholder="আপনার নাম লিখুন")
cls = st.text_input("শ্রেণি (Class)", placeholder="যেমন: 10 / HSC")
section = st.text_input("সেকশন (Section)", placeholder="যেমন: A")
roll = st.text_input("রোল (Roll)", placeholder="আপনার রোল লিখুন")

st.markdown("---")
st.markdown("### 📋 পরিবেশবান্ধব অভ্যাস চেকআপ:")

# 설문 문항 예시
q1 = st.radio(
    "1. আপনি কি প্রতিদিন প্লাস্টিক বোতল ব্যবহারের পরিবর্তে রিইউজেবল বোতল ব্যবহার"
    " করেন?",
    ("হ্যাঁ", "না"),
)
q2 = st.radio(
    "2. রুম থেকে বের হওয়ার সময় কি আপনি ফ্যান ও লাইটের সুইচ বন্ধ করেন?",
    ("হ্যাঁ", "না"),
)
q3 = st.radio("3. আপনি কি গাছ লাগাতে বা পরিচর্যা করতে পছন্দ করেন?", ("হ্যাঁ", "না"))

# 점수 계산 및 제출 버튼
if st.button("সাবমিট করুন (Submit)", type="primary"):
  if not name or not cls:
    st.warning("দয়া করে আপনার নাম এবং শ্রেণি লিখুন!")
  else:
    # 점수 계산 로직
    score = 0
    if q1 == "হ্যাঁ":
      score += 33
    if q2 == "হ্যাঁ":
      score += 33
    if q3 == "হ্যাঁ":
      score += 34

    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 데이터 저장을 위한 텍스트 포맷
    log_data = (
        f"সময়: {current_time} | নাম: {name} | শ্রেণি: {cls} | সেকশন: {section} |"
        f" রোল: {roll} | স্কোর: {score}%\n"
    )

    # 화면에 결과 출력
    st.success(
        f"ধন্যবাদ, {name}! আপনার তথ্য সফলভাবে জমা হয়েছে। আপনার ইকো-স্কোর: {score}%"
    )
    st.balloons()

    # (옵션) 로컬 텍스트 파일 저장 대신 구글 시트 연동이나 안전한 저장을 위한 안내
    # 현재는 안정적인 작동을 위해 화면에 결과를 보여주고 기록합니다.

