__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import streamlit as st
from crew import PlanejamentoCrew

st.title("🔎  Bem Vindo ao seu assitente de IA de nutrição e esporte")

with st.sidebar:
    st.header("Crie seu planejamento mensal de nutrição e treinamento:")
    peso = st.text_input("Qual seu peso atual")
    imc = st.text_input("Qual seu IMC (Índice massa corporal)")
    objetivo = st.text_area("Qual seu objetivo na dieta e qual seu objetivo no esporte?")
    tempo_treinamento = st.text_area("Quanto tempo de treinamento você possui?")
    esportes = st.text_area("Quais esportes você deseja praticar e qual a frequência?")
    
if st.button("Gerar Planejamento 🚀"):
    if not peso or not imc or not objetivo or not tempo_treinamento or not esportes:
        st.warning("⚠️Preencha todos os campos.")
    else:
        st.write("⏳ Gerando o seu planejamento... Aguarde")

        research_crew = PlanejamentoCrew(
            peso=peso, 
            imc=imc, 
            objetivo=objetivo,
            tempo_treinamento=tempo_treinamento, 
            esportes=esportes
        )
        
        result = research_crew.run()
        st.subheader("Aqui está seu planejamento")
         
        for txt in result:
            st.markdown(txt)