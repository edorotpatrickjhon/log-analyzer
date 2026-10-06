def parse_log_line(log_line):
    lines = log_line.split('"')
    parse_dictionary = {}

    #getting the values
    line_one = lines[0]
    line_three = lines[2]
    line_three = line_three.split()
    line_one = line_one.split()

    #ip
    ip_value = line_one[0]

    #timestamp
    timestamp_value = line_one[-2] + " " + line_one[-1]

    #method
    method_value = lines[1]

    #status
    status_value = int(line_three[0])
    #size
    size_value = int(line_three[1])

    parse_dictionary = {
            'ip' : ip_value,
            'timestamp' : timestamp_value,
            'method' : method_value,
            'status' : status_value,
            'size' : size_value
        }
    return parse_dictionary

def count_failed_logins(input_records):
    input_records = [
            {'ip' : '192.168.1.10', "status" : 401},
            {'ip' : '192.168.1.10', "status" : 401},
            {'ip' : '10.0.0.5', "status" : 200}
        ]

    ip_and_error_dict = {}

    for record in input_records:

        if record['status'] == 401:
            if record['ip'] in ip_and_error_dict:
                ip_and_error_dict[record["ip"]] += 1
            else:
                ip_and_error_dict[record["ip"]] = 1
    
    return ip_and_error_dict

def read_log_file(filepath):
    with open (filepath) as f:
        logs = []
        for line in f:
            logs.append(line.strip())

    return logs

