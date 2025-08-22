import streamlit as st

st.set_page_config(page_title="맞춤 건강식 배달", page_icon="🍱", layout="centered")
st.title("🍱 질환별 맞춤 건강식 배달 서비스")
st.write("여러 질환을 고려해 배달 가능한 건강식 메뉴를 추천합니다! 🚚")

# -----------------------
# 1. 사용자 입력
# -----------------------
diseases = st.multiselect(
    "💊 가지고 있는 질환 선택 (1개 이상 가능):",
    ["고혈압", "당뇨", "고지혈증", "과체중/비만", "빈혈", "위염", "역류성 식도염", "아토피/알레르기", "골다공증"]
)

st.subheader("🕒 원하는 끼니 선택")
breakfast = st.checkbox("🍳 아침", value=True)
lunch = st.checkbox("🥗 점심", value=True)
dinner = st.checkbox("🍲 저녁", value=True)

# -----------------------
# 2. 질환별 추천 메뉴 + 가격
# -----------------------
menu_db = {
    "고혈압": [("저염 두부덮밥", 8000), ("고등어구이 정식", 10000), ("닭가슴살 샐러드", 9000)],
    "당뇨": [("현미밥 도시락", 9000), ("연어샐러드", 11000), ("두부스테이크 도시락", 9500)],
    "고지혈증": [("귀리죽", 7000), ("연어스테이크", 12000), ("채소구이 플래터", 10000)],
    "과체중/비만": [("다이어트 도시락", 9500), ("그릭요거트볼", 7000), ("퀴노아 샐러드", 9000)],
    "빈혈": [("소고기 미역국 정식", 10000), ("간볶음 덮밥", 9500), ("시금치 오믈렛 도시락", 8500)],
    "위염": [("양배추죽", 7000), ("감자수프", 7500), ("바나나 스무디", 6500)],
    "역류성 식도염": [("닭죽", 7000), ("흰살생선구이", 9500), ("채소스프 + 호밀빵", 8000)],
    "아토피/알레르기": [("기본 도시락(쌀밥+채소+달걀)", 9000), ("사과 샐러드", 7000), ("채식 도시락", 9500)],
    "골다공증": [("두부 스테이크 정식", 9500), ("멸치볶음과 시금치나물 도시락", 9000), ("우유+요거트 스무디", 6500)]
}

# -----------------------
# 3. 추천 메뉴 계산
# -----------------------
if diseases:
    # 선택한 질환 메뉴 합집합
    recommended_menus = set()
    for d in diseases:
        recommended_menus.update(menu_db.get(d, []))

    recommended_menus = list(recommended_menus)[:3]  # 기본 3개 메뉴만 사용

    st.subheader("✅ 기본 추천 메뉴 😋")
    for m, price in recommended_menus:
        st.write(f"- {m} 💰 {price}원")

    # -----------------------
    # 4. 끼니별 추천
    # -----------------------
    st.subheader("🍴 선택한 끼니별 메뉴")
    meals = [("🍳 아침", breakfast), ("🥗 점심", lunch), ("🍲 저녁", dinner)]
    for i, (meal_name, selected) in enumerate(meals):
        if selected and i < len(recommended_menus):
            m, price = recommended_menus[i]
            st.markdown(f"**{meal_name}**: {m} 💰 {price}원")

    # -----------------------
    # 5. 주문 버튼
    # -----------------------
    if st.button("🚚 이 식단 주문하기"):
        st.success("주문 완료! 곧 건강식이 배송됩니다 🥳")
else:
    st.info("하나 이상의 질환을 선택해주세요!")
