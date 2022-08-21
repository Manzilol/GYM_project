DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS sessions;


CREATE TABLE sessions (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    room VARCHAR(255),
    duration INT,
    capacity INT,
    difficulty INT
);

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    sex VARCHAR(255)
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    member_id INT NOT NULL REFERENCES members(id) ON DELETE CASCADE,
    session_id INT NOT NULL REFERENCES sessions(id) ON DELETE CASCADE,
    notes VARCHAR(255)
);

