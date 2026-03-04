import json


def parse_line(line: str) -> dict:
    '''Parsing funrion'''
    date, level, message = line.split("|")
    data = {"date": date, "level": level}
    
    for pair in message.split():
        if "=" in pair:
            key, value = pair.split("=")
            data[key] = int(value) if value.isdigit() else value
            
    return data


def to_json(raw_logs: list, filepath: str) -> list:
    '''Func to convert to json'''
    parsed_logs = [parse_line(line) for line in raw_logs]
    
    if filepath:
        with open(filepath, "w") as f:
            json.dump(parsed_logs, f, indent=4, ensure_ascii=False)
            
    return parsed_logs


def filter_logs(logs: list, **kwargs) -> list:
    '''Function that filters logs obviously'''
    return [log for log in logs if all(log.get(k) == v for k, v in kwargs.items())]


def count_by_key(logs: list, key: str) -> dict:
    '''Func to count logs that satisfy specific key''' 
    res = {}

    for log in logs: 
        val = log.get(key)
        if val:
            res[val] = res.get(val, 0) + 1

    return res


def sum_failed_payments(logs: list) -> int:
    '''COunts the total amount of failes operation'''
    failed_payments = filter_logs(logs, status="fail", action="payment")
    return sum(int(log.get("amount", 0)) for log in failed_payments)


if __name__ == "__main__":
    logs = [
        "2025-02-01 10:15:33|INFO|user=anna action=login status=success ip=10.0.0.1",
        "2025-02-01 10:17:10|ERROR|user=bob action=payment status=fail amount=120",
        "2025-02-01 10:20:01|INFO|user=anna action=logout status=success",
        "2025-02-01 10:22:45|WARNING|user=anna action=payment status=fail amount=300",
        "2025-02-01 10:30:12|ERROR|user=tom action=login status=fail ip=10.0.0.5"
    ]
    
    # Save the file.
    parsed_data = to_json(logs, filepath="output.json")

    # Removed the loops copy-paste.
    filters = [
        {"status": "fail"},
        {"level": "ERROR"},
        {"user": "anna"}
    ]

    for condition in filters:
        key, value = list(condition.items())[0]
        print(f"---- ONLY {str(value).upper()} ----")
        
        for log in filter_logs(parsed_data, **condition):
            print(log)

    print("---- COUNT BY LEVEL ----")
    print(count_by_key(parsed_data, "level"))

    print("---- COUNT BY USER ----")
    print(count_by_key(parsed_data, "user"))

    print("---- SUM OF FAILED PAYMENTS AMOUNT ----")
    print(sum_failed_payments(parsed_data))
