from bank import value


def main():
    test_bank()

def test_bank():
    assert value("Hello") == 0

    assert value("Hello, Newman") == 0

    assert value("How you doing?") == 20


    assert value("What's happening?") == 100


if __name__ == "__main__":
    main()
