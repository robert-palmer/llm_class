import os 
from dotenv import load_dotenv
from fastapi import FastAPI

from crews.crew import crew





load_dotenv()

FMP_API_KEY = os.getenv("FMP_API_KEY")
#SERPER_API_KEY = os.getenv("SERPER_API_KEY")
SERPER_DEV_API_KEY = os.getenv("SERPER_DEV_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

LLM_MODEL = "gpt-4o-mini"
os.environ["OPENAI_MODEL_NAME"] = LLM_MODEL

os.environ['SERPER_API_KEY'] = SERPER_DEV_API_KEY
os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY

# app = FastAPI()

# @app.get("/get_company_info/{company}")
# async def get_company_info(company: str):
#     inputs={"company": company}
#     result = await crew.kickoff_async(inputs)
#     return result


if __name__ == "__main__":
    inputs={"company": "RBOT"}
    result = crew.kickoff(inputs)

