from crewai import Task
from pydantic import BaseModel

from .models import Edit_Task_Output
from .agents import researcher, technical_analyzer, econ_analyzer, fundamental_analyzer, report_builder, editor
 
research = Task(
    description=
        "1. Prioritize the latest trends, key players, commentary, events, "
            "financial information, and noteworthy news on {company}. "
        "2. Develop a detailed content outline including "
            "an introduction, key points, and a call to action."
        "3. Be sure to priortize different resources that highlight fundamental "
           "technical, and economic effects that help to analyze {company}. ",

    expected_output="A comprehensive content plan document "
        "with an outline, "
        "internet links, and resources."
        "list of the web sources and their links",
    agent=researcher,
)

technical_analyze = Task(
    description=
        "1. Use the relevant content from the researcher to craft a compelling "
            "technical analysis on {company}."
		    "2. Focus your analysis on technical analysis techniques, such as, price"
            "analysis, volume analysis, trendlines, etc."
        "3. Make sure sections/subtitles are properly named "
            "in an engaging manner."
        "4. Ensure your findings are structured with an "
            "engaging introduction, insightful body, "
            "and a summarizing conclusion."
        "5. Proofread for grammatical errors and "
            "concise writing.",

    expected_output="A well-written {company} technical analysis, "
        "ready for investor use, "
        "each section should have at least 1 paragraph.",
    agent=technical_analyzer,

)

fundamental_analyze = Task(
    description=
        "1. Use the relevant content from the researcher to craft a compelling "
            "fundamental analysis on {company}."
		    "2. Focus your analysis on fundamental analysis factors, such as, profitability"
            "company management, leverage, industry position, etc."
        "3. Make sure sections/subtitles are properly named "
            "in an engaging manner."
        "4. Ensure your findings are structured with an "
            "engaging introduction, insightful body, "
            "and a summarizing conclusion."
        "5. Proofread for grammatical errors and "
            "concise writing.",

    expected_output="A well-written {company} fundamental analysis, "
        "ready for investor use, "
        "each section should have at least 1 paragraph.",
    agent=fundamental_analyzer,

)

economic_analyze = Task(
    description=
        "1. Use the relevant content from the researcher to craft a compelling "
            "economic analysis on {company}."
		    "2. Focus your analysis on economic factors that may affect {company}"
            "such as, fed policy, consumer spending, industry specific trendds, etc."
        "3. Make sure sections/subtitles are properly named "
            "in an engaging manner."
        "4. Ensure your findings are structured with an "
            "engaging introduction, insightful body, "
            "and a summarizing conclusion."
        "5. Proofread for grammatical errors and "
            "concise writing.",

    expected_output="A well-written {company} economic analysis, "
        "ready for investor use, "
        "each section should have at least 1 paragraph.",
    agent=econ_analyzer,

)

report_build = Task(
    description=
        "1. Use the content from the analysts to craft a compelling "
            "report on {company}."
        "2. Be sure to include one section each for fundamental,"
            "technical, and economic analysis."
		"3. Make sure sections/subtitles are properly named "
            "in an engaging manner. "
        "4. Ensure the report structured with an "
            "engaging introduction, insightful body, "
            "and a summarizing conclusion. "
        "5. Proofread for grammatical errors and "
            "alignment with the brand's voice. ",

    expected_output="A well-written {company} investor report. "
        "Each section should have at least 1 paragraph.",
    agent=report_builder,

)


edit = Task(
    description=
        "1. Review the content from the report builder to ensure that "
            "the writing is concise and without spelling.",
    # expected_output=Edit_Task_Output,
    expected_output="A well-written {company} investor report. "
        "Each section should have at least 1 paragraph.",
    agent=editor,
    output_json=Edit_Task_Output
    # output_json=Edit_Task_Output()
    # output_file="content/output.json"

)




# research = Task(
#     description=(
#         "1. Prioritize the latest trends, key players, commentary, events, "
#             "financial information, and noteworthy news on {company}.\n"
#         "2. Develop a detailed content outline including "
#             "an overall summary, key points (financial and non financial), recent new, and the overall sentiment on the company.\n"
#         "3. Include SEO keywords and relevant data or sources."
#     ),
#     expected_output="A comprehensive investment overview document "
#         "with an outline, financial metrics"
#         "SEO keywords, and resources."
#         "list of the web sources and their links",
#     agent=researcher,
# )

# analyze = Task(
#     description=(
#         "1. Use the investment overview to craft a detailed and compelling "
#             "investment analysis on {company}.\n"
#         "2. Incorporate financial metrics, news, and catalysts naturally.\n"
# 		"3. Sections/Subtitles are properly named "
#             "in an engaging manner.\n"
#         "4. Ensure the post is direct with an "
#             "engaging introduction, insightful body, "
#             "and a summarizing conclusion.\n"
#         "5. Proofread for factual errors and "
#             "alignment with whether it is a good investment.\n"
#     ),
#     expected_output="A well-written {company} investment analysis, "
#         "ready for investor analysis, "
#         "each section should have 1 paragraph.",
#     agent=analyzer,
#     human_input=True,

# )

# report_build = Task(
#     description=(
#            "1. Use the content plan to craft a investment pitch on {company}.\n"
#         "2. Prioritize the most important information that is financially material.\n"
# 		"3. Sections/Subtitles are properly named "
#             "in an engaging manner.\n"
#         "4. Ensure the post is structured with an "
#             "engaging introduction, insightful body, "
#             "and a summarizing conclusion.\n"
#         "5. Proofread for grammatical errors and "
#             "alignment with the brand's voice.\n"
#     ),
#     expected_output="A well-written {company} analysis, "
#         "ready to present to the investment committee, "
#         "each section should have 1 paragraph.",
#     agent=report_builder,

# )