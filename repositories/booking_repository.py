from db.run_sql import run_sql
from models.booking import Booking

def save(booking):
    sql = " INSERT INTO bookings (member_id, session_id, notes) VALUES (%s, %s, %s) RETURNING id"
    values = [booking.member.id, booking.session.id, booking.notes]
    results = run_sql(sql, values)
    booking.id = results[0]['id']
    return booking