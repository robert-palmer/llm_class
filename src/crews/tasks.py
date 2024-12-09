from crewai import Task
from .agents import researcher, analyzer, report_builder
 
research = Task(
    description=(
        "1. Prioritize the latest trends, key players, commentary, events, "
            "financial information, and noteworthy news on {company}.\n"
        "2. Develop a detailed content outline including "
            "an overall summary, key points (financial and non financial), recent new, and the overall sentiment on the company.\n"
        "3. Include SEO keywords and relevant data or sources."
    ),
    expected_output="A comprehensive investment overview document "
        "with an outline, financial metrics"
        "SEO keywords, and resources."
        "list of the web sources and their links",
    agent=researcher,
)

analyze = Task(
    description=(
        "1. Use the investment overview to craft a detailed and compelling "
            "investment analysis on {company}.\n"
        "2. Incorporate financial metrics, news, and catalysts naturally.\n"
		"3. Sections/Subtitles are properly named "
            "in an engaging manner.\n"
        "4. Ensure the post is direct with an "
            "engaging introduction, insightful body, "
            "and a summarizing conclusion.\n"
        "5. Proofread for factual errors and "
            "alignment with whether it is a good investment.\n"
    ),
    expected_output="A well-written {company} investment analysis, "
        "ready for investor analysis, "
        "each section should have 1 paragraph.",
    agent=analyzer,
    human_input=True,

)

report_build = Task(
    description=(
           "1. Use the content plan to craft a investment pitch on {company}.\n"
        "2. Prioritize the most important information that is financially material.\n"
		"3. Sections/Subtitles are properly named "
            "in an engaging manner.\n"
        "4. Ensure the post is structured with an "
            "engaging introduction, insightful body, "
            "and a summarizing conclusion.\n"
        "5. Proofread for grammatical errors and "
            "alignment with the brand's voice.\n"
    ),
    expected_output="A well-written {company} analysis, "
        "ready to present to the investment committee, "
        "each section should have 1 paragraph.",
    agent=report_builder,

)