

import csv

def extract_records(file_name):
    """
    Convert csv fle into list of rows.
    """
    records = []
    with open(file_name) as file:
        for row in csv.reader(file):
            records.append(row)            
    return records

def count_records(records, col_index, values):
    """
    Counts records for which values in col_index equals value.
    """
    total = 0
    for record in records:
        record = remove_row_spaces(record)
        if record[col_index] in value:
            total += 1
    return total
    

def determine_col_index(headers, col_name):
    """
    Determine what the column index is.
    ['id', ' email', ' country', ' q1', ' q2', ' q3', ' q4']
    """
    return headers.index(col_name)

def remove_row_spaces(row):
    return [field.strip() for field in row]


def ensure_unique_responses(records, col_index):
    records_by_unique_field = {}
    for record in records:
        field_to_be_unique = record[col_index]
        if not records_by_unique_field.has_key(field_to_be_unique):
            records_by_unique_field[field_to_be_unique] = record
    return records_by_unique_field.values()

def count_values_in_file(file_name, col_name, values):
    records = extract_records(file_name)
    first_row = records[0]
    headers = remove_row_spaces(first_row)
    data = records[1:]
    col_index = determine_col_index(headers, col_name)
    
    
    ensure_unique_responses(records, determine_col_index(headers, "email"))
    total = count_records(data, col_index, values)
    
    print(total)
    
count_values_in_file('data.csv', "q2", ["1"])
count_values_in_file('survey2.csv', "q2", ["Yes"])
count_values_in_file('merged.csv', "q2", ["Yes", "1"])

'''
Example passing functions as parameters:


def count_records_2(records, inclusion_function):
    """
    Counts records for which values in col_index equals value.
    """
    total = 0
    for record in records:
        record = remove_row_spaces(record)
        if inclusion_function(record):
            total += 1
    return total


emails_already_counted = []
def answered_yes_to_q2(record):
    record[0] in emails_already_counted
    return record[2] == "1" or record[2] == "Yes"
    
count_records_2(records, answered_yes_to_q2)

'''