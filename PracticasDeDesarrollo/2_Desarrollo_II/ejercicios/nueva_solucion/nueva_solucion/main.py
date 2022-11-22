from typing import Dict, List, Tuple

import click


def mul(num: int, alt: bool = False):
    if alt:
        return num * 5
    return num * -2


b: int = mul(23, True)


class Mistery:
    def __init__(self, x: str, y: List[int]):
        self.x = x
        self.y = y

    def functionX(self) -> int:
        """Given a roman numeral (attr self.x), convert it to an integer.

        Returns:
            int: Roman number into int
        """

        ans = 0
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        for a, b in zip(self.x, self.x[1:]):
            if roman[a] < roman[b]:
                ans -= roman[a]
            else:
                ans += roman[a]

        return ans + roman[self.x[-1]]

    def functionY(self, target: int) -> Tuple[int, int]:
        """Given an array of integers nums (attr self.y) and an integer target, return indices of the two numbers such that they add up to target.

        Args:
            target (int): Target to reach.

        Returns:
            List[int]: List of indexes that form target.
        """
        numToIndex: dict[int, int] = {}

        for i, num in enumerate(self.y):
            if target - num in numToIndex:
                return numToIndex[target - num], i
            numToIndex[num] = i
        return -1, -1


@click.command("functionX")
@click.argument('roman', type=str, required=True)
def functionX(roman: str):
    """Llama a Mistrey.functionX

    Args:

        roman (str): Numero romano a convertir
    """
    mistery_instance = Mistery(roman, [])
    click.echo(f'{roman} en base 10 es {mistery_instance.functionX()}')


@click.command("functionY")
@click.argument('int_list', type=str, required=True)
@click.argument('target', type=int, required=True)
def functionY(int_list: str, target: int):
    """Llama a Mistery.functionY

    Args:

        int_list (str): Lista de enteros separada por coma

        target (int): Numero a formar en base a los números pasados cómo parámetro.
    """
    int_list_int = [int(x) for x in int_list.split(",")]
    mistery_instance = Mistery("", int_list_int)
    click.echo(
        f'{target} puede formarse sumando los valores en los indices {mistery_instance.functionY(target)}'
    )
