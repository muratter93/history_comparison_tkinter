import tkinter as tk
from tkinter import scrolledtext
from parallel import Parallel

# 参考 PythonのTkinterを使ってみる
# https://qiita.com/nnahito/items/ad1428a30738b3d93762

# ユーザーインターフェースを作成するクラス
class HistoryUI:

    # 初期化メソッド
    def __init__(self, root, japan_data, world_data):

        self.root = root
        self.japan_data = japan_data  # 日本の歴史データ
        self.world_data = world_data    # 世界の歴史データ
        self.create_widgets()            # ウィジェットを作成

    def create_widgets(self):
        # 日本のドロップダウンメニューの作成
        options_japan = ['1世紀', '2世紀', '3世紀', '4世紀', '5世紀', '6世紀', '7世紀', '8世紀', '9世紀', '10世紀', '11世紀', '12世紀', '13世紀', '14世紀', '15世紀', '16世紀', '17世紀', '18世紀', '1800年~', '1850年~', '1900年~', '1925年~', '1950年~', '1975年~', '2000年~']
        self.variable_japan = tk.StringVar(self.root)
        self.variable_japan.set(options_japan[0])  # デフォルト選択
        dropdown_japan = tk.OptionMenu(self.root, self.variable_japan, *options_japan, command=self.display_japan)
        dropdown_japan.pack(pady=10)

        # 日本のテキストエリアの作成
        self.text_area_japan = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=80, height=13)
        self.text_area_japan.pack(padx=10, pady=10)
        self.text_area_japan.config(state=tk.NORMAL)
        self.text_area_japan.insert(tk.END, '日本史\n', 'heading') # 初期表示
        self.text_area_japan.config(state=tk.DISABLED)
        self.text_area_japan.tag_config('heading', font=('Helvetica', 13, 'bold')) 

        # 世界のドロップダウンメニューの作成
        options_world = ['ヨーロッパ', '中東・アフリカ', '中国', 'アメリカ・ロシア']
        self.variable_world = tk.StringVar(self.root)
        self.variable_world.set(options_world[0])  # デフォルト選択
        dropdown_world = tk.OptionMenu(self.root, self.variable_world, *options_world, command=self.display_world)
        dropdown_world.pack(pady=10)

        # 世界のテキストエリアの作成
        self.text_area_world = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=80, height=13)
        self.text_area_world.pack(padx=10, pady=10)
        self.text_area_world.config(state=tk.NORMAL)
        self.text_area_world.insert(tk.END, '世界史\n', 'heading')  # 初期表示
        self.text_area_world.config(state=tk.DISABLED)
        self.text_area_world.tag_config('heading', font=('Helvetica', 13, 'bold'))

        # 終了ボタンの作成
        close_button = tk.Button(self.root, text='終了', command=self.root.quit)
        close_button.pack(pady=10)

        # DisplayManagerの作成
        self.display_manager = Parallel(self.japan_data, self.world_data, self.text_area_japan, self.text_area_world)

    def display_japan(self, choice):
        # 日本の歴史情報を表示するメソッド
        self.display_manager.display_selected_japan(choice)

    def display_world(self, choice_country):
        # 世界の歴史情報を表示するメソッド
        choice = self.variable_japan.get()  # 現在の日本の選択を取得
        self.display_manager.display_selected_world(choice, choice_country)
