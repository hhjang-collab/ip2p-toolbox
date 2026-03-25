import streamlit as st

# --- 1. 페이지 기본 설정 ---
st.set_page_config(
    page_title="통합 업무 포털",
    page_icon="🏢",
    layout="centered"
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
# URL 부분에 실제 배포하신 3개의 스트림릿 주소를 넣어주세요!

st.success("#### 🌿 1. 녹색인증 챗봇")
st.write("매뉴얼을 기반으로 녹색인증 관련 질의응답을 제공하는 AI 챗봇입니다.")
# ⬇️ 여기에 1번 앱 주소를 넣으세요!
st.link_button("🚀 녹색인증 챗봇 실행하기", url="https://green-chatbot-56eztzpmyzchahoppzgsmd.streamlit.app/", use_container_width=True)

st.write("")

st.info("#### 📄 2. 녹색인증 서류검토 Agent PRO")
st.write("복잡한 녹색인증 서류를 자동으로 검토하고 필요한 항목을 체크해 줍니다.")
# ⬇️ 여기에 2번 앱 주소를 넣으세요!
st.link_button("🚀 서류검토 프로그램 실행하기", url="https://your-app2-url.streamlit.app", use_container_width=True)

st.write("")

st.warning("#### 🧾 3. 매출전표 정리 자동화")
st.write("흩어져 있는 매출전표 PDF 데이터를 취합하고 엑셀로 깔끔하게 정리해 줍니다.")
# ⬇️ 여기에 3번 앱 주소를 넣으세요!
st.link_button("🚀 매출전표 정리 실행하기", url="https://sales-slip-9ahwfpatcrza7yxe6wnaxs.streamlit.app/", use_container_width=True)

st.markdown("---")
st.caption("© 2026 업무 자동화 시스템. All rights reserved.")
