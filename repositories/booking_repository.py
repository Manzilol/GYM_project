from db.run_sql import run_sql
from models.booking import Booking
import repositories.member_repository as member_repository
import repositories.session_repository as session_repository

def save(booking):
    sql = " INSERT INTO bookings (member_id, session_id, notes) VALUES (%s, %s, %s) RETURNING id"
    values = [booking.member.id, booking.session.id, booking.notes]
    results = run_sql(sql, values)
    booking.id = results[0]['id']
    return booking

def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)


def select_all():
    bookings = []
    sql = "SELECT * FROM bookings"
    results = run_sql(sql)

    for row in results:
        booking = Booking(row['member'], row['session'], row['notes'], row['id'])
        bookings.append(booking)
    return bookings

def select(id):
    sql = "SELECT * FROM bookings WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        member = member_repository.select(result['member_id'])
        session = session_repository.select(result['session_id'])
        booking = Booking(member, session, result['notes'], result['id'])
    return booking

        


def delete(id):
    sql = "DELETE FROM bookings WHERE id = %s"
    values = [id]
    run_sql(sql, values)