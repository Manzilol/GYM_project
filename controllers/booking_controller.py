from flask import Blueprint, Flask, redirect, render_template, request

from models.booking import Booking
import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository
import repositories.session_repository as session_repository

bookings_blueprint = Blueprint("bookings", __name__)

@bookings_blueprint.route("/bookings")
def bookings():
    bookings = booking_repository.select_all()
    return render_template("bookings/index.html", bookings=bookings)

@bookings_blueprint.route("/bookings/new")
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


@bookings_blueprint.route("/bookings/<id>", methods=["POST"])
def update_booking(id):
    member_id = request.form["member_id"]
    session_id = request.form["session_id"]
    notes = request.form["notes"]
    member = member_repository.select(member_id)
    session = session_repository.select(session_id)
    booking = Booking(member, session, notes, id)
    booking_repository.update(booking)
    return redirect("/bookings")

@bookings_blueprint.route("/bookings/<id>/delete", methods=["POST"])
def delete_booking(id):
    booking_repository.delete(id)
    return redirect("/bookings")

@bookings_blueprint.route("/bookings/enrollment")
def enrolled():
    
