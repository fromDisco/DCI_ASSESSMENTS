print("\n ---- Task1 ----")
settings = {"title": "how to get not frustrated", "pages": []}


def change_site_title(string):
    """
    Change global dictionary

    Parameters:
        string (str): string to change the title

    Returns: 
        none
    """
    settings["title"] = string


print(settings)
change_site_title("Tadaaa")
print(settings)


print("\n ---- Task2 ----")
default_settings = {"title": "Banana", "pages": []}


def get_title(dictionary=default_settings):
    """
    Returns title of given arg dictionary

    Parameters:
        dictionary (dict): Dictionary to read out

    Returns:
        title (str)
    """
    return dictionary["title"]


print(get_title(settings))
print(get_title())
change_site_title("A new fancy title")
print(get_title(settings))
print(get_title())


print("\n ---- Task3 ----")


def get_pages(settings=default_settings):
    """
    Return value for key "pages"

    Parameters:
        settings (dict)

    Returns: 
        none
    """
    return settings['pages']


def add_page(to_add, settings=default_settings):
    """
    change value of dict["pages"]

    Parameters:
        value (dict): add this to settings["pages"]
        settings (dict): dictionary to change

    Returns:
        none
    """
    settings["pages"].append(to_add)


home = {"title": "Home", "pages": "/"}
add_page(home)
print(get_pages())
print(get_pages(settings))
about = {"title": "About", "path": "/about/"}
add_page(about, settings)
print(get_pages())
print(get_pages(settings))


print("\n ---- Task4 ----")


def print_user_profile(gender="female", first="John", last="Doe", pictures=[]):
    if gender == "female" and first == "John":
        first = "Jane"

    user_pictures = "\n".join(pictures)

    return f"The user {first} {last} has the following pictures:\ncommon_header.png\n{user_pictures}"


test_data1 = {
    "gender": "male",
    "last": "Brown",
    "pictures": ["holidays1.png", "easter_grandma.png"]
}
test_data2 = {
    "first": "Alicia",
    "last": "Schmidt"
}
test_data3 = {
    "last": "Korkov",
    "pictures": ["sunset.png"]
}
print(print_user_profile(**test_data1))
print(print_user_profile(**test_data2))
print(print_user_profile(**test_data3))
print(print_user_profile(**test_data2))
