import os
from openai import OpenAI
from dotenv import load_dotenv

from rag.prompts import PROMPT
from rag.rag_agent import RagAgent

class LLMAgent :
    """LLM agent with OpenAI API."""

    def __init__(self):
        load_dotenv()
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        
    def call_llm(
        self,
        query:str,
        model:str="gpt-4o-mini",
        temperature:float=0.3      
    ) -> str:
        """Calls the OpenAI API to receive a response.

        Args:
            query (str): Query text
            model (str, optional): Set the model from the OpenAI models availables. Defaults to "gpt-4o-mini".
            temperature (float, optional): Set the temperature model. Defaults to 0.3.

        Returns:
            str: Returns the response based on the given query.
        """
        
        rag_agent = RagAgent()
        rag_response = rag_agent.retrieve_relevant_data(query=query)
        context = "\n".join(rag_response) if rag_response else "No hay datos relevantes para generar un contexto."
        
        messages = [
            {"role": "user", "content": PROMPT.format(context=context, query=query)}
        ]
        
        response=self.client.chat.completions.create(
            messages=messages,
            model=model,
            temperature=temperature
        )
        
        return (response.choices[0].message.content)
