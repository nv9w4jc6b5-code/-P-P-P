def divide(a, b):
    """Делит a на b. Бросает ZeroDivisionError при b == 0."""
    if b == 0:
        raise ZeroDivisionError("Деление на ноль")
    return a / b


def multiply(a, b):
    """Умножает a на b."""
    return a * b


def test_divide():
    assert divide(10, 2) == 5
    assert divide(-9, 3) == -3
    assert divide(1, 4) == 0.25
    try:
        divide(1, 0)
    except ZeroDivisionError:
        pass
    else:
        raise AssertionError("Ожидалось ZeroDivisionError")


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-3, 4) == -12
    assert multiply(-3, -4) == 12
    assert multiply(0, 5) == 0
    assert multiply(5, 0) == 0
    assert multiply(1.5, 2.5) == 3.75


if __name__ == "__main__":
    test_divide()
    test_multiply()
    print("Все проверки пройдены")
