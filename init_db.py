import os
import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="UserData",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD'])

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS public."Student";')
cur.execute('CREATE TABLE IF NOT EXISTS public."Student" ("Name" character varying(50) COLLATE pg_catalog."default" NOT NULL,'
                                 '"UFID" integer NOT NULL,'
                                 '"Email" character varying(50) COLLATE pg_catalog."default" NOT NULL,'
                                 'CONSTRAINT "Student_pkey" PRIMARY KEY ("UFID")'
                                 )

# Insert data into the table
cur.execute('INSERT INTO public."Student"("Name", "UFID", "Email")'
            'VALUES (\'Alice Aesop\', 11111111, \'alice@ufl.edu\')',
            )
#repeat insert command as many times as needed

conn.commit()

cur.close()
conn.close()