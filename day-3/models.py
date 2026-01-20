from sqlalchemy import Column, Integer, String, DateTime, Text
from datetime import datetime
from database import Base

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, nullable=False) # Orignal filename (e.g resume.pdf)
     
    file_type = Column(String, nullable=False) # pdf, csv, excel
    file_path = Column(String, nullable=False) # where file is stored on disk (eg, "uploads/123.pdf")
    extracted_text = Column(Text, nullable=True) # For PDFs
    """
    Extracted text from PDF (can be large, so use Text type)
    Nullable because CSV/Excel don't have extracted text
    """
    status = Column(String, default="pending") # pending, processed, failed
    """
    Track processing status
    "pending" → just uploaded
    "processed" → successfully processed
    "failed" → error during processing
    """
    created_at = Column(DateTime, default=datetime.utcnow)



