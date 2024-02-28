def solution(arr1, arr2):
    # 행렬의 곱셈값을 저장할 영행렬을 먼저 만든다
    two_arrays = [[0 for j in range(len(arr2[0]))]for i in range(len(arr1))]

    # 3개의 싸이클을 만듬
    # 행렬의 곱이 가능하려면 값이 같은 행과 열이 존재
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr1[0])):
                two_arrays[i][j] += arr1[i][k] * arr2[k][j]

    return two_arrays

if __name__ == '__main__':
    print(solution([[1, 4], [3, 2], [4, 1]],[[3, 3], [3, 3],[3, 3], [3, 3]]))