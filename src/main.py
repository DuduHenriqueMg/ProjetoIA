from crew import DireitoCrew


def run_law_assitent(pergunta: str):
    """
    Executa o Assistente de IA de Direito social.

    Args:
        pergunta (str): A pergunta de Direito Social que será enviada.

    Returns:
        str: A resposta do Assistente de IA.
    """
    if not pergunta.strip():
        return "⚠️ Entre com uma pergunta válida sobre Direito Social, por favor."

    # Initialize the DireitoCrew
    crew_instance = DireitoCrew()

    # Run the AI Compliance Assistant
    result = crew_instance.crew().kickoff(inputs={"pergunta": pergunta})

    return result