from unicodedata import name
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

# def select(id):
#     human = None 
#     sql = "SELECT * FROM humans WHERE id = %s"
#     values = [id]
#     results = run_sql(sql, values)
#     # checking if the list returned by `run_sql(sql, values)` is empty. Empty lists are 'fasly' 
#     # Could alternativly have..
#     # if len(results) > 0 
#     if results:
#         result = results[0]
#         human = Human(result["name"], result["id"])
#     return human

def select(id):
    member = None
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    
    if results:
        result = results[0]
        member = Member(result['name'], result['age'], results['sex'], results['id'])
    return member

def select_all():
    members = []
    sql = "SELECT * FROM members"
    results = run_sql(sql)

    for row in results:
        member = Member(row['name'], row['age'], row['sex'], row['id'])
        members.append(member)
    return members

def delete(id):
    sql = "DELETE FROM members WHERE id = %s"
    values = [id]
    run_sql(sql, values)