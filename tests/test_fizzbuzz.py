from fizzbuzz import fizzbuzz

def test_returns_number_as_string():
    assert fizzbuzz ( 1 ) == "1"


def test_multiple_of_three_returns_fizz():
    assert fizzbuzz ( 3 ) == "Fizz"


def test_multiple_of_five_returns_buzz():
    assert fizzbuzz ( 5 ) == "Buzz"


def test_multiple_of_three_and_five_returns_fizzbuzz():
    assert fizzbuzz ( 15 ) == "FizzBuzz"
