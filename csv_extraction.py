
import csv



[
 {'id': 1, 'email': 'bob@gmail.com', 'q1': 1, 'q2' :0}
]

for row in rows:
    row['q2']

def foo(fielname):
    """
    Ext
    
    and if but expect sometimes
    and strips spsvrdd
     """
    count = 0
    records = []
    rows_by_email = {}
       
    
    def count_rows(fielname):
        with open(fielname) as file:
            for row in csv.reader(file):
                records.append(remove_space_in_row(row))
                if row['country'].lower() == "scotland" and row['q2'] == True:
                    count += 1
        

def remove_space_in_row():
    [i.strip() for i in row]


items = [
  ('green', 2),
  ('red', 5),
  ('green', 5),
]



weights_by_colour = {} 
for i in items:
    colour = i[0]
    weight = i[1]
    if weights_by_colour.has_key(colour):
        weights_by_colour[colour] += weight
    else:
        weights_by_colour[colour] = weight
        
        
    previous_value = weights_by_colour.setdefault(colour, 0) 
    weights_by_colour[colour] = weight + previous_value

    

response['bob@gmail.com'] = row
response['jane@gmail.com'] = row
































def extract_records(file_name):
    """
    Convert csv file into list of rows.
    """
    records = []
    with open(file_name) as file:
        for user_response in csv.reader(file):
            records.append(user_response)            
    return records




def count_records(records, should_record_be_counted):
    """
    Counts records for which should_record_be_counted() is True
    """
    total = 0
    for record in records:
        record = remove_row_spaces(record)
        if should_record_be_counted(record):
            total += 1
    return total
    
    
def should_record_be_counted(record):
    return record[2] == "1"
    
    
filter_function = should_record_be_counted
count_records(rows_from_csv, filter_function)


def double(x):
    return x * 2

fn = double

fn(9)
 
    
    
    
    

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

def split_headers_from_rows(records):
    first_row = records[0]
    headers = remove_row_spaces(first_row)
    rows_minus_headers = records[1:]
    return headers, rows_minus_headers

def count_values_in_file(file_name, col_name, values):
    """
    
    """
    records = extract_records(file_name)
    headers, rows_minus_headers = slit_headers_from_rows(records)
    col_index = determine_col_index(headers, col_name)
    unique_records = ensure_unique_responses(rows_minus_headers, determine_col_index(headers, "email"))
    total = count_records(unique_records, col_index, values)
    
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