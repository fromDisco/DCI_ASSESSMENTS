class PhoneNumberConverter:
    regex = r"([(]?[+][\d]{2,}[)]?)([ ][(][\d]{4}[)])?([\d -]*)"

    def to_python(self, value):
        return value

    def to_url(self, value):
        return str(value)