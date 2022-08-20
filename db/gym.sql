DROP TABLE sessions;
DROP TABLE members;
DROP TABLE bookings;



CREATE TABLE sessions (
    session_id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    room VARCHAR(255),
    duration INT,
    capacity INT,
    difficulty INT
);

CREATE TABLE members (
    member_id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    sex VARCHAR(255),
    booking_id INT NOT NULL REFERENCES bookings(id)
);

CREATE TABLE bookings (
    booking_id SERIAL PRIMARY KEY,
    member_id INT NOT NULL  REFERENCES members(id) ON DELETE CASCADE,
    session_id INT NOT NULL  REFERENCES sessions(id) ON DELETE CASCADE,
    notes VARCHAR(255)
);

