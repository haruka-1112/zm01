import datetime

import typer

from zm01 import mathtools
from zm01 import demo
app = typer.Typer()


@app.callback()
def callback():
    """
    A Collection of Useful Commands
    """


@app.command()
def now():
    """
    Show local date and time
    """
    today = datetime.datetime.today()
    typer.echo(today.strftime('%A, %B %d, %Y'))


@app.command()
def gcd(x: int, y: int):
    """
    Greatest Common Divisor
    """
    typer.echo(mathtools.gcd(x, y))



import webbrowser
import pandas as pd

@app.command()
def train():
   data = {
       "路線名": ["南海高野線", "阪和線","大阪環状線","御堂筋線"],
       "情報種別": ["運行情報", "運行情報","運行情報","運行情報"],
       "URL": ["https://transit.yahoo.co.jp/diainfo/346/0", "https://transit.yahoo.co.jp/diainfo/274/0","https://transit.yahoo.co.jp/diainfo/263/0","https://transit.yahoo.co.jp/diainfo/321/0"]
   }
   df = pd.DataFrame(data)


   RED = '\033[31m'
   RESET = '\033[0m'

   print("+" + "-"*18 + "+" + "-"*10 + "+" + "-"*50 + "+")
   print(f"| {'路線名':<16} | {'情報種別':<8} | {'URL':<48} |")
   print("+" + "-"*18 + "+" + "-"*10 + "+" + "-"*50 + "+")
     
   for _, row in df.iterrows():
        colored_route = f"{RED}{row['路線名']}{RESET}"
        print(f"| {colored_route:<16} | {row['情報種別']:<8} | {row['URL']:<48} |")
     
   print("+" + "-"*18 + "+" + "-"*10 + "+" + "-"*50 + "+")


   
   
  