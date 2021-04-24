import csv
from datetime import datetime

class Workout:

    def __init__(self, workout_date_time, distance, duration, notes):
        self.workout_date_time = workout_date_time
        self.distance = distance
        self.duration = duration
        self.notes = notes

    def info(self):
        return {
            'workout_date_time': self.workout_date_time,
            'distance': self.distance,
            'duration': self.duration,
            'notes': self.notes
        }


def get_workout_for_date(training_plan_path, desired_workout_date):
    retval = None
    with open(training_plan_path) as csvfile:
        trainingPlanReader = csv.reader(csvfile)
        # Skip first row (header)
        next(trainingPlanReader)
        for row in trainingPlanReader:
            workout_date_time = datetime.strptime(f'{row[0]} {row[1]}', '%m/%d/%y %I:%M %p')
            if( desired_workout_date == workout_date_time.date() ):
                distance = None
                duration = None
                if(len(row[2]) > 0 ):
                    distance = int(row[2])
                if (len(row[3]) > 0):
                    duration = int(row[3])
                notes = row[4]
                retval = Workout(workout_date_time, distance, duration, notes)
    return retval