import datetime 
from workalendar.europe import Slovakia
from functools import cache

@cache
def SK_holidays(year):
    return [date_text[0] for date_text in Slovakia().holidays(2023)]

def dt_to_week_weekday(dt):

    return(dt.isocalendar()[1],dt.weekday())


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + datetime.timedelta(n)


def weeks_workdays(from_dt,to_dt):

    from_year=from_dt.year
    to_year=to_dt.year
    holidays=set(SK_holidays(from_year))|set(SK_holidays(to_year))
    from_dt_week,from_dt_weekday=dt_to_week_weekday(from_dt)
    to_dt_week,to_dt_weekday=dt_to_week_weekday(to_dt)
    counters={}
    for dt in daterange(from_dt,to_dt):
        week,weekday=dt_to_week_weekday(dt)
        if weekday>=5:
            continue
        if dt in SK_holidays(dt.year):
            continue
        counters[week]=counters.get(week,0)+1
    return counters

intervals=(
        (datetime.date(2023,7,1),datetime.date(2023,7,16)),
        (datetime.date(2023,7,23),datetime.date(2023,8,28)),
        (datetime.date(2023,12,27),datetime.date(2023,12,30)),
)       

sumall=0
for from_dt,to_dt in intervals:
    print('Interval',from_dt,to_dt)
    dov=weeks_workdays(from_dt,to_dt)
    print('V tyzdnoch',dov)
    sumint=sum(dov.values())
    print('Spolu za interval',sumint,'dni')
    print('-'*20)
    sumall+=sumint
print('Spolu za vsetky',sumall,'dni')

