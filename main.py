DECIMAL_PRECISION: int = 2


# round the input and convert to an int if possible
def rnd(x: float) -> int | float:

    if x - int(x) < 10 ** (-DECIMAL_PRECISION):
        return int(x)

    else:
        return round(x, DECIMAL_PRECISION)


# get the square root of an input
def sqrt(x: float) -> int | float:
    x2: float = 1.0

    while abs(x - x2**2) > 10 ** (-DECIMAL_PRECISION):
        x2 = (x2 + x / x2) / 2

    return rnd(x2)


# get the cube root of an input
def cbrt(x: float) -> int | float:
    x3: float = 1.0

    while abs(x - x3**3) > 10 ** (-DECIMAL_PRECISION):
        x3 = (2 * x3 + x / (x3 * x3)) / 3

    return rnd(x3)


# get the nth root of an input
def rt(x: float, n: float) -> int | float:
    xn: float = 1.0

    while abs(x - xn**n) > 10 ** (-DECIMAL_PRECISION):
        xn = ((n - 1) * xn + x / (xn ** (n - 1))) / n

    return rnd(xn)


def main():
    x_input = input("ENTER A NUMBER: ")

    square = float(x_input)
    square_root = sqrt(square)
    print("SQUARE ROOT:", square_root)

    cube = float(x_input)
    cube_root = cbrt(cube)
    print("CUBE ROOT:", cube_root)

    power = float(x_input)
    n_input = input("ENTER A ROOT: ")
    n = int(n_input)
    root = rt(power, n)
    print(f"{n}TH ROOT:", root)


if __name__ == "__main__":
    main()
