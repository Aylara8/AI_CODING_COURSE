-- Database Design for OpenShelf

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
);

CREATE TABLE resource (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    filename TEXT NOT NULL,
    cover_image TEXT,
    user_id INTEGER NOT NULL,
    FOREIGN KEY(user_id) REFERENCES user(id)
);

-- Example row:
INSERT INTO user (username, email, password) VALUES ('student1', 's1@school.edu', 'pbkdf2:sha256...');
INSERT INTO resource (title, filename, user_id) VALUES ('Math Quiz', '8f2a...quiz.pdf', 1);
