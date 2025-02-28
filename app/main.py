import math


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name    # Initialize class attributes
        self. description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        count_weeks = math.ceil(days / 7)
        return count_weeks

    @classmethod
    def from_dict(cls, course_dict: dict) -> "OnlineCourse":
        return cls(
            name=course_dict["name"],
            description=course_dict["description"],
            weeks=cls.days_to_weeks(course_dict["days"])
        )
