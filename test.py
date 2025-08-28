import streamlit as st
import random

# ---------------------------
# 질환별 추천 메뉴 데이터
# ---------------------------
menus = {
    "고혈압": [("저염 한식 도시락", 6500), ("훈제 닭가슴살 샐러드", 7000), ("현미밥 & 나물 반찬 세트", 6000)],
    "당뇨": [("곤약밥 & 연어 도시락", 7000), ("닭가슴살 샐러드", 6500), ("두부 스테이크 도시락", 6800)],
    "고지혈증": [("귀리밥 & 채소구이", 6500), ("연어 샐러드", 7000), ("두부비빔밥", 6200)],
    "위염": [("죽 세트(단호박/야채)", 5500), ("연두부 덮밥", 6000), ("양배추죽", 5800)],
    "과체중": [("닭가슴살 샐러드", 6500), ("곤약비빔밥", 6200), ("현미 샌드위치", 6000)],
    "빈혈": [("소고기 미역국 세트", 7000), ("시금치 달걀덮밥", 6500), ("간연어 도시락", 7200)],
    "아토피": [("현미밥 & 채소반찬", 6000), ("닭가슴살 채소볶음", 6500), ("두부 샐러드", 6200)],
    "골다공증": [("멸치볶음 & 시래기밥", 6000), ("두부버섯찌개 세트", 6500), ("연어 스테이크 도시락", 7000)],
}

# ---------------------------
# 페이지 설정
# ---------------------------
st.set_page_config(page_title="건강 맞춤 식단 주문 🍱", page_icon="🍲", layout="centered")
st.markdown(
    """
    <style>
    body {
        background-color: #fff5e6; /* 따뜻한 베이지 톤 */
    }
    .stApp {
        background-color: #fff5e6;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🍱 질환 맞춤 건강 식단 주문하기")
st.write("본인의 건강 상태에 맞는 메뉴를 한 끼부터 세 끼까지 자유롭게 선택하세요!")

# ---------------------------
# 질환 선택
# ---------------------------
selected_conditions = st.multiselect("👉 본인이 가지고 있는 질환을 선택하세요", list(menus.keys()))

# ---------------------------
# 몇 끼 주문할지 선택
# ---------------------------
meal_count = st.radio("👉 오늘 몇 끼 주문하시겠습니까?", [1, 2, 3])

# ---------------------------
# 추천받을지 직접 고를지
# ---------------------------
order_type = st.radio("👉 메뉴 선택 방식을 골라주세요", ["추천받기 🍀", "직접 고르기 ✋"])

# ---------------------------
# 주문 처리
# ---------------------------
if selected_conditions:
    st.subheader("📌 오늘의 주문")

    total_price = 0
    meals = ["아침 🌅", "점심 🌞", "저녁 🌙"]

    for i in range(meal_count):
        if order_type == "추천받기 🍀":
            condition = random.choice(selected_conditions)
            menu, price = random.choice(menus[condition])
            st.write(f"**{meals[i]}**: {menu} ({price}원) - 추천 질환: {condition}")
        else:
            condition = st.selectbox(f"{meals[i]} 메뉴를 고르세요", selected_conditions, key=f"cond_{i}")
            menu, price = random.choice(menus[condition])
            st.write(f"**{meals[i]}**: {menu} ({price}원) - 선택 질환: {condition}")
        total_price += price

    st.subheader(f"💰 총 합계: {total_price} 원")
else:
    st.warning("⚠️ 질환을 최소 1개 이상 선택해주세요!")
