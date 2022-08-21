# import pdb
from models.booking import Booking
from models.member import Member
from models.session import Session

import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository
import repositories.session_repository as session_repository

booking_repository.delete_all()
member_repository.delete_all()
session_repository.delete_all()

member1 = Member('Chuck Norris', 17, 'male')
member_repository.save(member1)

member2 = Member('Mr T', 25, 'male')
member_repository.save(member1)

member3 = Member('Samus Aran', 23, 'female')
member_repository.save(member3)

session1 = Session("Pilates", "F1-1", 30, 15, 3)
session_repository.save(session1)

session2 = Session("Trampolines", "F0-4", 90, 30, 4)
session_repository.save(session2)

session3 = Session("Free weights", "F2-5", 60, 6, 2)
session_repository.save(session3)

booking1 = Booking(member1, session1, "The chuck loves pilates")
booking_repository.save(booking1)

booking2 = Booking(member1, session3, "I chuck norris need to improve my deadlifts")
booking_repository.save(booking2)

booking3 = Booking(member3, session2, "This is the closest it feels to being back in space")
booking_repository.save(booking3)


# pdb.set_trace()


