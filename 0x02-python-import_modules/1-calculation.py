from calculator_1 import add, sub, mul, div


def main():
    a = 10
    b = 5

    result_add = add(a, b)
    print(f"{a} + {b} = {result_add}")

    result_sub = sub(a, b)
    print(f"{a} - {b} = {result_sub}")

    result_mul = mul(a, b)
    print(f"{a} * {b} = {result_mul}")

    result_div = div(a, b)
    print(f"{a} / {b} = {result_div}")


if __name__ == "__main__":
    main()
