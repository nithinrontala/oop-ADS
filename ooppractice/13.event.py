class Event:
    def __init__(self, eventid, name, loc, cap):
        self.eventID = eventid
        self.name = name
        self.location = loc
        self.capacity = cap
        self.participants = []  

    def isEventFull(self):
        return len(self.participants) >= self.capacity

class Participant:
    def __init__(self, id, name, email):
        self.participantID = id
        self.name = name
        self.email = email

    def getParticipationInfo(self):
        return f"ParticipantID: {self.participantID}, Name: {self.name}, Email: {self.email}"

class EventManager:
    def __init__(self, events, participants):
        self.events = events
        self.participants = participants

    def registerParticipant(self, eid, participant):
        for e in self.events:
            if e.eventID == eid:
                event = e
                break
        if event and not event.isEventFull():
            event.participants.append(participant)
            return True
        return False

    def listParticipants(self, eid):
        for e in self.events:
            if e.eventID == eid:
                event = e
                break
        if event:
            return event.participants
        return []


def main():
    # Create an event with capacity 2
    event = Event(1, "Tech Conference", "Hall A", 2)
    # Create participants
    participant1 = Participant(101, "Mike", "mike@example.com")
    participant2 = Participant(102, "Anna", "anna@example.com")
    participant3 = Participant(103, "John", "john@example.com")
    em = EventManager([], [])
    em.events.append(event)
    # Register participants
    reg1 = em.registerParticipant(1, participant1)
    reg2 = em.registerParticipant(1, participant2)
    reg3 = em.registerParticipant(1, participant3)
    print("Participant 101 registered:", reg1)
    print("Participant 102 registered:", reg2)
    print("Participant 103 registered (should fail):", reg3)
    # List participants
    print("Participants for event 1:")
    for p in em.listParticipants(1):
        print(p.name)
if __name__ == '__main__':
    main()         