import pytest
from app.restore_names import restore_names


@pytest.fixture
def users_incoming() -> list:
    return [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]


@pytest.fixture
def expected() -> list:
    return [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]


def test_restore_names(users_incoming: list,
                       expected: list) -> None:
    restore_names(users_incoming)

    assert users_incoming == expected
