import csv

# 参考 PythonでCSVファイルを読み込み・書き込み（入力・出力）
# https://note.nkmk.me/python-csv-reader-writer/#csvdictreader

class HistoryDataLoader:

    # 日本の歴史データを読み込むメソッド
    def load_japan(self, filename):
        event = {}
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    event[row['年代']] = (row['出来事'], row['URL'])
        except FileNotFoundError:
            print('エラー: 日本史csvファイルが見つかりません。')
        return event

    # 世界の歴史データを読み込むメソッド
    def load_world(self, filename):
        event = {}
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    key = (row['年代'], row['国'])
                    event[key] = (row['出来事'], row['URL'])
        except FileNotFoundError:
            print('エラー: 世界史csvファイルが見つかりません。')
        return event
