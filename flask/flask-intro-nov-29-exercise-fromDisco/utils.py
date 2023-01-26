def build_where_clauses(**kwargs):
    temp_query = []

    for key, value in kwargs.items():
        # default comparison operator for text search
        equal_or_like = " ilike "
        cleaned_value = ""

        try:
            # try to convert value into integer
            # (id, or other int based values)
            value = int(value)
        except ValueError:
            pass

        # dont clean up integers
        if type(value) != int:
            cleaned_value += "'%"
            for char in value:
                # reduce double chars like "oo" to one "o"
                # and add a wildcard "%" behind every letter
                # check the last 2 chars if they match the pattern
                if cleaned_value[-2:] != char + "%":
                    cleaned_value += char + "%"
            cleaned_value += "'"
        else:
            # integers are not changed because,
            # this would match too many numbers
            # and the id is specific
            cleaned_value = value
            # comparison operator for ints is =
            equal_or_like = "="

        temp_query.append(f"{key}{equal_or_like}{cleaned_value}")

    return temp_query


def get_table_columns():
    list_table_column_names = """SELECT column_name FROM 
    information_schema.columns WHERE table_name='reminders'"""
