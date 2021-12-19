from src.model.participant import Participant

def get_participants_from_event(event):
    event_participants = event["participants"]
    participants = []

    for participant in event_participants:
        participants.append(
            Participant(name=participant["name"], email=participant["email"])
        )

    return participants