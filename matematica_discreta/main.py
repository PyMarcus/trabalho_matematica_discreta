from sorting_algorithms.Sort import Sort
import configparser


def main(length: int) -> None:
    """
    Função principal que cria as
    instâncias para ordenar os dados.
    Contudo, estes dados vêm de um arquivo
    do tipo ini
    :length: tamanho do array
    :return: None
    """
    parser = configparser.RawConfigParser()
    parser.read("./data/data.ini")
    sorted_algorithms = Sort()
    for key, value in parser[str(length)].items():
        print(f"Lista de tamanho {length}:")
        print(f"Desordenada:")
        # ultimo valor é desconsiderado por ser um espaço em branco(preparação do array)
        value1 = [int(num) for num in value.split(',')[:length]]
        value2 = [int(num) for num in value.split(',')[:length]]
        print(value1)
        print("Ordenada:")
        sorted_algorithms.merge_sort(value1)
        sorted_algorithms.insertion_sort(value2)


if __name__ == '__main__':
    main(10)
