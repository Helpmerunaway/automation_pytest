from enum import Enum
from pydantic.dataclasses import dataclass


class News(Enum):
    FAKE = 'fake'
    REAL = 'real'


@dataclass
class TvProgram:
    news: News

print(TvProgram(**{'news': 'fake'}))

#   TvProgram(news=<News.FAKE: 'fake'>)
