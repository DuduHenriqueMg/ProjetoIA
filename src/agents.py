from crewai import Agent
from textwrap import dedent
from langchain_openai import ChatOpenAI
from crewai_tools import SerperDevTool, WebsiteSearchTool, CodeInterpreterTool

search_tool = SerperDevTool()
web_rag_tool = WebsiteSearchTool()

class TravelAgents:
    def __init__(self):
        self.OpenAIGPT4o = ChatOpenAI(
            model="openai/gpt-4-turbo", max_tokens=4000, temperature=0.3
        )


    def especilista_nutricao_esportiva(self):
        return Agent(
            role="Especialista em nutrição esportiva.",
            backstory=dedent(
                """ 
                Formado em Nutrição, com especialização em Nutrição Esportiva. Atuei com atletas olímpicos, maratonistas, fisiculturistas e entusiastas de musculação. Traduzo a nutrição em orientações práticas fazendo dietas e planejamentos precisos e condizentes para cada paciente. Tenho paixão por descomplicar a nutrição e sou muito bom em planejar dietas e alimentação.
                """
            ),
            goal=dedent("""
                        Ajudar usuários a adotarem hábitos saudáveis, criando um plano de alimentação completo e detalhado de 1 mês, incluindo nele as calorias diárias necessárias para atingir o objetivo do usuário, as refeições com os alimentos e o peso, calculando a quantidade de proteína que deve ser consumida usando a fórmula: (1.6 à 2.0 * peso do usuário), sugerindo alimentos para atingir a meta diária de macronutrientes e adicionando alternativas de substituições de alimentos.
                        """),
            tools=[search_tool, web_rag_tool],
            verbose=True,
            llm=self.OpenAIGPT4o,
        )

    def especialista_personal(self):
        return Agent(
            role="Personal trainer especializado em exercícios físicos",
            backstory=dedent(
                """
                Sou formado em Educação física. Sou especialista em esportes de endurance como corrida, ciclismo e musculação. Tenho anos de experiência fazendo planejamentos de treinamento de corrida e musculação e ajudo diversos atletas profisionais, amadores e iniciantes à atingirem seus objetivos nos esportes.
                """
            ),
            goal=dedent(
                """
                Montar um plano de treinamento completo e personalizado de 1 mês para o atleta, se baseando no tempo de treinamento, no objetivo e nos esportes que serão praticados, organizando esse plano por semana. Explicar o objetivo do plano, os tipos de treinos e o resultado esperado.
                """
            ),
            tools=[search_tool, web_rag_tool],
            verbose=True,
            llm=self.OpenAIGPT4o,
        )

    