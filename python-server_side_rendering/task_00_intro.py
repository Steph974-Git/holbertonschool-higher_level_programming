#!/usr/bin/python3

def generate_invitations(template, attendees):


    if not isinstance(template, str) or not isinstance(attendees, list):
        print("Invalid types: template must be a string and attendees must be a list.")
        return None
    if not template:
        print("Template is empty, no output files generated.")
        return None
    if not attendees:
        print("No data provided, no output files generated.")
        return None

    for idx, attendee in enumerate(attendees, start=1):
        filled_template = template.format(
            name=attendee.get("name") or "N/A",
            event_title=attendee.get("event_title") or "N/A",
            event_date=attendee.get("event_date") or "N/A",
            event_location=attendee.get("event_location") or "N/A"
        )
        filename = f"output_{idx}.txt"
        try:
            with open(filename, "w") as f:
                f.write(filled_template)
        except Exception as e:
            print(f"Error writing file {filename}: {e}")
