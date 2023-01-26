from app_src import db


class Reminder(db.Model):
    __tablename__ = "reminders"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.VARCHAR(255))
    description = db.Column(db.TEXT)

    def __repr__(self):
        return f"<{self.__class__.__name__} id={self.id}, title='{self.title}', description='{self.description}'>"

    @classmethod
    def all(cls):
        """
        Send back all entries of table
        """
        reminder_list = cls.query.all()
        return reminder_list

    def save(self):
        """
        Stores the values of title and description in the table
        """
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except:
            raise Exception("Something terrible happened! Talk to the developer")

    @classmethod
    def find(cls, id):
        """
        Find an db entry by id an return an instance
        """
        try:
            reminder_instance = cls.query.get(id)
            return reminder_instance
        except Exception as e:
            print("Error stdout", "#" * 40, "\n", e, "#" * 40)
            return None

    @classmethod
    def delete(cls, id):
        """
        Delete one table row by id
        """
        try:
            instance = cls.query.get(id)
            db.session.delete(instance)
            db.session.commit()
            del instance

            return "Delete was successful", 204
        except:
            return "Something wrong happened!", 500

    def update(self, **kwargs):
        """
        Update row of associated instance
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

        db.session.commit()
        return self
