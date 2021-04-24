import csv

class Dress:
    def __init__(self, temp_lower_bound, temp_upper_bound, dress_items):
        self.temp_lower_bound = temp_lower_bound
        self.temp_upper_bound = temp_upper_bound
        self.dress_items = dress_items

    def info(self):
        return {
            'temp_lower_bound': self.temp_lower_bound,
            'temp_upper_bound': self.temp_upper_bound,
            'dress_items': self.dress_items
        }


def get_dress_for_weather(dress_rules_path, temp):
    with open(dress_rules_path) as csv_file:
        dress_reader = csv.reader(csv_file)
        # Skip first row (header)
        next(dress_reader)
        for row in dress_reader:
            if row[0] == '':
                lower_bound = int(-100)
            else:
                lower_bound = int(row[0])
            if row[2] == '':
                upper_bound = int(200)
            else:
                upper_bound = int(row[1])
            dress_items = row[2].split(', ')
            if temp >= lower_bound and temp < upper_bound:
                return Dress(lower_bound, upper_bound, dress_items)
    return None
