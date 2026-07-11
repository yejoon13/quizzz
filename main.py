import streamlit as st
from questions import questions

st.set_page_config(page_title="💻 바이브 코딩 퀴즈", page_icon="💻", layout="wide")

st.markdown("""
<style>
.stApp{background:#f5f7fb;}
h1,h2,h3{color:#2563eb;text-align:center;}
.stButton>button{
    background:#2563eb;
    color:white;
    width:100%;
    height:45px;
    border-radius:10px;
}
</style>
""", unsafe_allow_html=True)

if "num" not in st.session_state:
    st.session_state.num = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "money" not in st.session_state:
    st.session_state.money = 0
if "checked" not in st.session_state:
    st.session_state.checked = False

st.title("💻 바이브 코딩 퀴즈")

col1,col2,col3=st.columns(3)
col1.metric("💰 기술화폐",f"{st.session_state.money}원")
col2.metric("🏆 정답",st.session_state.score)
col3.metric("📖 진행",f"{min(st.session_state.num+1,len(questions))}/{len(questions)}")

st.progress(st.session_state.num/len(questions))

if st.session_state.num < len(questions):

    q=questions[st.session_state.num]

    st.subheader(q["question"])

    answer=st.radio(
        "정답을 선택하세요.",
        q["choices"],
        key=f"q{st.session_state.num}"
    )

    if not st.session_state.checked:

        if st.button("제출"):

            if q["choices"].index(answer)==q["answer"]:
                st.success("🎉 정답입니다! (+500원)")
                st.session_state.score+=1
                st.session_state.money+=500
            else:
                st.error(f"❌ 오답입니다.\n\n정답 : {q['choices'][q['answer']]}")

            st.session_state.checked=True
            st.rerun()

    else:

        if st.button("다음 문제"):

            st.session_state.num+=1
            st.session_state.checked=False
            st.rerun()

else:

    st.balloons()

    st.title("🎉 퀴즈 완료!")

    st.success(f"정답 개수 : {st.session_state.score} / {len(questions)}")

    st.metric("💰 획득한 기술화폐",f"{st.session_state.money}원")

    if st.session_state.score==15:
        st.write("🏆 만점입니다! 훌륭해요!")

    elif st.session_state.score>=12:
        st.write("🥇 정말 잘했습니다!")

    elif st.session_state.score>=8:
        st.write("🥈 좋은 결과입니다!")

    else:
        st.write("🥉 다시 도전해 보세요!")

    if st.button("🔄 다시 시작"):

        st.session_state.num=0
        st.session_state.score=0
        st.session_state.money=0
        st.session_state.checked=False

        st.rerun()
