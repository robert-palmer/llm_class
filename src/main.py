import os 
import langchain_community
from crewai_tools import ScrapeWebsiteTool, SerperDevTool
from crewai import Agent, Task, Crew
from dotenv import load_dotenv, dotenv_values


from src.crews.crew import crew

load_dotenv()

FMP_API_KEY = os.getenv("FMP_API_KEY")
#SERPER_API_KEY = os.getenv("SERPER_API_KEY")
SERPER_DEV_API_KEY = os.getenv("SERPER_DEV_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

LLM_MODEL = "gpt-4o-mini"

os.environ["OPENAI_MODEL_NAME"] = LLM_MODEL
os.environ['SERPER_API_KEY'] = SERPER_DEV_API_KEY
os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY



if __name__ == "__main__":
    inputs={"company": "SMCI"}
    result = crew.kickoff(inputs)
