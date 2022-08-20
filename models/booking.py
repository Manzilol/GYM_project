class Booking:

    def __init__(self, member, session, notes, id = None):
        self.member = member
        self.session = session
        self.notes = notes
        self.id = id