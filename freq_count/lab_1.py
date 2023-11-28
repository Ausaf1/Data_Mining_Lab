import re
from rich.console import Console
from rich.table import Table


def freq():
    table = Table(title="freq count")
    f = open(r'D:/data_mining_lab/freq_count/input.txt', 'r')
    d = {}
    for line in f:
        words = line.split()
        words = [re.sub(r'[.,!?:;(){}\[\]"\']', '', word) for word in words]
        for word in words:
            if word in d:
                d[word] += 1
            else:
                d[word] = 1
    d = sorted(d.items(), key=lambda x: x[1])
    f1 = open(r'D:/data_mining_lab/freq_count/output.txt', 'w')
    column_names = ["Word", "Frequency"]
    table.add_column(column_names[0])
    table.add_column(column_names[1])
    for word, freq in d:
        table.add_row(word, str(freq))
    console = Console()
    console.print(table)
    f1.write(str(d))
    f.close()


freq()
