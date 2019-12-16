from flask import Flask, make_response, request
import json
import os

from record_parser import parse_record_line, parse_record_file
from record_store import RecordStore

app = Flask(__name__)


@app.route("/healthcheck")
def healthcheck():
    return make_response("Healthy", 200)


@app.route("/records", methods=["POST"])
def create_record():
    # Reads entire request data as single record lien to be parsed
    # assumes request header of "Content-Type: text/html"
    parsing_successful, record = parse_record_line(request.get_data().decode("utf-8"))
    if not parsing_successful:
        return make_response(json.dumps(record), 400)

    RecordStore().add_record(record)

    return make_response(json.dumps({'record_status': 'added'}), 201)


@app.route("/records/gender", methods=["GET"])
def get_by_gender():
    # prompt 1
    # females before males, then last name ascending
    # e.g. (Lisa Ashcroft, Lisa Zulu, Dan Asher, Dan Weber)
    records = RecordStore().get_all_records(1)
    return make_response(json.dumps(records, default=str), 200)


@app.route("/records/birthdate", methods=["GET"])
def get_by_birthdate():
    # prompt 2
    # dob ascending (oldest person first)
    # e.g. (1960, 1970, 2010)
    records = RecordStore().get_all_records(2)
    return make_response(json.dumps(records, default=str), 200)


@app.route("/records/name", methods=["GET"])
def get_by_name():
    # prompt 3
    # last name descending
    # e.g. (Hank Zimmerman, Hank Martinez, Hank Bolt, Hank Asher)
    records = RecordStore().get_all_records(3)
    return make_response(json.dumps(records, default=str), 200)


if __name__ == "__main__":
    mock_data_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "mock_data")
    datafiles = [
        os.path.join(mock_data_dir, "MOCK_DATA_1.csv"),
        os.path.join(mock_data_dir, "MOCK_DATA_2.csv"),
        os.path.join(mock_data_dir, "MOCK_DATA_3.csv")
    ]
    bad_records = []
    for df in datafiles:
        df_records, df_bad_records = parse_record_file(df)
        bad_records.extend(df_bad_records)
        RecordStore().add_records(df_records)
    for bad_record in bad_records:
        print(f"BAD RECORD: f{bad_record}")

    app.run(host="0.0.0.0")
