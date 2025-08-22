import streamlit as st
import random

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

# -----------------------
# 2. 질환별 추천 메뉴 + 가격 (가격 낮춤)
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
# 3. 추천 메뉴 합집합
# -----------------------
recommended_menus = set()
if diseases:
    for d in diseases:
        recommended_menus.update(menu_db.get(d, []))
recommended_menus = list(recommended_menus)[:3]  # 기본 3개 메뉴

# -----------------------
# 4. 아침/점심/저녁 메뉴 선택
# -----------------------
st.subheader("🕒 끼니별 메뉴 선택 (선택하지 않으면 자동 추천)")

meals = {}
meal_names = [("🍳 아침", 0), ("🥗 점심", 1), ("🍲 저녁", 2)]
for meal_name, idx in meal_names:
    options = [m[0] for m in recommended_menus]
    choice = st.selectbox(f"{meal_name} 메뉴 선택", ["추천 메뉴 자동 선택"] + options, key=meal_name)
    if choice == "추천 메뉴 자동 선택":
        meals[meal_name] = recommended_menus[idx] if idx < len(recommended_menus) else ("건강식", 5000)
    else:
        # 선택한 메뉴 이름으로 가격 찾기
        price = next((p for n, p in recommended_menus if n == choice), 5000)
        meals[meal_name] = (choice, price)

# -----------------------
# 5. 선택 메뉴 표시
# -----------------------
st.subheader("✅ 최종 선택 메뉴")
total_price = 0
for meal_name, (menu_name, price) in meals.items():
    st.write(f"{meal_name}: {menu_name} 💰 {price}원")
    total_price += price

st.write(f"💰 **총 가격: {total_price}원**")

# -----------------------
# 6. 주문 버튼
# -----------------------
if st.button("🚚 이 식단 주문하기"):
    st.success("주문 완료! 곧 건강식이 배송됩니다 🥳")
