def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    # ここから記述

    # 探索するインデックスの範囲を示す変数
    left_index: int = 0
    right_index: int = len(sorted_array) - 1

    # 探索部分
    # left_indexがright_indexより大きくなるまで繰り返す
    while left_index <= right_index:
        # 範囲の中間のindexとその値を取得
        middle_index: int = (left_index + right_index) // 2
        middle_value: int = sorted_array[middle_index]

        # 探索対象を発見 => middle_indexを返却
        if target_number == middle_value:
            return middle_index
        # 探索対象は中間の値より小さい => 範囲を左半分にする
        elif target_number < middle_value:
            right_index = middle_index - 1
        # 探索対象は中間の値より大きい => 範囲を右半分にする
        elif target_number > middle_value:
            left_index = middle_index + 1

    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()