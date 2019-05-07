The squirrels in Palo Alto spend most of the day playing. In particular, they play if the temperature is between 60 and 90 (inclusive). Unless it is summer, then the upper limit is 100 instead of 90. Given an int temperature and a boolean is_summer, return True if the squirrels play and False otherwise.


squirrel_play(70, False) → True
squirrel_play(95, False) → False
squirrel_play(95, True) → True
Go...Save, Compile, Run (ctrl-enter)






def alarm_clock(day, vacation):

    weekend = "06"
    weekdays = "12345"
    if vacation:
        if str(day) in weekend:
            return "off"
        else:
            return "10:00"
    else:
        if str(day) in weekend:
            return "10:00"
        else:
            return "7:00"
