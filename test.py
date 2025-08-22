import streamlit as st

st.title("질환 맞춤 배달 음식 추천 🍱")

# 질환 선택
diseases = st.multiselect(
    "가지고 있는 질환을 선택하세요:",
    ["고혈압", "당뇨", "고지혈증", "비만", "위염", "역류성 식도염"]
)

# 추천 메뉴
menu = {
    ("고혈압", "당뇨"): [
        "현미밥과 닭가슴살 샐러드 세트",
        "연어 스테이크와 구운 채소",
        "저염 된장국 + 잡곡밥 + 구운 생선 정식"
    ],
    ("고혈압", "고지혈증"): [
        "두부 스테이크 정식 (현미밥 포함)",
        "지중해식 연어 샐러드 (올리브오일 드레싱)",
        "버섯·채소 비빔밥 (저염 간장 소스)"
    ],
    ("당뇨", "비만"): [
        "닭가슴살 샐러드 랩 (통밀 또띠아)",
        "곤약 비빔국수 세트",
        "구운 연어와 샐러드 볼"
    ],
    ("위염", "역류성 식도염"): [
        "닭죽/소고기야채죽 세트",
        "흰살생선구이 + 감자샐러드",
        "채소스프 + 호밀빵"
    ]
}

if len(diseases) >= 2:
    found = False
    for key, menus in menu.items():
        if all(d in diseases for d in key):
            st.subheader("추천 메뉴 🍴")
            for m in menus:
                st.write(f"- {m}")
            found = True
    if not found:
        st.warning("선택하신 질환 조합에 맞는 메뉴가 준비되지 않았습니다.")
else:
    st.info("질환을 2개 이상 선택하세요!")

