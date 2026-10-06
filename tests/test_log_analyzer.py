from analyzer import read_log_file, parse_log_line, count_failed_logins

def test_parse_log_line_valid_post_returns_parsed_dict():
    log_line = '192.168.1.10 - - [06/Oct/2026:14:32:10 +0000] "POST /login HTTP/1.1" 401 128'
    
    expected_output = {
        'ip' : '192.168.1.10',
        'timestamp' : '[06/Oct/2026:14:32:10 +0000]',
        'method' : 'POST /login HTTP/1.1',
        'status' : 401,
        'size' : 128
    }

    assert parse_log_line(log_line) == expected_output

def test_count_failed_logins_valid_list_returns_ip_and_error_dict():
    input_records = [
        {'ip' : '192.168.1.10', "status" : 401},
        {'ip' : '192.168.1.10', "status" : 401},
        {'ip' : '10.0.0.5', "status" : 200}
    ]
    
    expected_output = {
        '192.168.1.10': 2
    }
    
    assert count_failed_logins(input_records) == expected_output


def test_read_log_file_valid_log_file_returns_list_of_lines():
    filepath = 'tests/test_log.txt'

    expected_output = [
        '192.168.1.10 - - [06/Oct/2026:14:32:10 +0000] "POST /login HTTP/1.1" 401 128',
        '10.0.0.5 - - [07/Oct/2026:10:00:00 +0000] "GET / HTTP/1.1" 200 50'
    ]

    assert read_log_file(filepath) == expected_output