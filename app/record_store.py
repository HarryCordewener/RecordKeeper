# Provides an in memory datastore of the records
# If this app were expanded to include a persistence layer, it would be interfaced here


class RecordStore:
    _records = []

    def add_record(self, person):
        RecordStore._records.append(person)

    def add_records(self, persons):
        for person in persons:
            self.add_record(person)

    # Returns a new list, where the records are sorted by sort choice
    def get_all_records(self, sort_choice=1):
        reverse_sort = False
        if sort_choice == 1:
            sort_key = lambda p: (p.gender, p.last_name)
        elif sort_choice == 2:
            sort_key = lambda p: p.date_of_birth
        elif sort_choice == 3:
            sort_key = lambda p: p.last_name
            reverse_sort = True
        else:
            raise ValueError("sort choice must be 1, 2, or 3")

        return sorted(RecordStore._records, key=sort_key, reverse=reverse_sort)
