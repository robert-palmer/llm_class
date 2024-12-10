from crewai import Crew, Process
from .agents import researcher, editor, technical_analyzer, fundamental_analyzer, econ_analyzer, report_builder
from .tasks import research, edit, report_build, fundamental_analyze, economic_analyze, technical_analyze

crew = Crew(
    agents=[researcher, technical_analyzer, fundamental_analyzer, econ_analyzer, report_builder, editor],
    tasks=[research, fundamental_analyze, economic_analyze, technical_analyze, report_build, edit],
    verbose=True,
    process=Process.sequential

)