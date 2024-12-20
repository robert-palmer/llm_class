import json
import os 
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Adjust this to the origin of your frontend
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, PUT, etc.)
    allow_headers=["*"],  # Allow all headers
)

@app.get("/get_company_info/{company}")
async def get_company_info(company: str):
    inputs={"company": company}
    result = await crew.kickoff_async(inputs)
    print(result)
    return result
