from dataclasses import dataclass


@dataclass
class Path:
    indices: list[int]
    length: float
    name: str
