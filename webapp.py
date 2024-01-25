from flask import Flask, session, render_template, request
import os
import swim_utils
import data_utils
import conTime_utils

app = Flask(__name__)
app.secret_key = "Who is gonna know..."

@app.get("/")
def index():
    # Render the index page with a welcome message
    return render_template("index.html", title="Welcome to Swimclub")

@app.get("/swims")
def display_swim_sessions():
    # Retrieve swim sessions data
    data = data_utils.get_swim_sessions()
    
    # Extract dates from the data
    dates = [str(session[0].date()) for session in data]  
    
    # Render the template for selecting a swim session
    return render_template(
        "select.html",
        title="Select a swim session",
        url="/swimmers",
        select_id="chosen_date",
        data=dates,
    )

@app.post("/swimmers")
def display_swimmers():
    # Store chosen date in the session
    session["chosen_date"] = request.form["chosen_date"]
    
    # Retrieve swimmer data for the chosen date
    data = data_utils.get_session_swimmers(session["chosen_date"])
    
    # Format swimmer data for display
    swimmers = [f"{swimmer[0]}-{swimmer[1]}" for swimmer in data]
    
    # Render the template for selecting a swimmer
    return render_template(
        "select.html",
        title="Select a swimmer",
        url="/showevents",
        select_id="swimmer",
        data=sorted(swimmers),
    )

@app.post("/showevents")
def display_swimmer_events():
    # Extract swimmer and age from the selected form data
    session["swimmer"], session["age"] = request.form["swimmer"].split("-")
    
    # Retrieve swimmer's events for the chosen date
    data = data_utils.get_swimmers_events(
        session["swimmer"], session["age"], session["chosen_date"]
    )
    
    # Format events data for display
    events = [f"{event[0]} {event[1]}" for event in data]
    
    # Render the template for selecting an event
    return render_template(
        "select.html",
        title="Select an event",
        url="/showbarchart",
        select_id="event",
        data=events,
    )

@app.post("/showbarchart")
def show_bar_chart():
    # Extract event details from the selected form data
    distance, stroke = request.form["event"].split(" ")
    
    # Retrieve swimmer's times for the selected event
    data = data_utils.get_swimmers_times(
        session["swimmer"],
        session["age"],
        distance,
        stroke,
        session["chosen_date"],
    )
    
    # Extract times from the data
    times = [time[0] for time in data]
    
    # Perform conversions on times
    average_str, times_reversed, scaled = conTime_utils.perform_conversions(times)
    
    # Create a header for the chart
    header = f"{session['swimmer']} (Under {session['age']}) {distance} {stroke} - {session['chosen_date']}"
    
    # Render the template for the bar chart
    return render_template(
        "chart.html",
        title=header,
        data=list(zip(times_reversed, scaled)),
        average=average_str,
    )

if __name__ == "__main__":
    # Run the application in debug mode
    app.run(debug=True)