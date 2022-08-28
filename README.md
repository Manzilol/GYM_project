# GYM_project

App Requirements:
This app will require the user to have:
  - Flask

Brief:

This app was designed to be used by a member of staff who works ina gym.
It can:
  -Show all members
    -Add a new member
    -Edit an existing member
    -Delete an existing member
    
  -Show all sessions
    -Add a new session
    -Edit an existing session
    -Show all members currently enrolled in a session.
    -Delete an existing session
    
  -Show all bookings
    -Add a new booking
    -Edit an existing booking
    -Delete an existing booking
    
    
How to get the app running:
1. Navigate to the files folder in the console.
2. Type 'createdb gym'
3. Type psql -d gym -f db/gym.sql
4. Type python3 console.py
5. Type flask run
6. copy the ip address in the terminal (it should look like 'http://127.0.0.1:5001')
7. paste this into your browser. This should then load the app.

Navigating the App:

To navitgate the app use your mouse to click on anything that is within a border.
