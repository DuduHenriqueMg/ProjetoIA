from crewai import Crew, Process
from textwrap import dedent
from agents import TravelAgents
from tasks import TravelTasks
from dotenv import load_dotenv

load_dotenv()

class PlanejamentoCrew:
    def __init__(self, peso, imc, objetivo, tempo_treinamento, esportes):
        self.peso = peso
        self.objetivo = objetivo
        self.imc = imc
        self.tempo_treinamento = tempo_treinamento
        self.esportes = esportes
        

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = TravelAgents()
        tasks = TravelTasks()

        # Define your custom agents and tasks here
        especilista_nutricao_esportiva = agents.especilista_nutricao_esportiva()
        especialista_personal = agents.especialista_personal()

        # Custom tasks include agent name and variables as input
        criar_plano_de_alimentacao = tasks.criar_plano_de_alimentacao(
            especilista_nutricao_esportiva, 
            peso = self.peso,
            objetivo = self.objetivo, 
            imc = self.imc,
        )

        criar_plano_de_treinamento = tasks.criar_plano_de_treinamento(
            especialista_personal,
            objetivo = self.objetivo,
            peso = self.peso,
            esportes = self.esportes,
            tempo_treinamento= self.tempo_treinamento,
            
        )
        
        crew = Crew(
            agents=[especilista_nutricao_esportiva, especialista_personal],
            tasks=[criar_plano_de_alimentacao, criar_plano_de_treinamento],
            process=Process.sequential,
            verbose=True,
        )

        crew.kickoff()
        
        resultado_dieta = criar_plano_de_alimentacao.output
        resultado_treino = criar_plano_de_treinamento.output
        
        return [resultado_dieta, resultado_treino]


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to Trip Planner Crew")
    print("-------------------------------")
    peso = input(
        dedent("""
      From where will you be traveling from?
    """)
    )
    exercicios = input(
        dedent("""
      What are the exercicios options you are interested in visiting?
    """)
    )
    objetivo = input(
        dedent("""
      What is the date range you are interested in traveling?
    """)
    )
    imc = input(
        dedent("""
      What are some of your high level imc and hobbies?
    """)
    )

    trip_crew = TripCrew(peso, exercicios, objetivo, imc)
    result = trip_crew.run()
    print("\n\n########################")
    print("## Here is you Trip Plan")
    print("########################\n")
    print(result)