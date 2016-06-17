
##x = "hello" 
##y = len(x)
##

##x = len('hello')
##
##if x > 8:
##    print("x is greater than 8")
##elif (x == 8):
##    print("")
##elif (x == 8):
##    print("")
##elif (x == 8):
##    print("")
##elif (x == 8):
##    print("")
##else:
##    print("It's not")
##    
##print(a is None)
##
##i = 0
##reached_end_of_file_buffer = False
##
##while not reached_end_of_file_buffer:
##    print_next_line(x)
##    if EOL:
##        reached_end_of_file_buffer = True
##   
##i = 0
##while True:
##    print(i)
##    i += 1
##    if True:
##        if i >= 10: 
##            break
##    print ()
##    
##print('finished')

##import math
##
##print(math.cos(50))
##
##
##w = [23, 56, 89]
##a = "hello my name is Andrew"
##chunks = a.split()
##chunks.append("hi")
##chunks.extend(w)
##chunks.insert(1, "Yo")
##w.
##print(chunks)

a = [23, 12, 89]
t = (1, 4, 8)
t1, t2, t3 = t
print(t1)

    
##x = a[2]
##a[0] = 99
##print(a)
##
##i = 0
##while i < len(a):
##    print(a[i])
##    i += 1


##for t in enumerate(a):
##    i, x = t
##    print(i)
##    print(x)
##
##
##for i, x in enumerate(a):
##    print(i)
##    print(x)
##    
##if x > 8:
##    pass
##else:
##    print(88)
##
##
##
##def has_exactly_one_at(text):
##    return text.count("@") == 1
##
##def has_correct_ending(text):
##    return text.endswith(".com")
##
##def has_only_valid_chars(text, valid_chars):
##    all_are_valid = True
##    for c in text:
##        if not (c.isalnum() or c in valid_chars):
##            all_are_valid = False
##            break
##    return all_are_valid
##
##valid_chars = ['.', '_', '@', '-']
##
##
##def is_email_valid(text):
##    conditions_that_must_be_true = [
##            #has_exactly_one_at(text),
##            has_correct_ending(text),
##            has_no_spaces(text),
##            has_only_valid_chars(text, valid_chars)
##            ]
##    return all(conditions_that_must_be_true)
##
##assert is_email_valid("@moetavern.com")
##assert is_email_valid("moe@tavern.com")
##assert not is_email_valid("moe@@tavern.com")
##assert not is_email_valid("moe@@tavern.co.uk")
###assert not is_email_valid("mo e@tavern.com")
##
##print "success"
##
### Prompt user for words exercise:
##
##words = []
##while True:
##    new_word = raw_input("Enter a new word").strip()
##    if len(new_word) > 0:
##        words.append(new_word)
##    else:
##        break
##
##print(sorted(words))
##
##
##
##
##def do_stuff(m):
##    m.append(99)
##    
##a = [1, 12, 34]
##b = list(a)
##do_stuff(b)
##
##print(b)
##print(a)
##
##x = "hello"
##
##old_list = "5, janet.fairfield@fastmail.me,  england, 0, 1, 1, 0".split(",")
####print(old_list)
##new_list = []
##for s in old_list:
##    new_list.append(s.strip())
##    
##for i, s in enumerate(old_list):
##    old_list[i] = s.strip()
##    
##    
##new_list = [i.strip() for i in old_list]
##
##
##
##d = {} 
##d['jim@gmail.com'] = row
##d['bob@fmail.com'] = row
