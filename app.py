import streamlit as st

# --- 1. 페이지 기본 설정 ---
# 카드를 여러 개 나란히 배치하기 위해 넓은 화면(wide)으로 변경합니다.
st.set_page_config(
    page_title="통합 업무 포털",
    page_icon="🏢",
    layout="wide" 
)

# --- 2. 메인 화면 헤더 ---
st.title("🏢 사내 통합 업무 포털")
st.markdown("---")

st.markdown("""
### 👋 환영합니다!
이곳은 업무 효율을 높이기 위해 제작된 사내 도구 모음집(Toolbox)입니다.  
필요한 작업을 선택하시면 새 창에서 해당 프로그램이 실행됩니다. 
*(보안을 위해 각 프로그램 접속 시 개별 로그인이 필요합니다)*
""")

st.write("")
st.write("")

# --- 3. 프로그램 링크 카드 섹션 ---
# 한 줄에 3개씩 배치하기 위해 화면을 3등분(col1, col2, col3) 합니다.
col1, col2, col3 = st.columns(3)

# 📦 첫 번째 박스
with col1:
    with st.container(border=True): # 테두리가 있는 예쁜 박스 생성
        st.markdown("### 🌿 1. 녹색인증 챗봇")
        st.write("매뉴얼을 기반으로 녹색인증 관련 질의응답을 제공하는 AI 챗봇입니다.")
        st.write("") # 버튼 위 여백
        # ⬇️ 앱 1번 주소
        st.link_button("🚀 챗봇 실행하기", url="https://green-chatbot-56eztzpmyzchahoppzgsmd.streamlit.app/", use_container_width=True)

# 📦 두 번째 박스
with col2:
    with st.container(border=True):
        st.markdown("### 📄 2. 서류검토 Agent")
        st.write("복잡한 녹색인증 서류를 자동으로 검토하고 필요한 항목을 체크해 줍니다.")
        st.write("") 
        # ⬇️ 앱 2번 주소
        st.link_button("🚀 서류검토 실행하기", url="https://your-app2-url.streamlit.app", use_container_width=True)

# 📦 세 번째 박스
with col3:
    with st.container(border=True):
        st.markdown("### 🧾 3. 매출전표 자동화")
        st.write("흩어져 있는 매출전표 PDF 데이터를 취합하고 엑셀로 깔끔하게 정리해 줍니다.")
        st.write("") 
        # ⬇️ 앱 3번 주소
        st.link_button("🚀 매출전표 정리 실행", url="https://sales-slip-9ahwfpatcrza7yxe6wnaxs.streamlit.app/", use_container_width=True)

# 💡 나중에 4번째, 5번째 프로그램이 생기면?
# 아래처럼 빈 줄을 하나 넣고 새로운 컬럼을 만들어서 추가하시면 됩니다!
# st.write("")
# col4, col5, col6 = st.columns(3)
# with col4:
#     with st.container(border=True):
#         ...

st.markdown("---")
st.caption("© 2026 업무 자동화 시스템. All rights reserved.")
