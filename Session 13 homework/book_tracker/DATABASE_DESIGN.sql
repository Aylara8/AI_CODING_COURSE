-- Database Design for Book Tracker
CREATE TABLE books (
    id UUID PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    status VARCHAR(50) CHECK (status IN ('Want to Read', 'Reading', 'Finished')),
    rating INTEGER DEFAULT 0,
    review TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);