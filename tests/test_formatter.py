import pytest
from src.format_users import filter_users

test_data = {
    "results":[
        {
            "name":{"first":"After", "last":"2000"},
            "dob":{"date":"2005-01-01T00:00:00.000Z"}
        },
        {
            "name":{"first":"Before", "last":"2000"},
            "dob":{"date":"1999-12-31T00:00:00Z"}
        },
        {
            "name": {"first": "James", "last": "Bond"},
            "dob": {"date": "1950-10-29T00:00:00Z"}
        }
    ]
}

def test_with_empty_results():
    test_data = {
        "results":[]
    }
    result = filter_users(test_data)
    assert result == []

def test_return_list():
    result=filter_users(test_data)
    assert isinstance(result, list)

def test_filter_out_based_on_birthyear():
    result=filter_users(test_data)
    assert "After 2000" not in result
    assert "Before 2000" in result
    assert "James Bond" in result

def test_full_name_format():
    # testing that full_name returns back exactly first_name + " " + last_name"
    result=filter_users(test_data)
    assert "Bond James" not in result
    assert "James Bond" in result