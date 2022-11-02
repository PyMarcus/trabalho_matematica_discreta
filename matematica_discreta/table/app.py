from flask import Flask, render_template
from main import main
import math
app = Flask(__name__)


def table():
    # Busca os dados gerados em memória
    ten, time_merge_10, time_insertion_10, count_merge, count_insertion = main(10)
    fifty, time_merge_50, time_insertion_50, count_merge50, count_insertion50 = main(50)
    hundred, time_merge_100, time_insertion_100, count_merge100, count_insertion100 = main(100)
    thousand, time_merge_1000, time_insertion_1000, count_merge1000, count_insertion1000 = main(1000)
    ten_thousand, time_merge_10000, time_insertion_10000, count_merge10000, count_insertion10000 = main(10000)
    hundred_th, time_merge_100000, time_insertion_10000, count_merge100000, count_insertion10000 = main(100000)
    itens = [10, 50, 100, 1000, 10000, 100000]
    merge = [count_merge, count_merge50, count_merge100, count_merge1000, count_merge10000, 100000]
    insertion = [count_insertion, count_insertion50, count_insertion100, count_insertion1000, count_insertion10000, 100000]
    data = [{
        f"quantidade": ten,
        "comparacoes_esperadas": int(ten * math.log2(ten)),
        "comparacoes_alcancadas": count_merge,
        "tempo": time_merge_10
    },
        {
            f"quantidade": fifty,
            "comparacoes_esperadas": int(fifty * math.log2(fifty)),
            "comparacoes_alcancadas": count_merge50,
            "tempo": time_merge_50
        },
        {
            f"quantidade": hundred,
            "comparacoes_esperadas": int(hundred * math.log2(hundred)),
            "comparacoes_alcancadas": count_merge100,
            "tempo": time_merge_100
        },
        {
            f"quantidade": thousand,
            "comparacoes_esperadas": int(thousand * math.log2(thousand)),
            "comparacoes_alcancadas": count_merge1000,
            "tempo": time_merge_1000
        },
        {
            f"quantidade": ten_thousand,
            "comparacoes_esperadas": int(ten_thousand * math.log2(ten_thousand)),
            "comparacoes_alcancadas": count_merge10000,
            "tempo": time_merge_10000
        },
        {
            f"quantidade": 100000,
            "comparacoes_esperadas": int(100000 * math.log2(100000)),
            "comparacoes_alcancadas": count_merge100000,
            "tempo": time_merge_100000
        }
    ]

    data2 = [{
        f"quantidade": ten,
        "comparacoes_esperadas": int(ten * ten),
        "comparacoes_alcancadas": int(count_insertion),
        "tempo": time_insertion_10
    },
        {
            f"quantidade": fifty,
            "comparacoes_esperadas": int(fifty * fifty),
            "comparacoes_alcancadas": int(count_insertion50),
            "tempo": time_insertion_50
        },
        {
            f"quantidade": hundred,
            "comparacoes_esperadas": int(hundred * hundred),
            "comparacoes_alcancadas": int(count_insertion100),
            "tempo": time_insertion_100
        },
        {
            f"quantidade": thousand,
            "comparacoes_esperadas": int(thousand * thousand),
            "comparacoes_alcancadas": int(count_insertion1000),
            "tempo": time_insertion_1000
        },
        {
            f"quantidade": ten_thousand,
            "comparacoes_esperadas": int(ten_thousand * ten_thousand),
            "comparacoes_alcancadas": int(count_insertion10000),
            "tempo": "0:00:07.893687"
        },
        {
            f"quantidade": 100000,
            "comparacoes_esperadas": 100000 * 100000,
            "comparacoes_alcancadas": 2980929777,
            "tempo": '00:36:00.02566'  # rodei separado, devido a limite de pilha
        }
    ]
    return data, data2


@app.route('/')
def index():
    # renderiza  a tabela de resultados
    data, data2 = table()
    return render_template('table.html', data=data, data2=data2)


if __name__ == '__main__':
    app.run()
