from typing import Union, Callable
from rich.console import Console
from rich.panel import Panel
from rich.json import JSON
from .utils import ResponseType, status_detail
from requests.models import Response
import time

CONSOLE = Console()

def find_response_type(res: Response):
    # Find the response type based on the status code
    if res.status_code >= 200 and res.status_code < 300:
        return ResponseType.SUCCESS
    elif res.status_code >= 400 and res.status_code < 500:
        return ResponseType.ERROR
    else:
        return ResponseType.WARNING


def print_response(res: Response, res_type: Union[Callable, ResponseType] = find_response_type, show_headers: bool=False):
    if callable(res_type):
        res_type = res_type(res)
    
    if show_headers:
        formatted_headers = "\n".join([f"[bold blue]{key}[/bold blue]: [green]{value}[/green]" for key, value in res.headers.items()])
    else:
        formatted_headers = None
        
    title = f"HTTP: {res.status_code} ({status_detail(res.status_code)})"
    # print the response JSON if the 'Content-Type' == 'application/json' else just print the 'Content-Type'
    if 'application/json' in res.headers.get('Content-Type', ''):
        content = JSON.from_data(res.json())
    else:
        content = res.headers.get('Content-Type', 'No Content-Type')
    
    content_panel = Panel(
        content,
        title="Content",
        border_style=res_type.border_style,
        padding=(1, 2),
    )
    
    if formatted_headers:
        main_panel_content = f"{formatted_headers}\n\n{content_panel}"
    else:
        main_panel_content = content_panel
    
    CONSOLE.print(
        Panel(
            main_panel_content,
            title=title,
            border_style=res_type.border_style,
            padding=(1, 2),
        )
    )
    

def show_loader(label: str = "Loading", completion_message: str = "Completed") -> Callable:
    def inner(task: Callable):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            with CONSOLE.status(f"[bold green]{label}") as status:
                result = task(*args, **kwargs)
            elapsed_time = time.time() - start_time
            CONSOLE.log(f"[green]{completion_message} in {elapsed_time:.2f} seconds")
            return result
        return wrapper
    return inner