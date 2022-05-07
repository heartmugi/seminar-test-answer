def main():
    #ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]

def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]

    # ここから記述

    # 探索範囲
    left_limit: int = 0
    right_limit: int = len(array)

    # 左右それぞれの探索位置を示す変数
    left_index: int = 0
    right_index: int = len(array) - 1

    # 基準値が最小値の場合，それを除いた配列を考える
    if pivot == min(array):
        left_limit += 1
        left_index += 1
        pivot = array[1]

    # 基準値を参考に2つの値を探索し，交換する部分
    while left_index < right_index:
        # 基準値以上の値のindexを探索
        while left_index < right_limit and pivot > array[left_index]:
            left_index += 1
        # 基準値未満の値のindexを探索
        while right_index >= left_limit and pivot <= array[right_index]:
            right_index -= 1

        # left_indexがright_indexを超えていない場合，値を交換
        if left_index < right_index:
            array[left_index], array[right_index] = array[right_index], array[left_index]
        # 超えている場合，探索を終了
        else:
            break
    
    # 基準値未満のグループと基準値以上のグループ，それぞれに対して同様の処理を再帰的に繰り返す
    # 要素が一つもない場合，この処理は行わない
    if len(array[:left_index]) > 0:
        array[:left_index] = sort(array[:left_index])       # 基準値未満のグループ
    if len(array[left_index:]) > 0:
        array[left_index:] = sort(array[left_index:])       # 基準値以上のグループ

    return array

    # ここまで記述

if __name__ == '__main__':
    main()