# Import the DBcm module for database connection management
import DBcm

# Database connection details
db_details = {
    "host": "localhost",
    "database": "SwimClub",
    "user": "swimuser",
    "password": "swimPasswd",
    "port": 3307
}

# Import SQL queries from the queries module
from queries import *

def get_swim_sessions():
    # Connect to the database and execute the SQL query to get swim sessions
    with DBcm.UseDatabase(db_details) as db:
        db.execute(SQL_SESSIONS)
        results = db.fetchall()
    return results

def get_session_swimmers(date):
    """Given a date (YYYY-MM-DD), retrieve a list of 
    swimmers and their corresponding ages for that specific date.
    """
    # Connect to the database and execute the SQL query to get swimmers for a session
    with DBcm.UseDatabase(db_details) as db:
        db.execute(SQL_SWIMMERS_BY_SESSION, (date,))
        results = db.fetchall()
    return results

def get_swimmers_events(name, age, date):
    """Given a date (YYYY-DD-MM), swimmer's name, and age, 
    obtain a list of events they participated in on that date."""
    # Connect to the database and execute the SQL query to get swimmer's events for a session
    with DBcm.UseDatabase(db_details) as db:
        db.execute(
            SQL_SWIMMERS_EVENTS_BY_SESSION,
            (
                name,
                age,
                date,
            ),
        )
        results = db.fetchall()
    return results

def get_swimmers_times(name, age, distance, stroke, date):
    """When provided with a date, swimmer's name, age, distance, and stroke, 
    yield a list of swim times for the specified swimmer on that date, 
    considering the given distance and stroke"""
    # Connect to the database and execute the SQL query to get swimmer's times for an event in a session
    with DBcm.UseDatabase(db_details) as db:
        db.execute(
            SQL_CHART_DATA_BY_SWIMMER_EVENT_SESSION,
            (
                name,
                age,
                distance,
                stroke,
                date,
            ),
        )
        results = db.fetchall()
    return results