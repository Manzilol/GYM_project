from cProfile import run
from db.run_sql import run_sql

from models.session import Session

def save(session):
    sql = "INSERT INTO sessions(name, room, duration, capacity, difficulty) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [session.name, session.room, session.duration, session.capacity, session.difficulty]
    results = run_sql(sql, values)
    session.id = results[0]['id']
    return session

def delete_all():
    sql = "DELETE FROM sessions"
    run_sql(sql)