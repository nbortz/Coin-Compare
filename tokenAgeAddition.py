import datetime

def add_age(benchmarkDate: datetime.date, userTokenAge: int) -> datetime.date:
    """
    Adds 'age_in_days' to the 'reference_date' and returns a single date result.
    
    :param reference_date: A datetime.date object representing the starting date.
    :param age_in_days: An integer representing the number of days to add.
    :return: A datetime.date object resulting from the addition of 'age_in_days' to 'reference_date'.
    """
    new_date = benchmarkDate + datetime.timedelta(days=userTokenAge)
    return new_date

