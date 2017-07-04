#!/usr/bin/env python

# Creation of internal reporting tool for Logs Analysis of Newspaper

# import postgresql library
import psycopg2

# database name
DB_NAME = "news"


def print_headers():

    # Function to print the headers of the report
    print("\n")
    print("Internal Reporting Tool\n")
    print("Generating Reports...\n")

# 1 What are the most popular three articles of all time.


def pop_three_articles():

    conn = psycopg2.connect(database=DB_NAME)
    c = conn.cursor()
    """Below Query returns most accessed three articles as a
    sorted list with the most popular article at the top."""

    c.execute("""select a.title, count(*) as views
    from articles a join log l on l.path like concat('%', a.slug)
    where l.status = '200 OK'
    group by a.title, l.path
    order by views desc limit 3;""")
    pop_three_art = c.fetchall()
    conn.close()

# Display Results
    print("*** Three Most Accessed Articles ***\n")
    for row in pop_three_art:
        print(str(row[0]) + " ---> " + str(row[1]) + " views")
    print("\n")

# 2 Who are the most popular article authors of all time


def pop_art_authors():
    conn = psycopg2.connect(database=DB_NAME)
    c = conn.cursor()
    """Below Query returns most popular article author of all
    time as a sorted list with most popular author at the top."""

    c.execute("""select au.name, count(*) as views
    from authors au join articles a on a.author = au.id join log l on l.path
    like concat('%', a.slug)
    where l.status = '200 OK'
    group by au.name
    order by views desc;""")
    pop_art_auth = c.fetchall()
    conn.close()

# Display results
    print("*** Most Popular Article Author of all time ***\n")
    for row in pop_art_auth:
        print(str(row[0]) + " ---> " + str(row[1]) + " views")
    print("\n")

# 3 On which days did more than 1% of requests lead to errors


def page_req_errors():
    conn = psycopg2.connect(database=DB_NAME)
    c = conn.cursor()
    """Below Query returns date and error percent of page request which is
    greater than 1%."""

    c.execute("""select date, cast(to_char(percentage, 'FM999999999.00') as decimal)
    as percent
    from calc
    where cast(to_char(percentage, 'FM999999999.00') as decimal) > 1.0;""")
    req_errors = c.fetchall()
    conn.close()

# Display results
    print("*** Date and Error percent of page request greater than 1% ***\n")
    for row in req_errors:
        print (str(row[0]) + ' ---> ' + str(row[1]) + " % " + " Errors ")
    print("\n*** End of Report ****")
    print("\n")

print_headers()
pop_three_articles()
pop_art_authors()
page_req_errors()
