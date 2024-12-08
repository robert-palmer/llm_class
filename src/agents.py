from crewai import Agent, Task
from crewai_tools import ScrapeWebsiteTool, SerperDevTool

search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()
"""
long/short variable to determine how we analyze the stock


"""
researcher = Agent(
      role="Researcher",
      goal="Collect stock-related data and news for {company} from online sources",
      backstory="You're a CFA charterholder with years of experience who is gathering information "
                "to begin researching {company} "
                "and trying to find important data, news, commentary, and recent and long-term trends."
                "You collect and summarize information that is relevant and financially material and "
                "can be used to make informed investing decisions."
                "and presenet it in a clear actionable format",
      allow_delegation=False,
      tools=[search_tool, scrape_tool],
      verbose=True,

  )


analyzer = Agent(
    role="Analyzer",
    goal="Analyze provided data, trends, commentary, and news to determine "
         "whether {company} stock is performing well or not ",
    backstory="You are an editor who receives information from the Researcher."
              "Your goal is to review the research "
              "to evaluate how the {company} has performed recently"
              "and to identify the most salient trends and any potential catalysts or significant"
              "developments that have happened recently "
              "and provide a reccomendation as to whether the {company} "
              "is going to perform well or badly",
    allow_delegation=False,
    verbose=True,
)

report_builder = Agent(
      role="Report Builder",
      goal="Provide a report on the most important information affecting {company} ",
      backstory="You're a CFA charterholder with years of experience who is analyzing  "
                "whether {company} is a good investment. "
                "You want to consider the most important financial and non-financial factors "
                "as well as macroeconomic factors that are effecting the company in the past, today, and the future.",
      allow_delegation=False,
      tools=[search_tool, scrape_tool],
      verbose=True,

  )


research = Task(
    description=(
        "1. Prioritize the latest trends, key players, commentary, events, "
            "financial information, and noteworthy news on {company}.\n"
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

report_build = Task(
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
    agent=report_builder,

)