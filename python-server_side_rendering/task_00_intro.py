#!/usr/bin/python3

def generate_invitations(template, attendees):


    if not isinstance(template, str) or not isinstance(attendees, list):
        print("Invalid types: template must be a string and attendees must be a list.")
        return TypeError
    if template is None or template == "":
        print("Template is empty, no output files generated.")
        return ValueError
    if attendees is None or attendees == "":
        print("No data provided, no output files generated.")
        return ValueError
    return [template.format(name=attendee) 
            for attendee in attendees]


template = "Hello {name},\n You are invited to the {event_title} on {event_date} at {event_location}."
attendees = [
    {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
]

invitation = generate_invitations(template, attendees)

for index, invitation in enumerate(invitation, star=1):
    
    



