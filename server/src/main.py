from network_module import run_server

def sum(a, b):
    return a + b


def main():
    a = 2
    b = 2
    print(f'sum({a}, {b}) = {sum(a, b)}')

    run_server()


if __name__ == "__main__":
    main()
