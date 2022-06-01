"""
Enum — Python Orientado a Objetos
"""
from enum import Enum


class Directions(Enum):
    Right = 0
    Left = 1
    Up = 2
    Down = 3


def move(direction):
    if not isinstance(direction, Directions):
        raise ValueError('valor indisponível')

    return f'Moving {direction.name}'


if __name__ == '__main__':
    print(move(Directions.Right))
    print(move(Directions.Left))
    print(move(Directions.Up))
    print(move(Directions.Down))
