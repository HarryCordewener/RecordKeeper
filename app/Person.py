from datetime import datetime


class Person:
    birth_date_format = "%m/%d/%Y"

    def __init__(self, **kwargs):
        # last name mandatory, must be alphabetic
        # This will rule out real world last names like "Del Toral" or "Smith-Grainger"
        self.last_name = kwargs['last_name'].strip().capitalize()
        if not self.last_name.isalpha():
            raise ValueError(f"Invalid last name {self.last_name}")

        # first name mandatory, must be alphabetic
        self.first_name = kwargs['first_name'].strip().capitalize()
        if not self.first_name.isalpha():
            raise ValueError(f"Invalid first name {self.first_name}")

        # gender mandatory, must be male or female
        self.gender = kwargs['gender'].strip().capitalize()
        if self.gender not in ("Male", "Female"):
            raise ValueError("Gender must be \"Male\" or \"Female\"")

        # color mandatory, must be alphabetic
        self.favorite_color = kwargs['favorite_color'].strip().lower()
        if self.favorite_color and not self.favorite_color.isalpha():
            raise ValueError(f"Invalid favorite color {self.favorite_color}")

        # birth date mandatory and in MM/DD/YYYY format
        try:
            self.date_of_birth = datetime.strptime(
                kwargs['date_of_birth'].strip(),
                Person.birth_date_format)
        except ValueError:
            raise ValueError("Date of birth must be in MM/DD/YYYY format")

    def __str__(self):
        return ", ".join([
            self.first_name,
            self.last_name,
            self.gender,
            self.favorite_color,
            self.date_of_birth.strftime(Person.birth_date_format)
        ])
