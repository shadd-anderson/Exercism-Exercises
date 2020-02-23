def saddle_points(matrix):
    if not valid_matrix(matrix):
        raise ValueError("Not a valid matrix!")
    elif len(matrix) == 0:
        return matrix

    points = []
    columns = [[row[x] for row in matrix] for x in range(len(matrix[0]))]
    for row_index, row in enumerate(matrix):
        for column_index, column in enumerate(row):
            if max(row) == row[column_index] == min(columns[column_index]):
                points.append({"row": row_index + 1, "column": column_index + 1})
    return points


def valid_matrix(matrix):
    return len(set(len(row) for row in matrix)) <= 1
