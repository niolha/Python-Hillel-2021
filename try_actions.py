def squares(start, end):
    squares = []
    for value in range(start, end + 1):
        square = value ** 2
        squares.append(square)
    return squares


if "__main__" == __name__:
    print(squares(1, 11))
