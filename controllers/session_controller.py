from flask import Blueprint, Flask, redirect, render_template, request

from models.session import Session
import repositories.session_repository as session_repository

session_blueprint = Blueprint("sessions", __name__)

@session_blueprint.route("/sessions")
def sessions():
    sessions = session_repository.select_all()
    return render_template("sessions/index.html", sessions=sessions)

@session_blueprint.route("/sessions/new")
def new_session():
    return render_template("/sessions/new.html")

@session_blueprint.route("/sessions", methods=["POST"])
def create_session():
    name = request.form["name"]
    room = request.form["room"]
    duration = request.form["duration"]
    capacity = request.form["capacity"]
    difficulty = request.form["difficulty"]
    new_session = Session(name, room, duration, capacity, difficulty)
    session_repository.save(new_session)
    return redirect("/sessions")

@session_blueprint.route("/sessions/<id>/edit")
def edit_(id):
    session = session_repository.select(id)
    return render_template('sessions/edit.html', session=session)

@session_blueprint.route("/session/<id>", methods=["POST"])
def update_session(id):
    name = request.form["name"]
    room = request.form["room"]
    duration = request.form["duration"]
    capacity = request.form["capacity"]
    difficulty = request.form["difficulty"]
    session = Session(name, room, duration, capacity, difficulty, id)
    session_repository.update(session)
    return redirect("/sessions")

@session_blueprint.route("/sessions/<id>/delete", methods=["POST"])
def delete_session(id):
    session_repository.delete(id)
    return redirect("/sessions")