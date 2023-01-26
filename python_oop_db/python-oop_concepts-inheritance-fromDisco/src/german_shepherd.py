from dog import Dog


class GermanShepherd(Dog):
    def walk(self) -> str:
        """
        How does the GS run?
        """
        super().walk()
        return_val = "German Shepherds show their beautiful fur while running."
        print(return_val)
        return return_val
