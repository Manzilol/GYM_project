from flask import Blueprint, Flask, redirect, render_template, request

from models.session import Session
import repositories.session_repository as session_repository

sessions_blueprint = Blueprint("sessions", __name__)

@sessions_blueprint.route("/sessions")
def sessions():
    sessions = session_repository.select_all()
    return render_template("/sessions/index.html", sessions=sessions)

@sessions_blueprint.route("/sessions/new")
def new_session():
    return render_template("/sessions/new.html")

@sessions_blueprint.route("/sessions", methods=["POST"])
def create_session():
    name = request.form["name"]
    room = request.form["room"]
    duration = request.form["duration"]
    capacity = request.form["capacity"]
    difficulty = request.form["difficulty"]
    new_session = Session(name, room, duration, capacity, difficulty)
    session_repository.save(new_session)
    return redirect("/sessions")

@sessions_blueprint.route("/sessions/<id>/edit")
def edit_session(id):
    session = session_repository.select(id)
    return render_template('sessions/edit.html', session=session)

@sessions_blueprint.route("/sessions/<id>", methods=["POST"])
def update_session(id):
    name = request.form["name"]
    room = request.form["room"]
    duration = request.form["duration"]
    capacity = request.form["capacity"]
    difficulty = request.form["difficulty"]
    session = Session(name, room, duration, capacity, difficulty, id)
    session_repository.update(session)
    return redirect("/sessions")

@sessions_blueprint.route("/sessions/<id>/delete", methods=["POST"])
def delete_session(id):
    session_repository.delete(id)
    return redirect("/sessions")

@sessions_blueprint.route("/sessions/enrolled")
def enrolled_session_form():
    return render_template("/sessions/enrolled.html")

@sessions_blueprint.route("/sessions/<id>", methods = ["POST"])
def session_members_enrolled(id):
    session = session_repository.select(id)
    members = session_repository.enrolled(session)
    return render_template("sessions/enrolled.html", session=session, members = members)

