import argparse
import json


def process_values(values_json:dict)->dict:
    result = {}
    for value in values_json["values"]:
        result[value["id"]] = value["value"]
    return result



def recursive_fill(inp_json: dict, values: dict) -> None:
    if "tests" in inp_json:
        for test in inp_json["tests"]:
            recursive_fill(test, values)
    elif "values" in inp_json:
        for value in inp_json["values"]:
            recursive_fill(value, values)

    if "value" in inp_json:
        inp_json["value"] = values[inp_json["id"]]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("values_file", type=argparse.FileType("r"), help="values file")
    parser.add_argument("tests_file", type=argparse.FileType("r"), help="test file")
    parser.add_argument("report_file", type=argparse.FileType("w"), help="report file")
    args = parser.parse_args()
    values = json.load(args.values_file)
    tests = json.load(args.tests_file)
    recursive_fill(tests, process_values(values))
    json.dump(tests, args.report_file, ensure_ascii=False, indent=4)
