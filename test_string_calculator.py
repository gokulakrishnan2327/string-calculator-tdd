from string_calculator import StringCalculator

def test_empty_string():
    calc = StringCalculator()
    assert calc.add("") == 0

def test_single_number():
    calc = StringCalculator()
    assert calc.add("1") == 1

def test_two_numbers():
    calc = StringCalculator()
    assert calc.add("1,5") == 6

def test_multiple_numbers():
    calc = StringCalculator()
    assert calc.add("1,2,3,4") == 10

def test_newline_between_numbers():
    calc = StringCalculator()
    assert calc.add("1\n2,3") == 6

def test_custom_delimiter():
    calc = StringCalculator()
    assert calc.add("//;\n1;2") == 3

def test_negative_numbers_exception():
    calc = StringCalculator()
    try:
        calc.add("1,-2,-3")
    except Exception as e:
        assert str(e) == "Negative numbers not allowed: -2, -3"
