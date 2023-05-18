from getCredentials import get_credentials
from db.Database import DB
def main():

    uname , pwd = get_credentials()

    db_obj = DB(uname , pwd)
    conn = db_obj.get_connection()
    df = db_obj.get_data(conn)



if __name__ == "__main__":

    main()