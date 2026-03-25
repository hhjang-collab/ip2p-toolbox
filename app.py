# --- 3. 프로그램 링크 카드 섹션 (3열 그리드) ---
col1, col2, col3 = st.columns(3)

# 📦 첫 번째 박스
with col1:
    with st.container(border=True):
        # 💡 HTML 태그를 이용해 제목을 가운데 정렬하고 글씨 크기를 키웁니다 (h4 태그)
        st.markdown("<h4 style='text-align: center;'>녹색인증 챗봇</h4>", unsafe_allow_html=True)
        st.write("매뉴얼을 기반으로 녹색인증 관련 질의응답을 제공")
        st.write("") 
        st.link_button("실행하기", url="https://green-chatbot-56eztzpmyzchahoppzgsmd.streamlit.app/", use_container_width=True)

# 📦 두 번째 박스
with col2:
    with st.container(border=True):
        st.markdown("<h4 style='text-align: center;'>서류검토 도우미</h4>", unsafe_allow_html=True)
        st.write("제출한 서류를 검토하고, 보완요청 메세지를 작성")
        st.write("") 
        st.link_button("실행하기", url="https://your-app2-url.streamlit.app", use_container_width=True)

# 📦 세 번째 박스
with col3:
    with st.container(border=True):
        st.markdown("<h4 style='text-align: center;'>매출전표 정리</h4>", unsafe_allow_html=True)
        st.write("매출전표를 분리하고, 파일명을 규칙에 맞게 변경")
        st.write("") 
        st.link_button("실행하기", url="https://sales-slip-9ahwfpatcrza7yxe6wnaxs.streamlit.app/", use_container_width=True)

st.markdown("---")
