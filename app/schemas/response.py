from pydantic import BaseModel
from typing import Optional, Dict, List, Union

class Response(BaseModel):
    """Standardized response model

    Args:
        BaseModel (_type_): Pydantic base model class
    """
    
    status: int
    message: str
    value: Optional[Union[Dict, List]] = None