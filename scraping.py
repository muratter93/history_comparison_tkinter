import requests
import bs4
import tkinter as tk

# 参考 https://qiita.com/Moh_no/items/a835f77b6b4e3972fbbe
# Pythonで手軽に始めるWebスクレイピング

# 参考 https://qiita.com/d_kvn/items/5da7f5cdfc8200172a39
# Python API通信時の例外処理

# スクレイピングクラス
class Scraping:
    
    # テキストエリアを初期化
    def __init__(self, text_area):
        self.text_area = text_area
    
    # 選択された情報を取得し、表示するメソッド
    def fetch(self, choice, data_source, tag):

        # データソースから選択された情報を取得
        if choice in data_source:
            text, url = data_source[choice]
            
        # データが見つからない場合のデフォルトURLとメッセージ
        else:
            url = 'https://www.weblio.jp/content/歴史'
            text = 'データが見つかりませんでした。'

        # Webからデータを取得（Webスクレイピング)
        try:
            response = requests.get(url)
            html = response.text
            soup = bs4.BeautifulSoup(html, 'html.parser')

            # h2からタイトルを取得
            h2 = soup.find('h2')
            h2_text = h2.text if h2 else 'タイトル情報なし'

            # pの内容を抽出
            paragraph = soup.find_all('p')
            paragraph2 = [
                para.text for para in paragraph 
                if not any(kw in para.text for kw in ['カテゴリ一覧', '出典: フリー百科事典『ウィキペディア（Wikipedia）』', '読み方：', '辞書ショートカット'])
            ]

            # 結果のテキストを生成
            result_text = f'\n\n{h2_text}\n\n' + '\n\n'.join(paragraph2[:2])

            # テキストエリアを更新
            self.text_area.config(state=tk.NORMAL)
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, text, tag)  # 選択した情報を挿入
            self.text_area.insert(tk.END, result_text)  # 取得したデータを挿入
            self.text_area.config(state=tk.DISABLED)

        # エラーが発生した場合の処理
        except requests.exceptions.RequestException:
            self.text_area.config(state=tk.NORMAL)
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, 'エラーが発生しました。インターネットの接続を確認してください。')
            self.text_area.config(state=tk.DISABLED)
