import streamlit as st
import random

# -----------------------
# 1. 페이지 설정 + 스타일
# -----------------------
st.set_page_config(page_title="오늘 뭐 먹지? 🍱", page_icon="🍽️", layout="centered")
st.markdown("""
<style>
body {background-color: #FFF5E6; color:#4D2600;}
.stButton>button {background-color: #FF8C42; color:white; font-size:16px;}
</style>
""", unsafe_allow_html=True)

st.title("🍽️ 오늘 건강식 메뉴 추천")
st.write("질환과 선호도를 고려해 오늘의 한 끼~세 끼 메뉴를 추천합니다 😋")

# -----------------------
# 2. 사용자 입력
# -----------------------
diseases = st.multiselect(
    "💊 가지고 있는 질환 선택 (1개 이상)",
    ["고혈압", "당뇨", "고지혈증", "과체중/비만", "빈혈", "위염", "역류성 식도염", "아토피/알레르기", "골다공증"]
)

# 몇 끼 먹을지 선택
meal_count = st.slider("오늘 몇 끼를 드실 예정인가요?", 1, 3, 1)

# 메뉴 추천 방식 선택
st.subheader("🍴 메뉴 추천 방식 선택")
recommend_mode = st.radio(
    "각 끼마다 메뉴를 어떻게 추천받을까요?",
    ("시스템 랜덤 추천", "본인이 선택")
)

# -----------------------
# 3. 메뉴 DB
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
recommended_menus = set()
if diseases:
    for d in diseases:
        recommended_menus.update(menu_db.get(d, []))
recommended_menus = list(recommended_menus)

# 끼니 이름
meal_names = ["🍳 아침", "🥗 점심", "🍲 저녁"][:meal_count]
meals = {}

# -----------------------
# 5. 끼니별 메뉴 추천/선택
# -----------------------
for meal in meal_names:
    st.subheader(f"{meal}")
    if recommend_mode == "시스템 랜덤 추천":
        menu_name, price = random.choice(recommended_menus)
        meals[meal] = (menu_name, price)
        st.markdown(f"- 추천 메뉴: **{menu_name}** 💰 {price}원")
    else:  # 본인이 선택
        options = [m[0] for m in recommended_menus]
        choice = st.selectbox("메뉴 선택", ["선택하세요"] + options, key=meal)
        if choice != "선택하세요":
            price = next((p for n, p in recommended_menus if n == choice), 5000)
            meals[meal] = (choice, price)

# -----------------------
# 6. 최종 주문 표시
# -----------------------
if meals and st.button("🚚 이 식단 주문하기"):
    total_price = sum(price for _, price in meals.values())
    st.subheader("✅ 주문 완료")
    for meal_name, (menu_name, price) in meals.items():
        st.write(f"{meal_name}: {menu_name} 💰 {price}원")
    st.write(f"💰 **총 가격: {total_price}원**")
    st.success("곧 건강식이 배송됩니다! 🥳")
