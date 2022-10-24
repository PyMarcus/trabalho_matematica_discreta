import random
import aiofiles as af
import asyncio


def generates_entries(length: int) -> list[int]:
    """
        Função destinada a gerar os vetores
    de tamanhos solicitados pelo professor
    da disciplina.
    :param length:
    :return: void
    """

    # como é até 100000, o máximo, nao gasta tanta memo
    list_of_numbers = [random.randint(0, length) for num_randomic in range(length)]
    for numbers in list_of_numbers:
        yield numbers


async def write_in_file(length: int) -> None:
    """
       Para manter um padrão e facilitar a análise
    os dados serão salvos em um arquivo ini
    :param length (tamanho do vetor)
    :return: void
    """
    async with af.open("data.ini", 'a') as file:
        await file.writelines(f"[{length}]")
        await file.writelines('\n')
        await file.write(f"length_{length} = ")
        for values in generates_entries(length):
            await file.writelines(str(values) + ', ')
        await file.writelines('\n\n')


if __name__ == '__main__':
    asyncio.get_event_loop()
    asyncio.run(write_in_file(10))
    asyncio.run(write_in_file(50))
    asyncio.run(write_in_file(100))
    asyncio.run(write_in_file(1000))
    asyncio.run(write_in_file(10000))
    asyncio.run(write_in_file(100000))
