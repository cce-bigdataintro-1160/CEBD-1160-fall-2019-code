#!/usr/bin/env python3

import MySQLdb
import pandas.io.sql as psql


def pretty_print(name, to_print):
    print(f'{name}:')
    print(f'{to_print}\n\n')


db = MySQLdb.connect(host='localhost', user='root', passwd='root', db='defaultdb')

# create the query
query = "select * from users"

# execute the query and assign it to a pandas dataframe
df = psql.read_sql(query, con=db)

pretty_print("Users dataframe", df.to_string())
pretty_print("Users dataframe", df.columns)
pretty_print("Users dataframe", df.info())
pretty_print("Users dataframe", df.describe().to_string())

# close the database connection
db.close()
