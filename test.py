import streamlit as st
import random

# --- 페이지 설정 ---
st.set_page_config(page_title="맞춤 건강 식단", page_icon="🥗", layout="centered")
st.markdown("""
<style>
body { background-color: #FFF8F0; }
.meal-card {
    padding: 20px; margin: 10px 0;
    border-radius: 15px; background-color: #FFEED9;
    box-shadow: 2px 2px 6px rgba(0,0,0,0.1); font-size: 18px;
}
.highlight { font-weight:bold; font-size:20px; color:#D35400; }
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

# --- 질환 선택 ---
st.title("🥗 맞춤 건강 식단 주문하기")
disease = st.selectbox("당신의 건강 상태에 맞는 질환을 선택하세요:", list(menus.keys()))
st.markdown("---")

# --- 끼니 수 선택 ---
meal_count = st.radio("몇 끼를 드시겠습니까?", [1,2,3], horizontal=True)

chosen_meals = {}
meal_names = ["아침", "점심", "저녁"]

# --- 메뉴 선택/추천 ---
for i in range(meal_count):
    st.subheader(f"🍽 {meal_names[i]} 메뉴 선택")
    method = st.radio(f"{meal_names[i]} 식사 방법 선택", ["추천받기 🤖", "내가 고르기 👤"], key=f"method_{i}")

    if method == "추천받기 🤖":
        menu = random.choice(menus[disease])
    else:
        menu = st.selectbox(f"{meal_names[i]} 메뉴를 고르세요", menus[disease], key=f"select_{i}")

    chosen_meals[meal_names[i]] = menu
    st.markdown(f"<div class='meal-card'>✅ <span class='highlight'>{meal_names[i]}: {menu} ({prices[menu]}원)</span></div>", unsafe_allow_html=True)

# --- 총합 계산 ---
total = sum(prices[m] for m in chosen_meals.values())
st.markdown("---")
st.markdown(f"## 💰 총 합계: <span class='highlight'>{total}원</span>", unsafe_allow_html=True)
