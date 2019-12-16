import pytest
from mock import mock_open, patch

from app.Person import Person
from app.record_parser import parse_record_line, parse_record_file


class TestRecordParser:
    @pytest.mark.parametrize("input_line, last_name, first_name, gender, favorite_color, date_of_birth", [
        ("Smith | Bob |male| blue | 10/20/2002", "Smith", "Bob", "Male", "blue", "10/20/2002"),
        ("Smith, Bob, male,blue, 10/20/2002", "Smith", "Bob", "Male", "blue", "10/20/2002"),
        ("Smith Betty female Blue 10/20/2002", "Smith", "Betty", "Female", "blue", "10/20/2002")
    ])
    def test_parse_record_line(self, input_line, last_name, first_name, gender, favorite_color, date_of_birth):
        success, record = parse_record_line(input_line)

        assert success
        assert record.last_name == last_name
        assert record.first_name == first_name
        assert record.gender == gender
        assert record.favorite_color == favorite_color
        assert record.date_of_birth.strftime("%m/%d/%Y") == date_of_birth


    @pytest.mark.parametrize("input_line, expected_error_message", [
        ("SmithBobMaleBlue10/20/2002", "Unknown delimiter"),
        ("Smith|Bob", "Incorrect number of fields"),
        ("Smith | Bob |male| blue | 10/20/2002 | Bob", "Incorrect number of fields"),
        ("3333 | Bob |male| blue | 10/20/2002", "Invalid last name 3333"),
        ("Smith | $ |male| blue | 10/20/2002", "Invalid first name $"),
        ("Smith Bob toyota blue 10/20/2002", "Gender must be \"Male\" or \"Female\""),
        ("Smith | Bob |male| blue | Jan 5th, 1985", "Date of birth must be in MM/DD/YYYY format")
    ])
    def test_parse_bad_delimiters(self, input_line, expected_error_message):
        success, record = parse_record_line(input_line)

        assert not success

        assert isinstance(record, dict)
        assert record == {
            "bad_record": input_line,
            "error": expected_error_message
        }

    @patch("app.record_parser.parse_record_line")
    def test_parse_record_file_returns_good_and_bad(self, mock_parse_record_line):
        file_path = "path/to/records.csv"

        def parse_logic(record):
            if "good" in record:
                return True, "happy record object :)"
            return False, "bad record object :("
        mock_parse_record_line.side_effect = parse_logic

        records = [
            "good record",
            "2nd good record",
            "bad record :(",
            "3rd good record"
        ]
        mock_record_file = mock_open(read_data="\n".join(records))

        with patch("app.record_parser.open", mock_record_file):
            good_records, bad_records = parse_record_file(file_path)

        assert len(good_records) == 3
        assert good_records[0] == "happy record object :)"
        assert good_records[1] == "happy record object :)"
        assert good_records[2] == "happy record object :)"
        assert len(bad_records) == 1
        assert bad_records[0] == "bad record object :("

