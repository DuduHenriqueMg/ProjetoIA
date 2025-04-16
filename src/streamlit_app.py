import streamlit as st
from main import run_law_assitent

st.title("🔎  Assistente de IA de DIreito Social")
st.write(
    "Esta IA te ajuda com questões sobre direito social"
)

# Sidebar for user selection
with st.sidebar:
    st.header("Selecione uma tarefa:")
    task_type = (
        "Responder pergunta sobre Direito Social"  # Since we have only one task, it's pre-selected
    )

    # Input field for user question
    user_input = st.text_area("Entre com sua pergunta sobre Direito Social:")

# Run the AI Compliance Assistant when the user clicks the button
if st.button("Executar pergunta 🚀"):
    if not user_input.strip():
        st.warning("⚠️Digite sua pergunta antes de executar.")
    else:
        st.write("⏳ Processando sua pergunta... Aguarde.")

        # ✅ Call the function from main.py
        result = run_law_assitent(user_input)

        # Display the AI response
        st.subheader("✅ Resposta da IA:")
        st.write(result)