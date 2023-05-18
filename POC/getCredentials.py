

def get_credentials():

    data = open("credentials.txt", "r")

    uname = None
    pwd = None
    for i in data:
        i = i.split("=")
        if i[0].lower() == "username":
            uname = i[1].strip()
        elif i[0].lower() == "password":
            pwd = i[1].strip()

    return uname , pwd