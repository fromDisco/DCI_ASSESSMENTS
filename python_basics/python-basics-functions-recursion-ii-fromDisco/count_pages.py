test_data1 = [
    {
        "title": "Home",
        "pages": [
            {
                "title": "About",
                "pages": [
                    {
                        "title": "The company"
                    },
                    {
                        "title": "Our services"
                    },
                    {
                        "title": "Our products"
                    },
                    {
                        "title": "Our deliveries",
                        "pages": [
                            {
                                "title": "National"
                            },
                            {
                                "title": "International"
                            }
                        ]
                    }
                ]
            },
            {
                "title": "Shop",
                "pages": [
                    {
                        "title": "Browse all"
                    },
                    {
                        "title": "Categories"
                    }
                ]
            },
            {
                "title": "My account",
                "pages": [
                    {
                        "title": "Settings"
                    },
                    {
                        "title": "Edit profile"
                    },
                    {
                        "title": "My transactions"
                    }
                ]
            }
        ]
    }
]


def count_pages(website_obj):
    """
    Count number of pages ("title") in db

    Parameters: 
        website_obj (list): contains dicts

    Returns:
        count (int)
    """
    count = 0

    # no need for base case, because for loop doesn't run infinite
    # for loop runs through every possible list
    # item is always a dict
    for item in website_obj:
        # it there is a title in item add 1
        count += 1 if item["title"] else 0
        if "pages" in item:
            # if there is key "pages" in item,
            # call count_pages again with containing list
            count += count_pages(item["pages"])

    return count


print(count_pages(test_data1))
