from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.knowledge.source.pdf_knowledge_source import PDFKnowledgeSource

pdf_tool = PDFKnowledgeSource(file_paths=["constituicao.pdf", "direitos_fundametais_sociais.pdf", "regime_direito_social.pdf"])

llm = LLM(
    model="openai/gpt-4o-mini",
    temperature=0,
    max_tokens=1500,
)

@CrewBase
class DireitoCrew:
    agents_config = "../config/agents.yaml"
    tasks_config = "../config/tasks.yaml"

    @agent
    def especialista_direito_social(self) -> Agent:
        return Agent(
            config=self.agents_config["especialista_direito_social"],
            verbose=True,
            llm=llm,
        )

    @task
    def responder_pergunta_direito_social(self) -> Task:
        return Task(
            config=self.tasks_config["responder_pergunta_direito_social"],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the MQuestKnowledge crew"""

        return Crew(
            agents=[self.especialista_direito_social()],
            tasks=[
                self.responder_pergunta_direito_social(),
            ],
            process=Process.sequential,
            verbose=True,
            knowledge_sources=[pdf_tool],
        )
        