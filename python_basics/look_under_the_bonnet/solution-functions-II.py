import os

os.system("clear")

# Task 1

settings = {"title": "My original title"}


def change_site_title(new_title):
    """Change the title of the site."""
    settings['title'] = new_title


# Test cases
print("------- Task 1 -------")
print("\n# settings before change:")
print(settings)

# change original settings (dict)
change_site_title("A new fancy title")

# print the changed settings (dict)
print("\n# settings after change:")
print(settings)


# Task 2
print("\n\n------- Task 2 -------")

default_settings = {
    "title": "My original title"
}


def get_title(settings=default_settings):
    """Get the title of the site."""
    return settings['title']


# Test cases
# print(get_title(settings))
# print(get_title())
# change_site_title("A new fancy title")
# print(get_title(settings))
# print(get_title())


# Task 3

print("\n\n------- Task 3 -------")
settings['pages'] = []
default_settings['pages'] = []


def get_pages(settings=default_settings):
    """Return the pages stored in the settings."""
    return settings['pages']


def add_page(page, settings=default_settings):
    """Add a page to the settings."""
    settings['pages'].append(page)


# Test cases
# home = {"title": "Home", "path": "/"}
# add_page(home)
# print(get_pages())
# print(get_pages(settings))
# about = {"title": "About", "path": "/about/"}
# add_page(about, settings)
# print(get_pages())
# print(get_pages(settings))


# Task 4
print("\n\n------- Task 4 -------")


def print_user_profile(gender="female", first=None, last="Doe", pictures=None):
    """Print a summary of a user profile."""
    if not pictures:
        pictures = []
    if not first:
        if gender == "female":
            first = "Jane"
        else:
            first = "John"
    pictures.insert(0, "common_header.png")
    print(f"The user {first} {last} has the following pictures:")
    for picture in pictures:
        print(picture)


# Test cases
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
print_user_profile(**test_data1)
print_user_profile(**test_data2)
print_user_profile(**test_data2)
print_user_profile(**test_data3)
