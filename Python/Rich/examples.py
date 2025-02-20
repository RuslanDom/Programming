from rich import print

print("[bold red]Ошибка![/bold red] Что то пошло не так... ")
print("Hello, [bold magenta]World[/bold magenta]!", ":vampire:", locals())

from rich.table import Table
from rich.console import Console

console = Console()

table = Table(title="Топ криптовалют")

table.add_column("Название", style='cyan', no_wrap=True)
table.add_column("Цена", style="green")
table.add_column("Изменение", style="red")

table.add_row("Bitcoin", "$96,000", "-1.2%")
table.add_row("Etherium", "$2,900", "+0.5%")
table.add_row("Solana", "$192", "+3.8%")

console.print(table)

from rich.progress import track
import time

for step in track(range(10), description = "Загрузка...",):
    time.sleep(0.5)
    

