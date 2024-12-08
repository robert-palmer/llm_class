import os 
import langchain_community
from crewai_tools import ScrapeWebsiteTool, SerperDevTool
from crewai import Agent, Task, Crew
from dotenv import load_dotenv, dotenv_values

load_dotenv()

FMP_API_KEY = os.getenv("FMP_API_KEY")
#SERPER_API_KEY = os.getenv("SERPER_API_KEY")
SERPER_DEV_API_KEY = os.getenv("SERPER_DEV_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

LLM_MODEL = "gpt-4o-mini"

os.environ["OPENAI_MODEL_NAME"] = LLM_MODEL
os.environ['SERPER_API_KEY'] = SERPER_DEV_API_KEY
os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY


search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()

researcher = Agent(
      role="Researcher",
      goal="Find recent news for {company} stock that is relevant for an investor",
      backstory="You're are reseraching news for an investor "
                "and trying to find important trends."
                "You collect and summarize information that  "
                "can be used to make informed investing decisions."
                "Your work is the basis for "
                "the analyzer to analyze whether the company is"
                "performing well or not",
      allow_delegation=False,
      tools=[search_tool, scrape_tool],
      verbose=True,

  )

analyzer = Agent(
    role="Analyzer",
    goal="analyze given news stories to determine "
         "whether {company} stock is performing well or not ",
    backstory="You are an editor who receives articles from the researcher"
              "Your goal is to review the research "
              "to evaluate how the {company} has performed recently"
              "and to identify any potential catalysts or significant"
              "developments that have happened recently "
              "and provide a reccomendation as to whether the {company} "
              "is going to perform well or badly",
    allow_delegation=False,
    verbose=True
)

research = Task(
    description=(
        "1. Prioritize the latest trends, key players, events, "
            "and noteworthy news on {company}.\n"
        "2. Develop a detailed content outline including "
            "an introduction, key points, and a call to action.\n"
        "3. Include SEO keywords and relevant data or sources."
    ),
    expected_output="A comprehensive content plan document "
        "with an outline, "
        "SEO keywords, and resources."
        "list of the web sources and their links",
    agent=researcher,
)

analyze = Task(
    description=(
        "1. Use the content plan to craft a compelling "
            "analysis on {company}.\n"
        "2. Incorporate SEO keywords naturally.\n"
		"3. Sections/Subtitles are properly named "
            "in an engaging manner.\n"
        "4. Ensure the post is structured with an "
            "engaging introduction, insightful body, "
            "and a summarizing conclusion.\n"
        "5. Proofread for grammatical errors and "
            "alignment with the brand's voice.\n"
    ),
    expected_output="A well-written {company} post, "
        "ready for investor analysis, "
        "each section should have 1 paragraph.",
    agent=analyzer,

)

crew = Crew(
    agents=[researcher,analyzer],
    tasks=[research, analyze],
    verbose=True,
)

if __name__ == "__main__":
    inputs={"company": "SMCI"}
    result = crew.kickoff(inputs)
