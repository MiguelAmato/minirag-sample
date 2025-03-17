import os

from rag.rag_agent import RagAgent
from rag.llm_agent import LLMAgent

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  
FILE_PATH = os.path.join(BASE_DIR, "data", "pixar_films.csv")

def main():
    file_path = FILE_PATH
    rag_agent = RagAgent()
    llm_agent = LLMAgent()
    rag_agent.load_and_store_csv(file_path=file_path)

    print("\nChatbot Pixar RAG - Pregunta sobre películas de Pixar (escribe 'salir' para terminar)\n")

    while True:
        question = input("Tú: ")
        if question.lower() in ["salir", "exit", "quit"]:
            print("¡Hasta luego!")
            break
        
        response = llm_agent.call_llm(query=question)
        print(f"Bot: {response}\n")


if __name__ == "__main__":
    main()