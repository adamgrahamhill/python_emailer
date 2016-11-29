#file_reader.py

# Read email addresses and corresponding names from file. Use to create dictionary
def get_emails():
    emails = {}
    
    try:
        email_file = open('emails2.txt', 'r')
    
        for line in email_file:
            (email, name) = line.split(',')
            emails[email] = name.strip()
    except FileNotFoundError as err:
        print(err)

    return emails

# Read schedule from file
def get_schedule():
    try:
        schedule_file = open('schedule.txt', 'r')
    
        schedule = schedule_file.read()
    except FileNotFoundError as err:
        print(err)
    
    return schedule