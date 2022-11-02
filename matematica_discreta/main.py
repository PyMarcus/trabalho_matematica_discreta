import sys
from typing import Any, Tuple
from sorting_algorithms.Sort import Sort
import configparser

sys.setrecursionlimit(1000000000)  # permitir grandes recursões


def main(length: int) -> tuple[int, Any, Any, int, float]:
    """
    Função principal que cria as
    instâncias para ordenar os dados.
    Contudo, estes dados vêm de um arquivo
    do tipo ini
    :length: tamanho do array
    :return: None
    """
    parser = configparser.RawConfigParser()
    parser.read("../data/data.ini")
    sorted_algorithms = Sort()
    for key, value in parser[str(length)].items():
        print(f"Lista de tamanho {length}:")
        print(f"Desordenada:")
        # ultimo valor é desconsiderado por ser um espaço em branco(preparação do array)
        value1 = [int(num) for num in value.split(',')[:length]]
        value2 = [int(num) for num in value.split(',')[:length]]
        print("Ordenada:")
        sorted_algorithms.merge_sort_(value1)
        sorted_algorithms.insertion_sort(value2)
        if length == 10:
            return length, sorted_algorithms.time_merge_10, \
                   sorted_algorithms.time_insertion_10, \
                   sorted_algorithms.count_merge, sorted_algorithms.count_insertion
        elif length == 50:
            return length, sorted_algorithms.time_merge_50, \
                   sorted_algorithms.time_insertion_50, \
                   sorted_algorithms.count_merge, sorted_algorithms.count_insertion
        elif length == 100:
            return length, sorted_algorithms.time_merge_100, \
                   sorted_algorithms.time_insertion_100, \
                   sorted_algorithms.count_merge, sorted_algorithms.count_insertion
        elif length == 1000:
            return length, sorted_algorithms.time_merge_1000, \
                   sorted_algorithms.time_insertion_1000, \
                   sorted_algorithms.count_merge, sorted_algorithms.count_insertion
        elif length == 10000:
            return length, sorted_algorithms.time_merge_10000, \
                   sorted_algorithms.time_insertion_10000, \
                   sorted_algorithms.count_merge, sorted_algorithms.count_insertion
        return length, sorted_algorithms.time_merge_100000, \
               sorted_algorithms.time_insertion_100000, \
               sorted_algorithms.count_merge, sorted_algorithms.count_insertion


if __name__ == '__main__':
    main(100000)
