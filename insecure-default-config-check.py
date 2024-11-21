  '''
  **Insecure Default Configurations**
Many software products come with default configurations that are not secure by default. For example, many
databases allow remote connections without proper authentication or have weak passwords enabled by default.

- **Exploit Example**: If you find a database server with the default username `admin` and password `password`,
you can exploit it to access sensitive data.
  '''
  
  
  import mysql.connector

  # Insecure configuration: Connect to MySQL without proper authentication
  db = mysql.connector.connect(
      host="localhost",
      user="admin",
      password="password"
  )

  cursor = db.cursor()
  cursor.execute("SHOW DATABASES")
  for db in cursor:
      print(db)