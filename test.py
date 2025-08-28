import streamlit as st
import random

st.set_page_config(page_title="건강 식단 추천", page_icon="🥗", layout="centered")

# --- 질환별 메뉴 ---
menus = {
    "당뇨": {"아침":["현미밥과 두부조림","귀리죽","닭가슴살 샐러드"],
           "점심":["닭가슴살 샐러드","채소비빔밥","현미밥과 채소볶음"],
           "저녁":["두부버섯볶음","연어구이와 퀴노아","귀리죽"]},
    "고혈압": {"아침":["저염 미역국과 보리밥","계란찜","귀리죽"],
            "점심":["채소비빔밥","두부샐러드","현미밥과 채소볶음"],
            "저녁":["두부버섯탕","닭가슴살 샐러드","연어구이"]},
    "고지혈증": {"아침":["오트밀","연두부","시금치죽"],
             "점심":["연어샐러드","퀴노아볼","채소비빔밥"],
             "저녁":["두부버섯볶음","연어구이와 퀴노아","닭가슴살 구이"]},
    "위염": {"아침":["죽(야채죽/소고기죽)","계란찜","연두부"],
           "점심":["닭가슴살 샐러드","현미밥과 채소볶음","채소비빔밥"],
           "저녁":["두부버섯탕","연어구이","귀리죽"]},
    "과체중": {"아침":["닭가슴살 샐러드","귀리 샐러드볼","두부스테이크"],
            "점심":["채소비빔밥","현미밥과 채소볶음","두부샐러드"],
            "저녁":["연어구이","닭가슴살 구이","두부버섯탕"]},
    "빈혈": {"아침":["시금치비빔밥","소고기죽","귀리죽"],
           "점심":["소고기 미역국","닭가슴살 샐러드","두부조림"],
           "저녁":["간장조림 두부","시금치 나물밥","연어구이"]},
    "아토피": {"아침":["현미밥과 채소볶음","고구마 샐러드","두부 스프"],
            "점심":["채소비빔밥","닭가슴살 샐러드","현미밥과 두부조림"],
            "저녁":["두부버섯탕","연어구이","귀리죽"]},
    "골다공증": {"아침":["멸치볶음과 현미밥","두부 스프","계란찜"],
             "점심":["두부버섯탕","치즈샐러드","채소비빔밥"],
             "저녁":["연어구이","닭가슴살 샐러드","현미밥과 두부조림"]}
}

prices = {menu: price for disease_menus in menus.values() for meal_list in disease_menus.values() for menu, price in zip(meal_list, [6000,6500,7000])}

st.title("🥗 맞춤 건강 식단 주문하기")

# --- 질환 선택 ---
diseases = st.multiselect("질환을 선택하세요 (여러 개 선택 가능):", list(menus.keys()))
st.markdown("---")

meal_names = ["아침", "점심", "저녁"]
chosen_meals = {}

# --- 끼니별 메뉴 상태 초기화 ---
for meal in meal_names:
    if f"options_{meal}" not in st.session_state:
        # 질환 선택 메뉴들을 합쳐 초기 옵션 설정
        combined_menu = []
        for d in diseases:
            combined_menu.extend(menus[d][meal])
        st.session_state[f"options_{meal}"] = list(dict.fromkeys(combined_menu))
    if f"selected_{meal}" not in st.session_state:
        st.session_state[f"selected_{meal}"] = None

# --- 끼니별 메뉴 선택 ---
for meal in meal_names:
    st.subheader(f"🍽 {meal} 메뉴 선택")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button(f"{meal} 추천받기", key=f"rec_{meal}"):
            if st.session_state[f"options_{meal}"]:
                menu = random.choice(st.session_state[f"options_{meal}"])
                chosen_meals[meal] = menu
                st.success(f"추천 메뉴: {menu} ({prices[menu]}원)")
                # 추천 후 드롭다운 초기화 (선택 메뉴 사라지게)
                st.session_state[f"options_{meal}"] = [menu]
                st.session_state[f"selected_{meal}"] = menu

    with col2:
        menu = st.selectbox(f"{meal} 직접 선택", st.session_state[f"options_{meal}"], key=f"sel_{meal}")
        if menu:
            chosen_meals[meal] = menu
            st.session_state[f"selected_{meal}"] = menu

# --- 주문하기 버튼 ---
if st.button("🛒 주문하기"):
    if chosen_meals:
        st.markdown("## ✅ 주문 완료!")
        for meal, menu in chosen_meals.items():
            st.markdown(f"{meal}: {menu} ({prices[menu]}원)")
        total = sum(prices[m] for m in chosen_meals.values())
        st.markdown(f"## 💰 총 합계: {total}원")
    else:
        st.warning("메뉴를 먼저 선택해주세요!")
