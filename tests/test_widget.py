from src.widget import date_from_string


def test_correct_data():
    assert date_from_string("2018-07-11T02:26:18.671407") == "11.07.2018"


# def test_up_first_for_empty():
#     assert up_first('') == ''
