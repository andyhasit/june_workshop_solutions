'''
Go over it first.

Thoughts?
Would you be happy taking ownership?
Would you be happy to take that into your system?

Questions you should ask:
    what does it do
    what is it supposed to do, is the intention clear
    are those the same
    Does it work
    Might it fail?
    Can I find out if it works under various circumstances?
    Can I easily change it?
    Can I do so without duplication?
    Does it work in Linux/Windows?
    Does it work in Taiwan?
    
Any "hmmmsss?"
Any WTFs?
    
What are the problems?
These are the questions you need to ask yourself.

4 qualities:
    
    Clarity of purpose
        Is it clear to anyone reading this what each part is supposed to do?
    
    Confidence in correct functioning
        Correct functioning is not good enough. 
        Must be demonstrable.
        Must be probable.
        How would you go about testing/checking/debugging this? Can you?
            Do it for real.
            Comment out & print
        simplicity + tests
    
    Adabtability     
        How would you handle likely variations/extensions?
            Mercurial?
            Linux/Windows
            American date format?
            Fri, Mon?
            Random date time, or option to specify?
    
    Reusability   
        Can I reuse parts for something slightly different?
            Can I reuse the date transforming with year?
     
The magic coincidence: what is good for one, is good for the other.        
'''

'''
1) Commit function does two unrelated things:
    Format the command
    Executes it on the operating system
    
    Should be separate.
    But it's only 2 lines long!
        What if one of those 2 lines grows, or needs to be variable?
        What if it was called elsewhere?
        What if we ant to us part of it elsewhere? - duplication!
'''

def execute_command(cmd_text):
    subprocess.call(cmd_text)
    
def build_git_commit_command(msg):
    return 'git commit -m "{0}"'.format(msg)

def call_git_commit(msg):
    cmd_text = build_git_commit_command(msg)
    execute_command(cmd_text)
    
'''
Is this enough? What about the ""
'''
    
def wrap_text_in_quotes_for_command(text):
    return "\"{0}\"".format(text)

'''
Even if we don't build the variability in at this point, it's worth structuring 
it correctly.
'''


'''
Do the same thing with the amend function
First, put comments:
'''


def amend(date_str):
    """
    Will send:
    git commit --amend --no-edit --date="Wed 03 Feb 21:56:23 2016"
    """
    #Get date time from date_str
    now = datetime.datetime.now()
    date_elements = date_str.split('/')
    day = int(date_elements[0])
    month = int(date_elements[1])
    if len(date_elements) == 3:
        year = int(date_elements[2])
        if year < 100:
            year = year + 2000 
    else:
        year = now.year
    new_date = datetime.datetime(year, month, day, now.hour, now.minute, 
                now.second)
    # Build date string
    new_date_str = new_date.strftime('%a %d %b %H:%M:%S %Y')
    # Build amend command text
    cmd = 'git commit --amend --no-edit --date="{0}"'.format(new_date_str)
    # Call command
    return subprocess.call(cmd)

'''
Next, pull out those bits:
'''

def get_date_time_from_string(date_str, time_object):
    now = datetime.datetime.now()
    date_elements = date_str.split('/')
    day = int(date_elements[0])
    month = int(date_elements[1])
    if len(date_elements) == 3:
        year = int(date_elements[2])
        if year < 100:
            year = year + 2000 
    elif year > 100 and year < 3000:
        year = now.year
    else:
        raise Exception("Please specify a date between 00 and 3000")
    return datetime.datetime(year, month, day, 
            time_object.hour, time_object.minute, time_object.second)

def build_git_amend_command(full_date_str):
    return 'git commit --amend --no-edit --date="{0}"'.format(full_date_str)

def build_full_date_string(date_object):
    return new_date.strftime('%a %d %b %H:%M:%S %Y')
    
def git_amend(date_str):
    """
    Expects date in format dd/mm or dd/mm/yy or dd/mm/yyyy
    Will send:
    git commit --amend --no-edit --date="Wed 03 Feb 21:56:23 2016"
    """
    date = get_date_time_from_string(date_str, now)
    full_date_str = build_full_date_string(date)
    cmd_text = build_git_amend_command(full_date_str)
    execute_command(cmd_text)

'''

Why is this better?
    Each function is easier to follow
    Each function is less likely to contain bugs
    So debugging takes a lot less time (and there is less of it)
    Reorganising takes a lot less time
    Functions can be tested in isolation, with multiple permutations, quickly
    So getting things to work takes a lot less time.
    
    
Let's try testing this. 

    Write a test for build_full_date_string()
'''

def test_build_full_date_string():
    date = datetime.datetime(2016, 02, 03, 21, 56, 23)
    assert build_full_date_string(date) == "Wed 03 Feb 21:56:23 2016"
    print "success"
    

'''
Let them try with the others.

get_date_time_from_string is not easy.

If it's difficult to write a test, then you haven't split it up enough.
    
'''

def extract_md(date_elements):
    day = int(date_elements[0])
    month = int(date_elements[1])
    return day, month
    
def extract_ymd(date_str):
    date_elements = date_str.split('/')
    day, month = extract_md(date_elements)
    if len(date_elements) == 3:
        year = int(date_elements[2])
    else:
        year = None
    return day, month, year
    
def fix_year(year):
    if year is None:
        year = datetime.datetime.now().year
    if year < 100:
        year = year + 2000 
    elif year < 1970:
        raise Exception("Please specify a year under 100 or above 1970")
    return year
    
def get_date_time_from_string(date_str, time_object):
    day, month, year = extract_ymd(date_str)
    year = fix_year(year)
    return datetime.datetime(year, month, day, 
            time_object.hour, time_object.minute, time_object.second)
            

def test_fix_year():
    this_year = datetime.datetime.now().year
    assert fix_year(None) == this_year
    assert fix_year(16) == 2016
    assert fix_year(1999) == 1999
    assert fix_year(1970) == 1970
    try:
        fix_year(189)
    except:
        failed_with_189 = True
    assert failed_with_189


'''
Having extracted the adjust_year functionality, we can change other parts around
it without risk of breaking it.
We can also change that, without breaking other parts around it.
That is vitally important.


Objections:
    This seems like a lot of extra work.
    I now have even more code.
    I'm not comfortable writing functions.
    I don't have time.
    It worked before/aint broke don't touch it.
        Working code is the worst
        If code is so precarious you won't touch it, then it doesn't "work"
        It "works" now, and within certain parameters.


Why should we bother doing this for hypothetical future requirements?
    That's not why you're doing it.
        
    You're doing it because:
        It makes your code clearer to follow
        So you can know for a fact your code works
        So your code is resistant to changes (even at first pass)
        
    
Things to note:
    It's OK to have many small one-line functions (in fact it's good)
    Function length isn't that important, so long as it just does one thing.
    note the level of abstraction: 
        git_amend is high-level, it doesn't do any nitty-gritty, it just coordinates.
        get_date_time_from_string deals

'''



'''
Is this right?
What about build_git_amend_command & build_full_date_string

Perhaps better as:
'''

def build_git_amend_command(date):
    full_date_str = build_full_date_string(date)
    return 'git commit --amend --no-edit --date="{0}"'.format(full_date_str)

def build_full_date_string(date_object):
    return new_date.strftime('%a %d %b %H:%M:%S %Y')

'''

Your task is to decide what should and shouldn't be inside each function.
Think:
    Level of abstraction
    Knowledge
    Reasons for change (should only be one)
'''
    

'''
Let's now look at how to make it variable:
    
First way is crude.
'''

def extract_md_uk(date_elements):
    day = int(date_elements[0])
    month = int(date_elements[1])
    return day, month

def extract_md_us(date_elements):
    day = int(date_elements[0])
    month = int(date_elements[1])
    return day, month

if settings['us_date_format']:
    extract_md = extract_md_uk
else:
    extract_md = extract_md_us
    

    
def git_amend(date_str):
    """
    Expects date in format dd/mm or dd/mm/yy or dd/mm/yyyy
    Will send:
    git commit --amend --no-edit --date="Wed 03 Feb 21:56:23 2016"
    """
    date = get_date_time_from_string(date_str, now)
    full_date_str = build_full_date_string(date)
    cmd_text = build_git_amend_command(full_date_str)
    execute_command(cmd_text)



'''

Finally: That WTF with those return values.

    Two problems:
        1) Has not encapsulated the abstraction.
            This function was meant to do something with the operating system, 
            and exposes a detail.
            What if this gets used on a different operating system that uses a
            different convention?
            Or the implementation returns string "0" instead?
        2) Has not made it clear what it is meant to be for
        
    Clearly had a problem, found the solution, implemented it, and carried on,
    leaving the next person clueless.
    
    What is the cost? Confusion, lack of faith in the rest.
    
    How do you avoid doing things like that?
    
    1. Recognize them as WTFs (use your gut feeling, or ask someone else).
    2. How can you communicate these things?
        Variable names
        Function names
        Add more variables
        Add more functions

'''

def execute_command(cmd_text):
    result = subprocess.call(cmd_text)
    return result == 0 # OS_SUCCESS_CODE
    
'''
But, should we even be doing this?

What if the calling code doesn't know to check the return value?
Python philosophy is to avoid return codes, and raise exceptions instead.

'''

def execute_command(cmd_text):
    result = subprocess.call(cmd_text)
    if result != OS_SUCCESS_CODE:
        raise EnvironmentError("command call failed\n" + cmd_text)
    

'''
Ask "What is the correct thing to do in case of failure?"

'''
