from database_manager import get_connection

conn = get_connection()
cursor = conn.cursor()
cursor.execute("SELECT name FROM products LIMIT 20")
rows = cursor.fetchall()
print("Actual names in your DB:")
for row in rows:
    print(f"'{row[0]}'")  # The quotes will show if there are hidden spaces
conn.close()
