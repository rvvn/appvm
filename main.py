import mysql.connector

connection = mysql.connector.connect(
 host="localhost", # replace this with your actual host name
 user="username",
 password="password",
 database="database_name"
)
cursor = connection.cursor()

# SQL injection example 1: ' or '1'='1' - single quote (')
query = "SELECT * FROM users WHERE username=(' or '1'='1'") # user input is not sanitized
print(cursor.execute(query))

# SQL injection example 2: '' OR 1=0
query = "SELECT * FROM users WHERE username=('') OR 1=0" # no quote marks around single quotes (')
print(cursor.execute(query))
