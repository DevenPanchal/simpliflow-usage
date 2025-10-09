# function that takes a string and returns only first 50 characters
def trimtoonly50chars(s):
    # call capitalizeeachchar function
    s = capitalizeeachchar(s)
    # call introduce_space function
    s = introduce_space(s)
    return s[:50]


# function that Capitalizes each character of a string
def capitalizeeachchar(s):
    return s.upper()


# function that introduces a space between each character of a string
def introduce_space(s):
    return ' '.join(s)


# function 'last20chars' that takes a string returns only last 20 chars
def last20chars(s):
    return s[-20:]


def Adder(s):
    # convert incoming string to integer, add 2 and return the result as string
    return str(int(s) + 2)

# Take the input server hostname and ping the server and return the status
def pingserver(host):
    import subprocess
    import platform
    
    # Determine the command based on the operating system
    if platform.system().lower() == "windows":
        command = ["ping", "-n", "1", host]
    else:
        command = ["ping", "-c", "1", host]

    try:
        response = subprocess.run(command, capture_output=True, text=True, check=True)
        return response.stdout
    except subprocess.CalledProcessError as e:
        return e.output


# print the input strings in pink color
def printinpink(s):
    return f"\033[95m{s}\033[00m"

# print the input strings such that all characters are in different colors
def printeachcharindiffcolors(s):
    return ''.join([f"\033[9{str(i)}m{s[i]}\033[00m" for i in range(len(s))])


# execute the incoming python code and return the output
def execute_python_code(code):
    try:
        exec(code)
    except Exception as e:
        return e
    return ""
