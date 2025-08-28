import streamlit as st
import random

st.set_page_config(page_title="건강 식단 추천", page_icon="🥗", layout="centered")

menus = {
    "당뇨": {"아침":["현미밥과 두부조림","귀리죽","닭가슴살 샐러드"],
           "점심":["닭가슴살 샐러드","채소비빔밥","현미밥과 채소볶음"],
           "저녁":["두부버섯볶음","연어구이와 퀴노아","귀리죽"]},
    "고혈압": {"아침":["저염 미역국과 보리밥","계란찜","귀리죽"],
            "점심":["채소비빔밥","두부샐러드","현미밥과 채소볶음"],
            "저녁":["두부버섯탕","닭가슴살 샐러드","연어구이"]},
    "과체중": {"아침":["닭가슴살 샐러드","귀리 샐러드볼","두부스테이크"],
            "점심":["채소비빔밥","현미밥과 채소볶음","두부샐러드"],
            "저녁":["연어구이","닭가슴살 구이","두부버섯탕"]}
}

prices = {menu: price for disease_menus in menus.values() for meal_list in disease_menus.values() for menu, price in zip(meal_list, [6000,6500,7000])}

st.title("🥗 맞춤 건강 식단 주문하기")

# 질환 선택
diseases = st.multiselect("질환을 선택하세요 (여러 개 선택 가능):", list(menus.keys()))
st.markdown("---")

meal_names = ["아침","점심","저녁"]
chosen_meals = {}

# 세션 상태 초기화
for meal in meal_names:
    key_options = f"options_{meal}"
    key_selected = f"selected_{meal}"
    if key_options not in st.session_state:
        combined_menu = []
        for d in diseases:
            combined_menu.extend(menus[d][meal])
        st.session_state[key_options] = list(dict.fromkeys(combined_menu))
    if key_selected not in st.session_state:
        st.session_state[key_selected] = None

# 메뉴 선택
for meal in meal_names:
    st.subheader(f"🍽 {meal} 메뉴 선택")
    options_key = f"options_{meal}"
    selected_key = f"selected_{meal}"
    combined_menu = st.session_state[options_key]

    col1, col2 = st.columns(2)
    with col1:
        if st.button(f"{meal} 추천받기", key=f"rec_{meal}"):
            if combined_menu:
                menu = random.choice(combined_menu)
                chosen_meals[meal] = menu
                st.success(f"추천 메뉴: {menu} ({prices[menu]}원)")
                # 추천 메뉴는 드롭다운에서 제외
                st.session_state[options_key] = [m for m in combined_menu if m != menu]
                st.session_state[selected_key] = menu

    with col2:
        # 드롭다운은 추천 메뉴 제외한 나머지 옵션
        menu = st.selectbox(f"{meal} 직접 선택", st.session_state[options_key], key=f"sel_{meal}")
        if menu:
            chosen_meals[meal] = menu
            st.session_state[selected_key] = menu

# 주문하기
if st.button("🛒 주문하기"):
    if chosen_meals:
        st.markdown("## ✅ 주문 완료!")
        for meal, menu in chosen_meals.items():
            st.markdown(f"{meal}: {menu} ({prices[menu]}원)")
        total = sum(prices[m] for m in chosen_meals.values())
        st.markdown(f"## 💰 총 합계: {total}원")
    else:
        st.warning("메뉴를 먼저 선택해주세요!")
