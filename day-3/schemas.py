from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Response when document is uploaded
class DocumentResponse(BaseModel):
    id: int
    filename: str
    file_type: str
    file_path: str
    status: str
    created_at: datetime

    class Config:
        from_attributes = True

# Response with extracted text (for PDFs)
class DocumentWithText(DocumentResponse):
    extracted_text: Optional[str] = None

# Response for CSV data
class CSVData(BaseModel):
    filename: str
    rows: int
    columns: list
    data: list