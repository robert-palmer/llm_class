from crewai import Agent
from crewai_tools import ScrapeWebsiteTool, SerperDevTool

search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()

researcher = Agent(
      role="Researcher",
      goal="Collect stock-related data and news for {company} from online sources",
      backstory="You're a CFA charterholder with years of experience who is gathering information "
                "to begin researching {company} "
                "and trying to find important data, news, and recent, and long-term trends."
                "You collect and summarize information that is relevant and financially material and "
                "can be used to make informed investing decisions."
                "and presenet it in a clear actionable format",
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
    verbose=True,
)

report_builder = Agent(
      role="Report Builder",
      goal="Collect stock-related data and news for {company} from online sources",
      backstory="You're a CFA charterholder with years of experience who is gathering information "
                "to begin researching {company} "
                "and trying to find important data, news, and recent, and long-term trends."
                "You collect and summarize information that is relevant and financially material and "
                "can be used to make informed investing decisions."
                "and presenet it in a clear actionable format",
      allow_delegation=False,
      tools=[search_tool, scrape_tool],
      verbose=True,

  )