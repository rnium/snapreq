# from rich.console import Console
# from rich.panel import Panel
# from rich.json import JSON
# from rich import print_json
# from console.logger import show_loader, print_response
# from console.utils import ResponseType
# import requests
# import time


# url = "https://jsonplaceholder.typicode.com/posts/1"

# @show_loader("Fetching data", f'Fetched [cyan]{url}[/cyan]')
# def fetchit():
#     res = requests.get(url)
#     return res


# res = fetchit()
# print_response(res, show_headers=True)
from rich.panel import Panel
from rich.layout import Layout
from rich.console import Console

layout = Layout(name="root")

inner_panel_1 = Panel("This is the first inner panel", title="Inner Panel 1")
inner_panel_2 = Panel("[small]This is the second inner panel[/small]", title="Inner Panel 2")

layout.split_row(
    Layout(inner_panel_1, ratio=2),
    Layout(inner_panel_2, ratio=1)
)

console = Console()
console.print(layout)

