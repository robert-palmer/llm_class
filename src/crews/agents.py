from re import VERBOSE
from crewai import Agent
from crewai_tools import ScrapeWebsiteTool, SerperDevTool
"""
long/short variable to determine how we analyze the stock
one dude makes a bull case, other makes a bear case
variables - analyst focuses on technicals, other fundementals 

"""
VERBOSE = False


search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()

researcher = Agent(
      role="Researcher",
      goal="Collect stock-related data and news for {company} from online sources",
      backstory="You're a CFA Analyst working for a hedge fund with years of experience who is gathering information "
                "to begin researching {company} "
                "and trying to find important data, news, commentary, and recent and long-term trends."
                "You collect and summarize information that is relevant and financially material and "
                "can be used to make informed investing decisions."
                "and presenet it in a clear actionable format",
      allow_delegation=False,
      tools=[search_tool, scrape_tool],
      verbose=VERBOSE,

  )


analyzer = Agent(
    role="Analyzer",
    goal="Analyze provided data, trends, commentary, and news to determine "
         "whether {company} stock is performing well or not ",
    backstory="You are a portfolio manager who receives information from the Researcher."
              "Your goal is to review the research "
              "to evaluate how the {company} has performed recently"
              "and to identify the most salient trends and any potential catalysts or significant"
              "developments that have happened recently "
              "and provide a reccomendation as to whether the {company} "
              "is going to perform well or badly",
    allow_delegation=False,
    verbose=VERBOSE,
)

report_builder = Agent(
      role="Report Builder",
      goal="Provide a report on the most important information affecting {company} ",
      backstory="You're a CFA charterholder with years of experience who is analyzing  "
                "whether {company} is a good investment. "
                "You want to consider the most important financial and non-financial factors "
                "as well as macroeconomic factors that are effecting the company in the past, today, and the future."
                "Please be clear whether the investment is good or bad. If bad, do not try to sugarcoat it.",
      allow_delegation=True,
      tools=[],
      verbose=VERBOSE,

  )


