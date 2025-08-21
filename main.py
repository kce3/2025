import streamlit as st

# -----------------------------
# MBTI별 직업 추천 데이터
# -----------------------------
mbti_jobs = {
    "INTJ": ["🧠 전략 기획자", "📊 데이터 분석가", "🔬 연구원"],
    "ENTP": ["🚀 기업가", "🎯 마케팅 기획자", "🎨 광고 크리에이터"],
    "ISFJ": ["🍎 교사", "💉 간호사", "💬 상담가"],
    "ESFP": ["🎤 배우", "📺 아나운서", "🎉 이벤트 기획자"],
    "INFJ": ["📖 작가", "🧘 상담심리사", "🎶 예술가"],
    "ENFP": ["🌍 여행가", "🎬 영화감독", "🎭 크리에이터"],
    "ISTJ": ["📚 회계사", "⚖️ 변호사", "🏦 은행원"],
    "ESTJ": ["👔 관리자", "🏢 기업 임원", "📑 행정 공무원"],
    "INFP": ["🎨 화가", "✍️ 시인", "🕊️ NGO 활동가"],
    "ENTJ": ["👑 CEO", "📈 경영 컨설턴트", "🧭 프로젝트 리더"],
    "ISTP": ["🛠️ 엔지니어", "🚗 자동차 정비사", "🔧 기술자"],
    "ESTP": ["🏅 운동선수", "📣 세일즈 전문가", "🎤 쇼호스트"],
    "ISFP": ["🎶 음악가", "🌸 플로리스트", "📷 사진작가"],
    "ESFJ": ["🤝 사회복지사", "👩‍🏫 교사", "🎀 이벤트 플래너"],
    "INTP": ["💻 프로그래머", "🔬 연구원", "📚 학자"],
    "ENFJ": ["🌟 리더", "🎤 강연가", "💡 교육 컨설턴트"],
}

# -----------------------------
# 페이지 세팅
# -----------------------------
st.set_page_config(page_title="🌟 MBTI 직업 추천 🌟", page_icon="✨")

# -----------------------------
# 제목 영역
# -----------------------------
st.markdown(
    """
    <h1 style='text-align: center; color: #FF69B4;'>
    ✨🌈 MBTI 기반 진로 추천 서비스 🌈✨
    </h1>
    <h3 style='text-align: center; color: #FFA500;'>
    당신의 MBTI를 선택하면 <br> 반짝반짝 빛나는 ✨ 직업 추천이 기다리고 있어요! 🌟
    </h3>
    """,
    unsafe_allow_html=True,
)

st.write("")

# -----------------------------
# MBTI 선택
# -----------------------------
mbti = st.selectbox(
    "👉 당신의 MBTI를 선택하세요 💖",
    options=list(mbti_jobs.keys())
)

# -----------------------------
# 추천 결과 출력
# -----------------------------
if mbti:
    st.markdown(
        f"""
        <div style="background-color: #FFF0F5; border-radius: 15px; padding: 20px; margin-top: 20px;">
            <h2 style='text-align: center; color: #FF1493;'>🌟 {mbti} 유형의 추천 직업 🌟</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )

    for job in mbti_jobs[mbti]:
        st.markdown(
            f"<p style='font-size: 20px; color: #4B0082;'>💎 {job}</p>",
            unsafe_allow_html=True,
        )

    st.balloons()  # 🎈 추천 후 풍선 이펙트!
    st.snow()      # ❄️ 눈 내리는 이펙트!
