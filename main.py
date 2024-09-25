import sqlite3

def get_user_info(user_id):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    # Vulnerable to SQL injection
    query = f"SELECT * FROM users WHERE id = {user_id};"
    cursor.execute(query)
    user_info = cursor.fetchone()

    connection.close()
    return user_info
