# - Talk about environments
# - Integration test (connecting things together)
import psycopg2, os
from utils import build_where_clauses


def make_connection(database_name="flask_intro"):
    DATABASE_URL = os.environ.get("DATABASE_URL", None)
    if DATABASE_URL:
        # This is how we shall connect to the CI/CD and future production environments in the Cloud.
        connection = psycopg2.connect(DATABASE_URL)
    else:
        connection = psycopg2.connect(
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432",
            database=database_name,
        )
    connection.autocommit = True  # commit each entry to database automatically
    cur = connection.cursor()
    return dict(connection=connection, cur=cur)


class Reminder:
    cur = make_connection().get("cur")
    # Class name is Singular of Table

    def __init__(self, title, description) -> None:
        self.class_name = self.__class__.__name__
        self.table_name = self.set_table_name()
        self.title = title
        self.id = None
        self.description = description

    def __repr__(self) -> str:
        return f"<Reminder id={self.id}, title='{self.title}', description='{self.description}'>"

    def set_table_name(self):
        return f"{self.class_name.lower()}s"

    def save(self):
        """
        Stores the values of title and description in the table
        """
        # try:
        self.cur.execute(
            f"""INSERT INTO {self.table_name} (title, description) 
        VALUES('{self.title}', '{self.description}') RETURNING id, title, description"""
        )

        reminder_id, title, description = self.cur.fetchone()
        self.id = reminder_id
        return self
        # except Error as e:
        #    raise Exception("Something terrible happened! Talk to the developer")

    @classmethod
    def find(cls, *args, **kwargs):
        # TODO: Add support for an unknown number of arguments and make sure the data is queried
        # e.g. Reminder.find(title="a", description="Loves to eat") -> should find a reminder with a title and a description
        # - You may have to use concepts like `**kwargs` or `*args`
        # - the search should be case insensitive hint: Integrate the use of LIKE in Postgresql
        # - Your SQL can query more than one column at the same time

        # Prepare default parts of query
        query = "SELECT id, title, description FROM reminders WHERE "

        # defining combining condition: "and", "or"
        query_connectors = kwargs.get("connector", "")
        # delete connector.
        # Not nessacary for the query
        if query_connectors:
            del kwargs["connector"]
        else:
            query_connectors = "and"

        # if only on number is passed in Arguments it most likely the id
        if len(args) == 1 and type(*args) == int:
            kwargs["id"] = args[0]

        # pass kwargs to utils to transform to where clauses
        temp_query = build_where_clauses(**kwargs)

        # if no args or kwargs ar present give feedback to client
        if not args and not kwargs:
            raise Exception("Please provide Arguments, when instantiating a class.")

        # build the complete query
        query += f" {query_connectors} ".join(temp_query)

        try:
            cls.cur.execute(query)
            id, title, description = cls.cur.fetchone()

            reminder_instance = cls(title=title, description=description)
            reminder_instance.id = id
            return reminder_instance
        except Exception as e:
            print(e)
            return None

    @classmethod
    def all(cls):
        # return all reminders
        cls.cur.execute("SELECT id, title, description FROM reminders;")
        reminders = cls.cur.fetchall()

        reminder_list = []
        for r in reminders:
            # create an instance
            reminder_instance = cls(title=r[1], description=r[2])
            reminder_instance.id = r[0]

            reminder_list.append(reminder_instance)

        return reminder_list

    @classmethod
    def delete(cls, id):
        try:
            # SQL something?
            cls.cur.execute(f"DELETE FROM reminders WHERE id={id}")
            return "Delete was successful", 204
        except:
            return "Something wrong happened!", 500

    def update(self, **kwargs):

        title = kwargs.get("title", None)
        description = kwargs.get("description", None)

        # SQL statement to UPDATE both title and description (50%)
        self.cur.execute(
            f"""
        UPDATE reminders 
        SET title='{title}', description='{description}'
        WHERE id={self.id} RETURNING id, title, description
        """
        )

        reminder_values = self.cur.fetchone()
        print(reminder_values)
