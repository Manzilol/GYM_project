from db.run_sql import run_sql

from models.member import Member

def save(member):
    sql = "INSERT INTO members(name, age, sex) VALUES (%s, %s, %s) RETURNING id"
    values = [member.name, member.age, member.sex]
    results = run_sql(sql, values)
    member.id = results[0]['id']
    return member

