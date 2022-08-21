# import pdb
from models.booking import Booking
from models.member import Member
from models.session import Session

import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository
import repositories.session_repository as session_repository

# booking_repository.delete_all()
# member_repository.delete_all()
# session_repository.delete_all()

member1 = Member('Chuck Norris', 17, "male")
member_repository.save(member1)

member2 = Member('Mr T', 25, "male")
member_repository.save(member1)

member1 = Member('Samus Aran', 23, "female")
member_repository.save(member1)

# pdb.set_trace()
