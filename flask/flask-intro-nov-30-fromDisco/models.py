import psycopg2, os

# TODO: Live coding task (Teacher led)
# Add an update method


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
    connection.autocommit = True
    cur = connection.cursor()
    return dict(connection=connection, cur=cur)


class Reminder:
    cur = make_connection().get("cur")

    def __init__(self, title, description) -> None:
        self.title = title
        self.id = None
        self.description = description

    def __repr__(self) -> str:
        return f"<Reminder id={self.id}, title='{self.title}', description='{self.description}'>"

    def save(self):
        """
        Stores the values of title and description in the table
        """
        try:
            self.cur.execute(
                f"""INSERT INTO reminders (title, description) 
            VALUES('{self.title}', '{self.description}') RETURNING id, title, description"""
            )

            id, title, description = self.cur.fetchone()
            reminder_instance = Reminder(title, description)
            reminder_instance.id = id
            return reminder_instance
        except:
            raise Exception("Something terrible happened! Talk to the developer")

    @classmethod
    def find(cls, id):
        try:
            cls.cur.execute(
                f"SELECT id, title, description FROM reminders WHERE id={id}"
            )

            id, title, description = cls.cur.fetchone()

            reminder_instance = cls(title=title, description=description)
            reminder_instance.id = id
            return reminder_instance
        except Exception as e:
            print("Error stdout", "#" * 40, "\n", e, "#" * 40)
            return None

    @classmethod
    def all(cls):
        cls.cur.execute("SELECT id, title, description FROM reminders;")

        reminders = cls.cur.fetchall()

        reminder_list = []

        for r in reminders:
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
        print("**********")
        print(self.id)

        # SQL statement to UPDATE both title and description (50%)
        self.cur.execute(
            f"""
        UPDATE reminders 
        SET title='{title}', description='{description}'
        WHERE id={self.id} RETURNING id, title, description
        """
        )

        reminder_values = self.cur.fetchone()
        return reminder_values

    def test_update(self):
        reminder_id = self.reminder.id
        # update the data
        self.reminder.update(title="Good", description="Class rocks!")
        self.assertEqual(
            str(Reminder.find(reminder_id)),
            f"<Reminder id={reminder_id}, title='Good', description='Class rocks!'>",
        )
