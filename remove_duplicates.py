def remove_duplicates_basic(items):
    unique_entries = []
    for i items:
        if not i in unique_entries:
            unique_entries.append(i)
    return unique_entries
        
    list(set(items))  
        

def remove_duplicates(items):
    ids_to_remove = []
    unique_entries = []
    for i, e in enumerate(items):
        if e in unique_entries:
            ids_to_remove.append(i)
        else:
            unique_entries.append(e)
    for i in reversed(ids_to_remove):
        items.pop(i)
        

a = ["tom", "tom", "jane", "bob", "jim", "jane", "bob", "jane"]
remove_duplicates(a)

assert a == ['tom', 'jane', 'bob', 'jim']
print(a)
