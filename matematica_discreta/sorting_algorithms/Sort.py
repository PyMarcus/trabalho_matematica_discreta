import datetime
import sys

sys.setrecursionlimit(1000000000)  # permitir grandes recursões


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
    count_merge: int = 0
    count_insertion: float = 0

    time_merge_10 = 0
    time_merge_50 = 0
    time_merge_100 = 0
    time_merge_1000 = 0
    time_merge_10000 = 0
    time_merge_100000 = 0

    time_insertion_10 = 0
    time_insertion_50 = 0
    time_insertion_100 = 0
    time_insertion_1000 = 0
    time_insertion_10000 = 0
    time_insertion_100000 = 0

    @classmethod
    def merge_sort_(cls, vector: list[int]) -> None:
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
        cls.merge_sort(vector, len(vector))
        ends = datetime.datetime.now()
        print(f"Tempo de execução Merge Sort: {ends - start}")
        print(f"Interações {cls.count_merge}\n")
        width = len(vector)
        match width:
            case 10:
                cls.time_merge_10 = ends - start
            case 50:
                cls.time_merge_50 = ends - start
            case 100:
                cls.time_merge_100 = ends - start
            case 1000:
                cls.time_merge_1000 = ends - start
            case 10000:
                cls.time_merge_10000 = ends - start
            case 100000:
                cls.time_merge_100000 = ends - start

    @classmethod
    def merge_sort(cls, arr, n):
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
        temp_arr = [0] * n
        return cls._mergeSort(arr, temp_arr, 0, n - 1)

    @classmethod
    def _mergeSort(cls, arr, temp_arr, left, right):
        # Dividir (recursivamente) e fazer o merge(conquistar)
        cls.count_merge = 0

        if left < right:
            mid = (left + right) // 2
            cls.count_merge += cls._mergeSort(arr, temp_arr, left, mid)

            cls.count_merge += cls._mergeSort(arr, temp_arr, mid + 1, right)

            cls.count_merge += cls.merge(arr, temp_arr, left, mid, right)
        return cls.count_merge

    @classmethod
    def merge(cls, arr, temp_arr, left, mid, right):
        i, j, k = left, mid + 1, left
        cls.count_merge = 0
        # Checam as codições
        # i e j não excedem os limites do array
        while i <= mid and j <= right:
            # Não há inversão se a condição abaixo ocorrer
            if arr[i] <= arr[j]:
                temp_arr[k] = arr[i]
                k += 1
                i += 1
            else:
                # Há inversão
                temp_arr[k] = arr[j]
                cls.count_merge += (mid - i + 1)
                k += 1
                j += 1
        # e os arrays vao para o array temporário
        while i <= mid:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        # subarray into temporary array
        while j <= right:
            temp_arr[k] = arr[j]
            k += 1
            j += 1
        # Copy the sorted subarray into Original array
        for loop_var in range(left, right + 1):
            arr[loop_var] = temp_arr[loop_var]
        return cls.count_merge

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
        if len(vector) < 100000:
            print(f"[+] Insertion Sort {len(vector)}")
            start = datetime.datetime.now()
            cls.__insertion_sort(vector, 0)
            print(vector)
            ends = datetime.datetime.now()
            print(f"Tempo de execução Insertion sort: {ends - start}")
            print(f"Interações {cls.count_insertion}\n")
            width = len(vector)
            match width:
                case 10:
                    cls.time_insertion_10 = ends - start
                case 50:
                    cls.time_insertion_50 = ends - start
                case 100:
                    cls.time_insertion_100 = ends - start
                case 1000:
                    cls.time_insertion_1000 = ends - start
                case 10000:
                    cls.time_insertion_10000 = ends - start
                case 100000:
                    cls.time_insertion_100000 = ends - start

    @classmethod
    def __insertion_sort(cls, vector: list[int], index: int) -> None:
        if index != len(vector):
            for n in range(index, 0, -1):
                if vector[n - 1] > vector[n]:
                    aux = vector[n - 1]
                    cls.count_insertion += 1  # realiza 2 trocas
                    vector[n - 1] = vector[n]
                    vector[n] = aux
            cls.__insertion_sort(vector, index + 1)
