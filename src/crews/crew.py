from crewai import Crew
from .agents import researcher, analyzer, report_builder
from .tasks import research, analyze, report_build

crew = Crew(
    agents=[researcher,analyzer, report_builder],
    tasks=[research, analyze, report_build],
    verbose=True,
)