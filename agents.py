# agents.py
# A base class for a generic AI agent.
# The AI agent communicates with the OpenAI API to execute tasks.

import os
from openai import OpenAI

class AIAgent:
    """A base class for a generic AI agent."""
    def __init__(self, system_prompt):
        """
        Initializes the agent with a specific system prompt.
        The system prompt defines the agent's role, personality, and capabilities.
        """
        self.system_prompt = system_prompt
        # Create the OpenAI client instance here instead of at the global level.
        # This ensures it's created only after load_dotenv() has been called in main.py
        self.client = OpenAI()
        # A quick check to see if the key is loaded.
        if self.client.api_key is None:
            raise ValueError("OpenAI API key is not set.")
        # Check for any errors during client initialization
        except Exception as e:
            print(f"Fatal Error during OpenAI client initialization in Agent: {e}")
            print("Please ensure your OPENAI_API_KEY is set in the .env file and load_dotenv() is called before creating an agent.")
            exit()


    def execute_task(self, user_prompt, model="gpt-4o"):
        """
        Executes a task by sending a request to the OpenAI API.
        """
        print(f"------ [AGENT: {self.__class__.__name__}] is thinking... ------")
        try:
            # Use the instance's client: self.client
            response = self.client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.5,
            )
            result = response.choices[0].message.content
            print(f"------ [AGENT: {self.__class__.__name__}] finished. ------\n")
            return result
        except Exception as e:
            return f"An error occurred while communicating with OpenAI: {e}"

# Specialized Agents

class ResearcherAgent(AIAgent):
    """An AI agent specialized in gathering factual information and news."""
    def __init__(self):
        system_prompt = (
            "You are a world-class research assistant. Your goal is to find the most recent, "
            "relevant, and factual information about a given topic. "
            "Focus on key developments, official announcements, and market position. "
            "Do not provide opinions, only data and cited facts. Present the information clearly in bullet points."
        )
        super().__init__(system_prompt)

class FinancialAnalystAgent(AIAgent):
    """An AI agent specialized in financial analysis."""
    def __init__(self):
        system_prompt = (
            "You are an expert financial analyst. You are given a research report on a company. "
            "Your task is to analyze the provided text and give a concise financial summary. "
            "Focus on stock performance, revenue trends, and profitability based *only* on the information provided. "
            "Do not invent new data."
        )
        super().__init__(system_prompt)

class StrategistAgent(AIAgent):
    """An AI agent specialized in creating SWOT analysis."""
    def __init__(self):
        system_prompt = (
            "You are a senior business strategist. You are provided with a research report and a financial analysis. "
            "Your job is to synthesize this information into a clear and concise SWOT analysis "
            "(Strengths, Weaknesses, Opportunities, Threats). "
            "Each point in the SWOT analysis should be directly supported by the provided information."
        )
        super().__init__(system_prompt)
