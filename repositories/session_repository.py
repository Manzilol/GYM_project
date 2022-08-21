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

def select(id):
    session = None
    sql = "SELECT * FROM sessions WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    
    if results:
        result = results[0]
        session = Session(result['name'], result['room'], results['duration'], results['capacity'], results['difficulty'], results['id'])
    return session


def select_all():
    sessions = []
    sql = "SELECT * FROM sessions"
    results = run_sql(sql)

    for row in results:
        session = Session(row['name'], row['age'], row['sex'], row['id'])
        sessions.append(session)
    return session

def delete(id):
    sql = "DELETE FROM sessions WHERE id = %s"
    values = [id]
    run_sql(sql, values)