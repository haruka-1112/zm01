import pandas as pd
import requests
from bs4 import BeautifulSoup
import datetime

import typer

from zm01 import mathtools
from zm01 import demo
app = typer.Typer()
@app.command()
def train():
    """関西の主要鉄道路線の運行情報を表示"""
    
    data = {
        "路線名": ["南海高野線", "阪和線", "大阪環状線", "御堂筋線"],
        "情報種別": ["運行情報", "運行情報", "運行情報", "運行情報"],
        "URL": [
            "https://transit.yahoo.co.jp/diainfo/346/0",
            "https://transit.yahoo.co.jp/diainfo/274/0",
            "https://transit.yahoo.co.jp/diainfo/263/0",
            "https://transit.yahoo.co.jp/diainfo/321/0"
        ]
    }
    df = pd.DataFrame(data)
    

    
    def get_train_status(url):
        """指定されたURLから運行状況を取得"""
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # 運行情報を探す（Yahoo路線情報の構造に基づく）
            status_elem = soup.find('div', class_='trouble')
            if status_elem:
                status_text = status_elem.get_text(strip=True)
                if '遅延' in status_text or '運転見合わせ' in status_text:
                    return "● 運行に支障"
                else:
                    return "△ 情報あり"
            else:
                return "○ 正常運行"
                
        except Exception as e:
            return "? 取得失敗"
    
    # 運行状況をチェックするかどうかの選択
    check_status = input("運行状況をチェックしますか？ (y/n): ").lower() == 'y'
    
    if check_status:
        print("運行状況を取得中...")
        print("+" + "-"*18 + "+" + "-"*16 + "+" + "-"*50 + "+")
        print(f"| {'路線名':<16} | {'運行状況':<14} | {'URL':<48} |")
        print("+" + "-"*18 + "+" + "-"*16 + "+" + "-"*50 + "+")
        
        for _, row in df.iterrows():
            status = get_train_status(row['URL'])
            print(f"| {row['路線名']:<16} | {status:<14} | {row['URL']:<48} |")
        
        print("+" + "-"*18 + "+" + "-"*16 + "+" + "-"*50 + "+")
    else:
        # 元のテーブル表示
        print("+" + "-"*18 + "+" + "-"*10 + "+" + "-"*50 + "+")
        print(f"| {'路線名':<16} | {'情報種別':<8} | {'URL':<48} |")
        print("+" + "-"*18 + "+" + "-"*10 + "+" + "-"*50 + "+")
              
        for _, row in df.iterrows():
            print(f"| {row['路線名']:<16} | {row['情報種別']:<8} | {row['URL']:<48} |")
            
        print("+" + "-"*18 + "+" + "-"*10 + "+" + "-"*50 + "+")

if __name__ == "__main__":
    train()



##

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



   