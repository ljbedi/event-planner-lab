from flask import Blueprint, render_template, request

from models.event import Event
from models.event_list import events, add_new_event

events_blueprint = Blueprint("events", __name__)

# INDEX, display all events 

@events_blueprint.route('/events')
def index():
    return render_template("index.jinja", title = "EVENT PLANNER", event_list=events)

@events_blueprint.route('/events', methods = ["POST"])
def add_event():
    event_title = request.form['title']
    event_description = request.form['description']
    event_date = request.form['date']
    event_location = request.form['location']
    event_number_of_guests = request.form['number_of_guests']
    new_event = Event(event_title, event_date, event_number_of_guests,  event_location, event_description)
    print(new_event.__dict__)
    add_new_event(new_event)
    return render_template('index.jinja', title="EVENT PLANNER", event_list=events)


