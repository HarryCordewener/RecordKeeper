import pytest

from app.Person import Person
from app.record_store import RecordStore


class TestRecordStore:
    @pytest.fixture(autouse=True)
    def setup(self):
        RecordStore._records = []

    def test_sort_1(self):
        record_store = RecordStore()

        people = [
            Person(gender='Male', last_name='D', first_name='x', favorite_color='x', date_of_birth='01/01/2000'),
            Person(gender='Male', last_name='A', first_name='x', favorite_color='x', date_of_birth='01/01/2000'),
            Person(gender='Female', last_name='Y', first_name='x', favorite_color='x', date_of_birth='01/01/2000'),
            Person(gender='Female', last_name='Z', first_name='x', favorite_color='x', date_of_birth='01/01/2000')
        ]
        record_store.add_records(people)

        sorted_records = record_store.get_all_records(1)

        assert sorted_records[0] == people[2]
        assert sorted_records[1] == people[3]
        assert sorted_records[2] == people[1]
        assert sorted_records[3] == people[0]

    def test_sort_2(self):
        record_store = RecordStore()

        people = [
            Person(last_name='x', first_name='x', gender='Male', favorite_color='x', date_of_birth='01/01/2000'),
            Person(last_name='x', first_name='x', gender='Male', favorite_color='x', date_of_birth='01/01/1990'),
            Person(last_name='x', first_name='x', gender='Male', favorite_color='x', date_of_birth='01/01/1960'),
            Person(last_name='x', first_name='x', gender='Male', favorite_color='x', date_of_birth='01/01/2002')
        ]
        record_store.add_records(people)

        sorted_records = record_store.get_all_records(2)

        assert sorted_records[0] == people[2]
        assert sorted_records[1] == people[1]
        assert sorted_records[2] == people[0]
        assert sorted_records[3] == people[3]

    def test_sort_3(self):
        record_store = RecordStore()

        people = [
            Person(last_name='B', first_name='x', gender='Male', favorite_color='x', date_of_birth='01/01/2000'),
            Person(last_name='A', first_name='x', gender='Male', favorite_color='x', date_of_birth='01/01/2000'),
            Person(last_name='C', first_name='x', gender='Male', favorite_color='x', date_of_birth='01/01/2000'),
            Person(last_name='D', first_name='x', gender='Male', favorite_color='x', date_of_birth='01/01/2000')
        ]
        record_store.add_records(people)

        sorted_records = record_store.get_all_records(3)

        assert sorted_records[0] == people[3]
        assert sorted_records[1] == people[2]
        assert sorted_records[2] == people[0]
        assert sorted_records[3] == people[1]
