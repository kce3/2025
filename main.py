import streamlit as st

# MBTI별 직업 추천 데이터
mbti_jobs = {
    "INTJ": ["전략 기획자", "데이터 분석가", "연구원"],
    "ENTP": ["기업가", "마케팅 기획자", "광고 크리에이터"],
    "ISFJ": ["교사", "간호사", "상담가"],
    "ESFP": ["배우", "아나운서", "이벤트 기획자"],
    # 필요에 따라 나머지 MBTI도 채우기!
}

st.set_page_config(page_title="MBTI 직업 추천", page_icon="✨")

st.title("MBTI 기반 진로 추천 서비스")
st.write("당신의 MBTI를 선택하면 적절한 직업을 추천해 드립니다!")

# MBTI 선택
mbti = st.selectbox(
    "당신의 MBTI를 선택하세요:",
    options=list(mbti_jobs.keys())
)

# 추천 결과
if mbti:
    st.subheader(f"🌟 {mbti} 유형 추천 직업")
    for job in mbti_jobs[mbti]:
        st.write(f"- {job}")
