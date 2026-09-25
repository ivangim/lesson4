import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

#Принимает на вход текст и удаляет пробелы в начале, если они есть

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    (" 04 апреля 2023", "04 апреля 2023"),
    (" Тест", "Тест"),
    ("/test", "/test")
    ])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    (" 123 ", "123 "),
    ("   ", ""),
    (" Test 1", "Test 1")
    ])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected

#Возвращает `True`, если строка содержит искомый символ
 #       и `False` - если нет

@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Skypro", "S", True),
    ("Skypro", "U", False),
    (" ", "A", False)
])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("2 мая", "2", True),
    ("Привет !", "_", False),
    (" ", "F", False),
])
def test_contains_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


#Удаляет все подстроки из переданной строки

@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("SkyPro", "S", "kyPro"),
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("4567", "6", "457"),
    ("", "", ""),
    ("aaaa", "aa", ""),
])
def test_delete_sybol_negative(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected