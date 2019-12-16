from Person import Person
from record_store import RecordStore


# returns (True, Person) if record could be parsed
# returns (False, bad_record (dict)) if record is bad
def parse_record_line(record):
    if "|" in record:
        fields = [r.strip() for r in record.split("|")]
    elif "," in record:
        fields = [r.strip() for r in record.split(",")]
    elif " " in record:
        fields = [r.strip() for r in record.split(" ")]
    else:
        bad_record = {
            "bad_record": record,
            "error": "Unknown delimiter"
        }
        return False, bad_record
    if len(fields) != 5:
        bad_record = {
            "bad_record": record,
            "error": "Incorrect number of fields"
        }
        return False, bad_record

    try:
        person = Person(
            last_name=fields[0],
            first_name=fields[1],
            gender=fields[2],
            favorite_color=fields[3],
            date_of_birth=fields[4]
        )
        return True, person
    except ValueError as e:
        bad_record = {
            "bad_record": record,
            "error": str(e)
        }
        return False, bad_record


def parse_record_file(file_path):
    records = []
    bad_records = []
    with open(file_path, "r") as record_file:
        for record in record_file:
            success, record = parse_record_line(record)
            if success:
                records.append(record)
            else:
                bad_records.append(record)

    return records, bad_records


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser("Parses record files and returns them in sorted order.")
    parser.add_argument("-f", "--files", type=str, required=True,
                        help="Location of data records to parse. If multiple, use CSV.")
    parser.add_argument("-s", "--sort-choice", type=int,
                        choices=[1, 2, 3],
                        default=1,
                        help="[1] (default) females before males, then last name ascending, e.g. (Lisa Ashcroft, Lisa Zulu, Dan Asher, Dan Weber). " +
                             "[2] dob ascending (oldest person first), e.g. (1960, 1970, 2010). " +
                             "[3] last name descending, (Hank Zimmerman, Hank Martinez, Hank Bolt, Hank Asher).")

    args = parser.parse_args()
    record_files = args.files.split(',')

    record_store = RecordStore()
    bad_records = []
    for record_file in record_files:
        rf_good, rf_bad = parse_record_file(record_file)
        record_store.add_records(rf_good)
        bad_records.extend(rf_bad)

    good_records = record_store.get_all_records(args.sort_choice or 1)

    for good_record in good_records:
        print(f"RECORD: {good_record}")
    for bad_record in bad_records:
        print(f"BAD RECORD: {bad_record}")
