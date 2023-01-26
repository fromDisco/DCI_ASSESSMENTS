from connect import Connect


def query_parser(emp_properties, db_output):
    """
    I KNOW. PERPHAPS ITS OVERENGENEERING
    but i had to do it, because of pratice.
    I use this function for normal Strings
    as well as lists of strings.
    I had the choice to do nested for loops.
    but this is not flexible, and no practice.
    SO NO. I WONT REWRITE IT ;)
    """
    output = ""
    for i, element in enumerate(db_output):
        if type(element) != tuple:
            output += f"{emp_properties[i]}: {element}\n"
        else:
            output += query_parser(emp_properties, element)
            output += "\n"

    # for i, emp_property in enumerate(emp_properties):
    #    output += f"{emp_property}: {db_output[0][i]}\n"

    return output


def add_to_db(sql_string):
    # get database connection and cursor from connect()
    connect = Connect()
    connection = connect.connection
    cursor = connect.cursor

    if type(sql_string) == list:
        for string in sql_string:
            cursor.execute(string)
    else:
        cursor.execute(sql_string)

    connection.commit()
    connect.closing(connection, cursor)


def read_from_db(sql_string):
    # open database and get connection and cursor from connect()
    connect = Connect()
    connection = connect.connection
    cursor = connect.cursor

    cursor.execute(sql_string)
    answer_tuple = cursor.fetchall()
    connect.closing(connection, cursor)

    return answer_tuple


if __name__ == "__main__":
    sql_string = [
        "CREATE TABLE warehouse (id serial NOT NULL PRIMARY KEY, warehouse_name VARCHAR (100) NOT NULL, employee_count serial);",
        "CREATE TABLE employee (id serial NOT NULL PRIMARY KEY,	employee_name VARCHAR (100) NOT NULL, warehouse_id serial NOT NULL,	joining_date DATE NOT NULL,	speciality VARCHAR (100) NOT NULL, salary INTEGER NOT NULL,	experience SMALLINT);"
        "INSERT INTO employee (id, employee_name, warehouse_id, joining_date, speciality, salary, experience) VALUES ('101', 'Mo', '1', '2005-2-10', 'HR Manager', '40000', NULL), ('102', 'Michael', '1', '2018-07-23', 'Driver', '30000', NULL), ('103', 'Lukaku', '2', '2016-05-19', 'Conveyor', '25000', NULL),('104', 'Robert', '2', '2017-12-28', 'Logistics Spcialist', '28000', NULL),('105', 'Linda', '3', '2004-06-04', 'Logistics Spcialist', '42000', NULL),('106', 'Kahn', '3', '2012-09-11', 'Manager', '30000', NULL),('107', 'Bernice', '4', '2014-08-21', 'Medic', '32000', NULL),('108', 'Karen', '4', '2011-10-17', 'Driver', '30000', NULL);",
        "INSERT INTO warehouse (id, warehouse_name, employee_count) VALUES ('1', 'Amazon Warehouse', 1000),('2', 'Rewe Warehouse', 400),('3', 'Tedi Warehouse', 200),('4', 'Bahn Warehouse', 1500);",
    ]
    add_to_db(sql_string)
