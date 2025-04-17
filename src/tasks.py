from crewai import Task
from textwrap import dedent


class TravelTasks:
    def __tip_section(self):
        return "Se você fizer um bom trabalho será recompensado com um bonûs de 5000 mil reais!"

    def criar_plano_de_alimentacao(self, agent, peso, objetivo, imc):
        return Task(
            description=dedent(
                f"""
            **Task**: Fazer um plano de alimentação de 1 mês
            **Description**: Fazer um plano de alimentação de 1 mês para o usuário, com detalhes sobre   
                as calorias diárias, as refeições e alimentos que vão ser consumidos no dia. Fazer o plano considerando o peso, objetivo e Índice de massa corporal do usuário. Você pode sugerir os alimentos necessários e o peso deles para o usuário bater a meta de macronutrientes, calcular a
                quantidade de proteína necessária com a fórmula: (1.6 à 2.0*peso do usuário), sugerir alternativas de substituições de alimentos e dar dicas sobre alimentação sáudavel e dieta.
             

            **Parameters**: 
            - Peso: {peso}
            - Objetivo: {objetivo}
            - IMC (Índice de massa corporal): {imc} 
            

            **Note**: {self.__tip_section()}
        """
            ),
            agent=agent,
            expected_output=dedent(
                """
                Um plano alimentar completo de 1 mês em pt-BR, incluindo:
                - Calorias diárias
                - Alimentos
                - Cronograma de refeições diárias
                - Alternativas de substituição de alimentos
                - Dicas de alimentação saudável e motivação
                """
            ),
        )

    def criar_plano_de_treinamento(self, agent, objetivo, tempo_treinamento, esportes, peso):
        return Task(
            description=dedent(
                f"""
                    **Task**:  Fazer um plano de treinos de 1 mês
                    **Description**: Criar um planejamento de treino personalizado analisando e escolhendo os melhores 
                        treinos se baseaando nos esportes e no objetivo do usuário. Montar um cronograma de 1 mês de treinos com limite de 6 treinos por semana e 1 treino por dia. Montar esse cronograma considerando o objetivo, tempo de treinamento, esportes que serão praticados e o peso do usuário. Você pode sugerir treinos, ritmos específicos nos treinos de corrida, sugerir um volume semanal para os treinos de corrida e sugerir exercícios específicos, quantidade de séries e repetições nos treinos de força ou musculação. 

                    **Parameters**: 
                    - Objetivo: {objetivo}
                    - Tempo de Treinamento: {tempo_treinamento}
                    - Esportes: {esportes}
                    - Peso: {peso}
                    
                    **Note**: {self.__tip_section()}
        """
            ),
            agent=agent,
            expected_output=dedent(
                """
                Um cronograma de treinos completo de 1 mês em pt-BR, incluindo:
                - Treinos baseados nos parâmetros
                - Exércicios do treino se o treino for de força ou musculação
                - Ritmo e quilômetros da corrida se o treino for de corrida
                - Tipo de treino
                - Dicas para realizar um bom treino e manter a motivação
                """
            ),
        )

