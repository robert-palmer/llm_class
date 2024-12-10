from pydantic import BaseModel

class Edit_Task_Output(BaseModel):
    introduction: str
    fundemental_analysis: str
    technical_analysis: str
    economic_analysis: str
    conclusion: str
