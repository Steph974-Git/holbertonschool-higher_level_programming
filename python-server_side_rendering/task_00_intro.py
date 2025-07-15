#!/usr/bin/node

def generate_invitations(template, attendees):


    if not isinstance(template, str) or (attendees, list):
        raise TypeError
    if template is None or template == "":
        raise ValueError("Template is empty, no output files generated.")
    if attendees is None or attendees == "":
        raise ValueError("No data provided, no output files generated.")
    return [template.format(name=attendee) 
            for attendee in attendees]



attendees = [
    {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
]


for attendee in attendees:
     value = attendee.get('key') or "N/A"