from flask import Blueprint, Flask, redirect, render_template, request

from models.booking import Booking
import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository
import repositories.session_repository as session_repository

bookings_blueprint = Blueprint("bookings", __name__)

@bookings_blueprint.route("/bookings")
def bookings():
    bookings = booking_repository.select_all()
    return booking_repository("/bookings/index.html", bookings=bookings)

@bookings_blueprint.route("bookings/new")
def new_booking():
    members = member_repository.select_all()
    sessions = session_repository.select_all()
    return render_template("bookings/new.html", members=members, sessions=sessions)

@bookings_blueprint.route("/bookings", methods=["POST"])
def create_booking():
    member_id = request.form["member_id"]
    session_id = request.form["session_id"]
    notes = request.form["notes"]
    member = member_repository.select(member_id)
    sesison = session_repository.select(session_id)
    new_booking = Booking(member, sesison, notes)
    booking_repository.save(new_booking)
    return redirect("/bookings")

@bookings_blueprint.route("/bookings/<id>/edit")
def edit_booking(id):
    booking = booking_repository.select(id)
    members = member_repository.select_all()
    sessions = session_repository.select_all()
    return render_template('bookings/edit.html', booking=booking, members=members, sessions=sessions)



























# @bookings_blueprint.route("/bookings/new")
# def new_booking():
#     return render_template("/booking/new.html")

# @bookings_blueprint.route("/bookings", methods=["POST"])
# def create_booking():
#     name = request.form["name"]
#     room = request.form["room"]
#     duration = request.form["duration"]
#     capacity = request.form["capacity"]
#     difficulty = request.form["difficulty"]
#     new_session = Session(name, room, duration, capacity, difficulty)
#     session_repository.save(new_session)
#     return redirect("/sessions")

# @bitings_blueprint.route("/bitings", methods=["POST"])
# def create_biting():
#     human_id = request.form["human_id"]
#     zombie_id = request.form["zombie_id"]
#     human = human_repository.select(human_id)
#     zombie = zombie_repository.select(zombie_id)
#     new_biting = Biting(human, zombie)
#     biting_repository.save(new_biting)
#     return redirect("/bitings")

# @bookings_blueprint.route("/bookings/<id>/edit")
# def edit_session(id):
#     session = session_repository.select(id)
#     return render_template('sessions/edit.html', session=session)

# @bookings_blueprint.route("/bookings/<id>", methods=["POST"])
# def update_session(id):
#     name = request.form["name"]
#     room = request.form["room"]
#     duration = request.form["duration"]
#     capacity = request.form["capacity"]
#     difficulty = request.form["difficulty"]
#     session = Session(name, room, duration, capacity, difficulty, id)
#     session_repository.update(session)
#     return redirect("/sessions")

# @bookings_blueprint.route("/bookings/<id>/delete", methods=["POST"])
# def delete_session(id):
#     session_repository.delete(id)
#     return redirect("/sessions")