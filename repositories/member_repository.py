from db.run_sql import run_sql

from models.member import Member

def save(member):
    sql = "INSERT INTO members(name, age, sex) VALUES (%s, %s, %s) RETURNING id"
    values = [member.name, member.age, member.sex]
    results = run_sql(sql, values)
    member.id = results[0]['id']
    return member

def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

def select(id):
    member = None
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    
    if results:
        result = results[0]
        member = Member(result['name'], result['age'], result['sex'], result['id'])
    return member

def select_all():
    members = []
    sql = "SELECT * FROM members"
    results = run_sql(sql)

    for row in results:
        member = Member(row['name'], row['age'], row['sex'], row['id'])
        members.append(member)
    return members

def update(member):
    sql = "UPDATE members SET (name, age, sex) = (%s, %s, %s) WHERE id = %s"
    values = [member.name, member.age, member.sex, member.id]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE FROM members WHERE id = %s"
    values = [id]
    run_sql(sql, values)

