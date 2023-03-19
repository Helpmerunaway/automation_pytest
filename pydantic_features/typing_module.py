from typing import Sequence

from pydantic.dataclasses import dataclass

@dataclass
class Bingo:
    numbers: Sequence[int]

seq_list = [1, 2, 3]
seq_tuple = (4, 5, 6)

for bingo_sequence in seq_list, seq_tuple:
    print(Bingo(**{'numbers': bingo_sequence}))

# Bingo(numbers=[1, 2, 3])
# Bingo(numbers=(4, 5, 6))
