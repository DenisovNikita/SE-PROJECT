def sum(a: int, b: int) -> int:
    """Sum of two integers.

    Args:
        a (int): First value.
        b (int): Second value.

    Returns:
        int: The return value.

    """
    return a + b


def main() -> None:
    """Calls `sum` function and print result.

    Returns:
        None

    """
    a = 2
    b = 2
    print(f'sum({a}, {b}) = {sum(a, b)}')


if __name__ == "__main__":
    main()
