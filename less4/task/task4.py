import time


def insert_sort(lists):
    length = len(lists)
    for i in range(1, length):
        key = lists[i]
        j = i - 1
        while j >= 0:
            if lists[j] > key:
                lists[j + 1] = lists[j]
                lists[j] = key
            j = j - 1
    return lists


if __name__ == "__main__":
    lists = [3, 4, 2, 8, 9, 5, 1]
    print("排序前序列为："),
    for i in lists:
        print(i, end=' ')
    print("\n排序后结果为："),
    for i in insert_sort(lists):
        print(i, end=' ')
