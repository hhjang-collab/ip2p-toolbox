import streamlit as st
import base64 # 로고 처리를 위해 추가

# --- 🖼️ 로고 변환 함수 ---
def get_base64_of_bin_file(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            return base64.b64encode(f.read()).decode()
    except:
        return "" 
# --------------------------------------------------------

# --- 1. 페이지 기본 설정 ---
st.set_page_config(
    page_title="업무 도구 포털",
    page_icon="🏢",
    layout="centered"
)

# --- 🎨 통합 CSS (제작사 로고 전용 CSS 포함) ---
st.markdown(
    """
    <style>
    /* 우측 상단 로고 고정 스타일 */
    .company-logo {
        position: fixed;
        top: 70px;      /* 짤리지 않게 내린 위치 유지 */
        right: 30px;    /* 우측 상단 고정 */
        width: 110px;   
        z-index: 1000;  
        cursor: pointer; /* 마우스 올리면 클릭 가능한 손가락 모양 */
    }
    
    /* 모바일 화면에서는 로고 작게 조절 */
    @media (max-width: 640px) {
        .company-logo {
            width: 80px;
            top: 60px;
            right: 10px; 
        }
    }
    </style>
    """, unsafe_allow_html=True
)
# -------------------------------------------------------------------

# --- 🖼️ 제작사 로고 화면에 띄우기 (HTML) ---
# 포털 저장소에 'company_logo.png' 파일이 있어야 합니다.
comp_img_base64 = get_base64_of_bin_file("company_logo.png") 

if comp_img_base64:
    st.markdown(
        f"""
        <a href="http://www.iptob.co.kr/" target="_blank" title="(주)아이피투비 홈페이지로 이동">
            <img src="data:image/png;base64,{comp_img_base64}" class="company-logo" alt="(주)아이피투비 로고">
        </a>
        """,
        unsafe_allow_html=True
    )
# -------------------------------------------------------------

# --- 2. 메인 화면 헤더 ---
st.title("🏢 업무 도구 포털")
st.markdown("---")

st.markdown("""
### 👋 환영합니다!
이곳은 업무 효율을 높이기 위해 제작된 업무 도구 포털입니다.  
필요한 작업을 선택하시면 해당 프로그램이 실행됩니다. 
*(보안을 위해 각 프로그램 접속 시 개별 로그인이 필요합니다)*
""")

st.write("")
st.write("")

# --- 3. 프로그램 링크 카드 섹션 (3열 그리드) ---
col1, col2, col3 = st.columns(3)

# 📦 첫 번째 박스
with col1:
    with st.container(border=True):
        # 제목 가운데 정렬
        st.markdown("<h4 style='text-align: center;'>녹색인증 챗봇</h4>", unsafe_allow_html=True)
        # 설명글도 가운데 정렬 및 회색 처리로 예쁘게
        st.markdown("<p style='text-align: center; color: gray; font-size: 0.95em;'>매뉴얼을 기반으로 녹색인증 관련 질의응답을 제공</p>", unsafe_allow_html=True)
        st.write("") 
        st.link_button("실행하기", url="https://green-chatbot-56eztzpmyzchahoppzgsmd.streamlit.app/", use_container_width=True)

# 📦 두 번째 박스
with col2:
    with st.container(border=True):
        st.markdown("<h4 style='text-align: center;'>서류검토 도우미</h4>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: gray; font-size: 0.95em;'>제출한 서류를 검토하고, 보완요청 메세지를 작성</p>", unsafe_allow_html=True)
        st.write("") 
        # ⬇️ 2번 앱은 주소가 나오면 나중에 이곳을 수정해 주세요!
        st.link_button("실행하기", url="https://green-check-jakrw5thqjgo3qxgb8ffwc.streamlit.app", use_container_width=True)

# 📦 세 번째 박스
with col3:
    with st.container(border=True):
        st.markdown("<h4 style='text-align: center;'>매출전표 정리</h4>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: gray; font-size: 0.95em;'>매출전표를 분리하고, 파일명을 규칙에 맞게 변경</p>", unsafe_allow_html=True)
        st.write("") 
        st.link_button("실행하기", url="https://sales-slip-9ahwfpatcrza7yxe6wnaxs.streamlit.app/", use_container_width=True)

st.markdown("---")

# --- 4. 카피라이트 설정 섹션 ---
st.caption("© 2026 (주)아이피투비. All rights reserved.")
