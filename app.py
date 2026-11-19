# type: ignore
import streamlit as st
from modelo import modelo, criar_mensagens_iniciais
from langchain_core.messages import HumanMessage

st.header("Luan - FitPlus", divider= True)
st.markdown("### converse com o Vendedor")
if st.button("🔄 Nova conversa"):
    st.session_state["mensagens"] = criar_mensagens_iniciais()
    st.rerun()

if "mensagens" not in st.session_state:
    st.session_state["mensagens"]= criar_mensagens_iniciais()

for mensagem in st.session_state["mensagens"]:
    if mensagem.type != "system":
        with st.chat_message(mensagem.type):
            st.write(mensagem.content)

prompt = st.chat_input("Digite sua Mensagem ...")

if prompt:
    st.session_state["mensagens"].append(HumanMessage(prompt))
    with st.spinner("Luan está digitando...")
        resposta = modelo.invoke(st.session_state["mensagens"])
    st.session_state["mensagens"].append(resposta)
    st.rerun()