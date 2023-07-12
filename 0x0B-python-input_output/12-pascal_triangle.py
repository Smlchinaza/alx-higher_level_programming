def pascal_triangle(n):
    """Generate Pascal's triangle of n"""
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                # Use the values from the previous row to calculate the current value
                prev_row = triangle[i - 1]
                value = prev_row[j - 1] + prev_row[j]
                row.append(value)
        triangle.append(row)

    return triangle
