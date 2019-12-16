import pytest
from datetime import datetime

from app.Person import Person


class TestPerson:
    @pytest.mark.parametrize("last, first, gender, color, dob", [
        # Basic values
        ("Smith", "John", "Male", "Blue", "05/30/1980"),
        # Basic values, bad capitalization and spacing
        (" smith      ", "    JOhn   ", "MaLE", " blue ", " 05/30/1980 "),
        # Female gender
        ("Smith", "Jane", "Female", "Blue", "05/30/1980"),
    ])
    def test_init_person(self, last, first, gender, color, dob):
        person = Person(
            last_name=last,
            first_name=first,
            gender=gender,
            favorite_color=color,
            date_of_birth=dob
        )

        assert person.last_name == last.strip().capitalize()
        assert person.first_name == first.strip().capitalize()
        assert person.gender == gender.strip().capitalize()
        assert person.favorite_color == color.strip().lower()
        assert person.date_of_birth == datetime.strptime(dob.strip(), "%m/%d/%Y")

    @pytest.mark.parametrize("last, first, gender, color, dob, expected_failure_message", [
        ("   ", "Jane", "Male", "Blue", "05/30/1980", "Invalid last name"),
        ("Smith", "   ", "Female", "Blue", "05/30/1980", "Invalid first name"),
        ("Smith", "Jane", "Honda Civic", "Blue", "05/30/1980", "Gender must be of"),
        ("Smith", "Jane", "Female", "30000", "05/30/1980", "Invalid favorite color"),
    ])
    def test_init_bad_values_raise(self, last, first, gender, color, dob, expected_failure_message):
        with pytest.raises(ValueError) as person_error:
            person = Person(
                last_name=last,
                first_name=first,
                gender=gender,
                favorite_color=color,
                date_of_birth=dob
            )
            assert expected_failure_message in person_error

    def test_str_value(self):
        person = Person(
            first_name=" bob ",
            last_name="SMITH",
            gender="Male",
            favorite_color="RED",
            date_of_birth="01/25/1999"
        )

        assert str(person) == "Bob, Smith, Male, red, 01/25/1999"
