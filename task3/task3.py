import argparse
import json

def recursive_fill(inp_json, values):
    if "tests" in inp_json:
        for test in inp_json["tests"]:
            recursive_fill(test, values)
    elif "values" in inp_json:
        for value in inp_json['values']:
            recursive_fill(value, values)

    if "value" in inp_json:
        for value_case in values['values']:
            if value_case['id'] == inp_json['id']:
                inp_json['value'] = value_case['value']


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "values_path", type=argparse.FileType("r"), help="values file"
    )
    parser.add_argument(
        "tests_path", type=argparse.FileType("r"), help="test file"
    )
    parser.add_argument(
        "report_path", type=argparse.FileType("w"), help="report file"
    )
    args = parser.parse_args()
    values = json.load(args.values_path)
    tests = json.load(args.tests_path)
    recursive_fill(tests, values)
    json.dump(tests, args.report_path, ensure_ascii=False, indent=4)

