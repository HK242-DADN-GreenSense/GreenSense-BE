def validate_interval_job_option(options) -> bool:
    time_units = ["weeks", "days", "hours", "minutes", "seconds"]
    
    for unit in time_units:
        if unit in options:
            if not isinstance(options[unit], int):
                return False
            
    return True 
    

def vallidate_cron_job_option(options) -> bool:
    cron_options = ["year", "month", "day", "week", "day_of_week", "hour", "minute", "second"]
    
    for option in cron_options:
        if option in options:
            if not options[option].isnumeric():
                return False
            
            if option == "year" and (int(options[option]) < 0):
                return False
            
            if option == "month" and (int(options[option]) < 1 or int(options[option]) > 12):
                return False
            
            if option == "day" and (int(options[option]) < 1 or int(options[option]) > 31):
                return False
            
            if option == "week" and (int(options[option]) < 1 or int(options[option]) > 53):
                return False
            
            if option == "day_of_week" and (int(options[option]) < 0 or int(options[option]) > 6):
                return False
            
            if option == "hour" and (int(options[option]) < 0 or int(options[option]) > 23):
                return False
            
            if option == "minute" and (int(options[option]) < 0 or int(options[option]) > 59):
                return False
            
            if option == "second" and (int(options[option]) < 0 or int(options[option]) > 59):
                return False
    
    return True