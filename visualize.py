import psycopg2

conn = psycopg2.connect(
    dbname="thronedb",
    user="postgres",
    password="your_password",
    host="localhost",
    port="5432"
)

print("Connected to ThroneDB successfully!")
conn.close()
