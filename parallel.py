import threading
from scraping import Scraping

# 参考 https://zenn.dev/nekoallergy/articles/py-advance-threading-01
# 【Python】 並列処理を理解しよう 　【threadingの使い方 01】

class Parallel:

    def __init__(self, japan_data, world_data, text_area_japan, text_area_world):
        self.japan_data = japan_data
        self.world_data = world_data
        self.text_area_japan = text_area_japan
        self.text_area_world = text_area_world

    # 日本の歴史を表示(並列処理)
    def display_selected_japan(self, choice):
        threading.Thread(target=self._display_japan, args=(choice,)).start()

    def _display_japan(self, choice):
        display = Scraping(self.text_area_japan)
        display.fetch(choice, self.japan_data, 'heading')

    # 世界の歴史を表示(並列処理)
    def display_selected_world(self, choice, choice_country):
        threading.Thread(target=self._display_world, args=(choice, choice_country)).start()

    def _display_world(self, choice, choice_country):
        display = Scraping(self.text_area_world)
        key = (choice, choice_country)
        display.fetch(key, self.world_data, 'heading')
