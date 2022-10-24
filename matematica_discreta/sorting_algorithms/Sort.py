import datetime


class Sort:
    """
    Classe que contém dois métodos
    de ordenação para aferição dos
    resultados das complexidades dos
    algoritmos de ordenação utilizados.

    Ela lê o arquivo ini que contém diversos
    dados e , com base nele, faz as medições necessárias
    para analise de recorrência e complexidade do algoritmo

    Vale ressaltar,portanto, que não utilizo nenhuma forma
    de otimização da execução, como threads ou algo do tipo,
    pois, não é esse o intuito.

    Além disso, o código é desenvolvido em python por ser mais
    simples a analise por parte de leigos, do ponto de vista semântico.
    """
    __count_merge: int = 0
    __count_insertion: int = 0

    __time_merge_10 = 0
    __time_merge_50 = 0
    __time_merge_100 = 0
    __time_merge_1000 = 0
    __time_merge_10000 = 0
    __time_merge_100000 = 0

    __time_insertion_10 = 0
    __time_insertion_50 = 0
    __time_insertion_100 = 0
    __time_insertion_1000 = 0
    __time_insertion_10000 = 0
    __time_insertion_100000 = 0

    @classmethod
    def merge_sort(cls, vector: list[int]) -> None:
        """
        É um algoritmo de ordenação-por-intercalação
        Ele é recursivo, o que, por vez, pode-se estipular,
        por analise de recorrência, seu consumo de tempo.

        Logo, ele usa a estratégia de divisão e conquista
        Sua recorrência pode ser escrita na forma de:

         T(n) = Θ(nlog(n))

        Portanto, o algoritmo Mergesort é linearítmico.
        :param vector:
        :return: None
        """
        print(f"[+] Merge Sort {len(vector)}")
        start = datetime.datetime.now()
        cls.__merge_sort(vector)
        ends = datetime.datetime.now()
        print(vector)
        print(f"Tempo de execução Merge Sort: {ends - start}")
        print(f"Interações {cls.__count_merge}\n")
        width = len(vector)
        match width:
            case 10:
                cls.__time_merge_10 = ends - start
            case 50:
                cls.__time_merge_50 = ends - start
            case 100:
                cls.__time_merge_100 = ends - start
            case 1000:
                cls.__time_merge_1000 = ends - start
            case 10000:
                cls.__time_merge_10000 = ends - start
            case 100000:
                cls.__time_merge_100000 = ends - start

    @classmethod
    def insertion_sort(cls, vector: list[int]):
        """
        Insertion sort é um algoritmo de ordenação
        baseado no embaralhamento de cartas

         É eficiente para problemas com pequenas entradas, sendo o mais eficiente entre os algoritmos desta ordem de classificação.
        Sua recorrência pode ser escrita na forma de:

         T(n) = Θ(n²)

        Portanto, o algoritmo Mergesort é quadrático.
        :param vector:
        :return: None
        """
        print(f"[+] Insertion Sort {len(vector)}")
        start = datetime.datetime.now()
        print(vector)
        cls.__insertion_sort(vector, len(vector))
        ends = datetime.datetime.now()
        print(vector)
        print(f"Tempo de execução Insertion sort: {ends - start}")
        print(f"Interações {cls.__count_insertion}\n")
        width = len(vector)
        match width:
            case 10:
                cls.__time_insertion_10 = ends - start
            case 50:
                cls.__time_insertion_50 = ends - start
            case 100:
                cls.__time_insertion_100 = ends - start
            case 1000:
                cls.__time_insertion_1000 = ends - start
            case 10000:
                cls.__time_insertion_10000 = ends - start
            case 100000:
                cls.__time_insertion_100000 = ends - start

    @classmethod
    def __merge_sort(cls, vector: list[int]) -> None:
        """
        Dividir (recursivamente) e fazer o merge(conquistar)
        :param vector:
        :return:
        """
        if len(vector) > 1:
            # divisão em duas partes
            left = vector[:len(vector) // 2]
            right = vector[len(vector) // 2:]

            # recursão
            cls.__merge_sort(left)
            cls.__merge_sort(right)

            # junção
            i, j, k = 0, 0, 0
            while i < len(left) and j < len(right):
                cls.__count_merge += 1
                if left[i] < right[j]:
                    vector[k] = left[i]
                    i += 1
                else:
                    vector[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                vector[k] = left[i]
                i = i + 1
                k = k + 1
            while j < len(right):
                vector[k] = right[j]
                j += 1
                k += 1

    @classmethod
    def __insertion_sort(cls, vector: list[int], index: int) -> None:
        if index > 1:
            i = len(vector) - 1
            while i > 0:
                if vector[i] <= vector[i - 1]:
                    cls.__count_insertion += 1
                    aux = vector[i - 1]
                    vector[i - 1] = vector[i]
                    vector[i] = aux
                i -= 1
            cls.__insertion_sort(vector, index - 1)
