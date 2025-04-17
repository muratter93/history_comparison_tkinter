# 参考 https://qiita.com/yoshi-kin/items/26fa4194ee7a726d685c
# [Python] 特殊メソッドまとめ

class Add:

    # addメソッド
    def __init__(self, x):
        self.x = x

    def __iadd__(self, other):
        self.x += other.x
        return self