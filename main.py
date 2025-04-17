import tkinter as tk
from data_loader import HistoryDataLoader
from history_ui import HistoryUI
from add import Add

# データの読み込み
loader = HistoryDataLoader()
japan_data = loader.load_japan('japan.csv')
world_data = loader.load_world('world.csv')

# TkinterのUIセットアップ
root = tk.Tk()
root.title('日本史・世界史比較プログラム')

# UIクラスのインスタンス化
ui = HistoryUI(root, japan_data, world_data)

# メインループ(GUIアプリを表示させたままにsる)
root.mainloop()
