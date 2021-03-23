from collections import defaultdict


def diagonalsArranging(a):
    mat = a
    dict_map = defaultdict(lambda: "")
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            dict_map[len(mat) + j - i] += mat[i][j]
    result = list()
    for key in sorted(dict_map.keys()):
        temp = dict_map[key]
        if len(temp) <= len(mat):
            temp *= len(mat)
            temp = temp[:len(mat)]
            result.append([key, temp])
    ans = [res[0] for res in sorted(result, key=lambda x: [x[1], x[0]])]
    return ans


mat = [["a", "c", "a", "b", "b"],["c", "b", "a", "c", "b"],["a", "a", "e", "c", "b"],["b", "b", "d", "a", "g"],["a", "b", "e", "b", "a"]]
mat_ = [["b", "b"], ["c", "a"]]
print(diagonalsArranging(mat_))
