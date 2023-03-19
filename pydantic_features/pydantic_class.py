from pydantic import BaseModel
from typing import Optional
from pydantic.dataclasses import dataclass

class QuestionOfLife(BaseModel):
    answer: int = 42

print(QuestionOfLife.__fields__)
#   {'answer': ModelField(name='answer', type=int, required=False, default=42)}

print(QuestionOfLife.__annotations__)
#   {'answer': <class 'int'>}

data = {'answer': 1337}

# might be None
@dataclass
class Question:
    answer: Optional[str]
Question(**{'answer': 'yep'})
Question(**{'answer': None})