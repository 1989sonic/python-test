import random
import string

# Generate a log type
log_type = ['[Info]   ', '[Warning]', '[Error]  ']

# Generate a random string of random unique characters
def generate_random_string(length):
    chars = [char for char in string.printable if char not in string.whitespace]    
    result = random.choices(chars, k=length)
    return ''.join(result)

# Generate the Logfile
log_list = [None] * 10000
x=0
while x < 10000:
    # Generate a random time
    random_time = str(f"{random.randint(0, 23):02d}")+":"+str(f"{random.randint(0, 59):02d}")+":"+str(f"{random.randint(0, 59):02d}")
    # Create the log
    typ = random.choice(log_type)
    random_string = generate_random_string(random.randint(5, 100))
    log_list[x] = random_time, ' ' + typ + '- ' + random_string
    x = x + 1

# Sort the log
sorted_log_list = sorted(log_list, key=lambda t: t[0])

# Print the log lines to a file
with open('LOG_FILE.txt', mode ='w') as file:
    for log_line in sorted_log_list:
        file.write(''.join(log_line)+'\n')