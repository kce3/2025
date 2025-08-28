import streamlit as st
import random

# --- 페이지 설정 ---
st.set_page_config(page_title="건강 식단 추천", page_icon="🥗", layout="centered")
st.markdown("""
<style>
body { background-color: #FFF8F0; font-size:20px; }
.meal-card {
    padding: 20px; margin: 10px 0;
    border-radius: 15px; background-color: #FFEED9;
    box-shadow: 2px 2px 6px rgba(0,0,0,0.1); font-size:20px;
}
.highlight { font-weight:bold; font-size:22px; color:#D35400; }
button { font-size:20px; padding:10px 20px; }
</style>
""", unsafe_allow_html=True)

# --- 질환별 메뉴 ---
menus = {
    "당뇨": ["현미밥과 두부조림", "닭가슴살 샐러드", "귀리죽"],
    "고혈압": ["저염 미역국과 보리밥", "채소비빔밥", "두부샐러드"],
    "고지혈증": ["연어구이와 퀴노아", "시금치 나물밥", "두부버섯볶음"],
    "위염": ["죽(야채죽/소고기죽)", "연두부덮밥", "계란찜"],
    "과체중": ["닭가슴살 샐러드", "귀리 샐러드볼", "두부스테이크"],
    "빈혈": ["시금치비빔밥", "소고기 미역국", "간장조림 두부"],
    "아토피": ["현미밥과 채소볶음", "고구마 샐러드", "두부 스프"],
    "골다공증": ["멸치볶음과 현미밥", "두부버섯탕", "치즈샐러드"]
}
prices = {menu: price for menu_list in menus.values() for menu, price in zip(menu_list, [6000,6500,7000])}

# --- 제목 ---
st.title("🥗 간편 건강 식단 주문하기")

# --- 질환 선택 ---
disease = st.selectbox("질환을 선택하세요:", list(menus.keys()))

st.markdown("---")
st.write("원하는 끼니를 아래에서 선택하세요:")

meal_names = ["아침", "점심", "저녁"]
chosen_meals = {}

for meal in meal_names:
    st.subheader(f"🍽 {meal}")
    col1, col2 = st.columns(2)
    with col1:
        if st.button(f"{meal} 추천받기", key=f"rec_{meal}"):
            menu = random.choice(menus[disease])
            chosen_meals[meal] = menu
    with col2:
        menu = st.selectbox(f"{meal} 직접 선택", menus[disease], key=f"sel_{meal}")
        if menu:
            chosen_meals[meal] = menu
    
# --- 선택 메뉴 표시 ---
for meal, menu in chosen_meals.items():
    st.markdown(f"<div class='meal-card'>✅ <span class='highlight'>{meal}: {menu} ({prices[menu]}원)</span></div>", unsafe_allow_html=True)

# --- 총합 계산 ---
if chosen_meals:
    total = sum(prices[m] for m in chosen_meals.values())
    st.markdown("---")
    st.markdown(f"## 💰 총 합계: <span class='highlight'>{total}원</span>", unsafe_allow_html=True)
