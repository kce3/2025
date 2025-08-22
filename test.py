import streamlit as st
import random

# -----------------------
# 1. 페이지 설정 + 배경색
# -----------------------
st.set_page_config(page_title="오늘 뭐 먹지? 🍱", page_icon="🍽️", layout="centered")

st.markdown(
    """
    <style>
    body {
        background-color: #FFF5E6;  /* 연한 주황빛 배경 */
        color: #4D2600;             /* 글자 브라운톤 */
    }
    .stButton>button {
        background-color: #FF8C42;  /* 식욕 돋는 주황 버튼 */
        color: white;
        font-size:16px;
    }
    .stSelectbox>div>div>div>select {
        background-color: #FFF3E0; /* 드롭다운 색 */
    }
    </style>
    """, unsafe_allow_html=True
)

st.title("🍽️ 오늘 뭐 먹지? 건강식 배달 추천")
st.write("질환과 선호도를 고려해 오늘 한 끼 메뉴를 추천해드려요! 😋")

# -----------------------
# 2. 사용자 입력
# -----------------------
diseases = st.multiselect(
    "💊 가지고 있는 질환 선택 (1개 이상)",
    ["고혈압", "당뇨", "고지혈증", "과체중/비만", "빈혈", "위염", "역류성 식도염", "아토피/알레르기", "골다공증"]
)

# -----------------------
# 3. 메뉴 DB (가격 낮춤)
# -----------------------
menu_db = {
    "고혈압": [("저염 두부덮밥", 7000), ("고등어구이 정식", 8000), ("닭가슴살 샐러드", 7000)],
    "당뇨": [("현미밥 도시락", 7500), ("연어샐러드", 8500), ("두부스테이크 도시락", 7500)],
    "고지혈증": [("귀리죽", 6500), ("연어스테이크", 9000), ("채소구이 플래터", 8000)],
    "과체중/비만": [("다이어트 도시락", 7500), ("그릭요거트볼", 6500), ("퀴노아 샐러드", 7000)],
    "빈혈": [("소고기 미역국 정식", 8000), ("간볶음 덮밥", 7500), ("시금치 오믈렛 도시락", 7000)],
    "위염": [("양배추죽", 6000), ("감자수프", 6500), ("바나나 스무디", 5500)],
    "역류성 식도염": [("닭죽", 6000), ("흰살생선구이", 7500), ("채소스프 + 호밀빵", 7000)],
    "아토피/알레르기": [("기본 도시락(쌀밥+채소+달걀)", 7000), ("사과 샐러드", 6000), ("채식 도시락", 7500)],
    "골다공증": [("두부 스테이크 정식", 7500), ("멸치볶음과 시금치나물 도시락", 7000), ("우유+요거트 스무디", 5500)]
}

# -----------------------
# 4. 추천 메뉴 계산
# -----------------------
if diseases:
    recommended_menus = set()
    for d in diseases:
        recommended_menus.update(menu_db.get(d, []))
    recommended_menus = list(recommended_menus)

    # -----------------------
    # 5. 랜덤 메뉴 추천
    # -----------------------
    if st.button("🎯 오늘 한 끼 추천받기"):
        if recommended_menus:
            menu_name, price = random.choice(recommended_menus)
            st.markdown(f"""
            <div style="background-color:#FFEDD5; padding:20px; border-radius:15px; margin-top:10px;">
            <h2 style="color:#FF6B35;">🍴 {menu_name}</h2>
            <p style="font-size:18px; color:#6B4226;">💰 가격: {price}원</p>
            <p style="font-size:16px;">오늘의 추천 건강식으로 맛있게 드세요! 😋</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.warning("선택한 질환에 맞는 추천 메뉴가 없습니다.")
else:
    st.info("먼저 하나 이상의 질환을 선택해주세요!")
