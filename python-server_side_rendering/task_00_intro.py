#!/usr/bin/python3
"""
task_00_intro.py
Generate invitation files from a template and a list of attendees.
"""

import os


def generate_invitations(template, attendees):
    """Generate output_X.txt invitation files from template and attendees."""

    # ---- Type checks ----
    if not isinstance(template, str):
        print(f"Invalid input type: template must be a string, got {type(template).__name__}.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        got = type(attendees).__name__
        print("Invalid input type: attendees must be a list of dictionaries, "
              f"got {got}.")
        return

    # ---- Empty input checks ----
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    placeholders = ["name", "event_title", "event_date", "event_location"]

    # ---- Generate files ----
    for idx, attendee in enumerate(attendees, start=1):
        invitation = template

        for key in placeholders:
            value = attendee.get(key, "N/A")

            # Treat None / empty string as missing
            if value is None or (isinstance(value, str) and value.strip() == ""):
                value = "N/A"

            invitation = invitation.replace("{" + key + "}", str(value))

        filename = f"output_{idx}.txt"

        # Don't overwrite existing files
        if os.path.exists(filename):
            print(f"File {filename} already exists, skipping.")
            continue

        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(invitation)
        except (OSError, IOError) as e:
            print(f"Error writing {filename}: {e}")
