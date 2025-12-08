-- Створення таблиці фільмів
CREATE TABLE IF NOT EXISTS movies (
    movie_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    genre VARCHAR(50) CHECK (genre IN ('мелодрама', 'комедія', 'бойовик')),
    duration INTEGER NOT NULL CHECK (duration > 0),
    rating DECIMAL(3,1) CHECK (rating >= 0 AND rating <= 10),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Створення таблиці кінотеатрів
CREATE TABLE IF NOT EXISTS cinemas (
    cinema_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    ticket_price DECIMAL(6,2) NOT NULL CHECK (ticket_price > 0),
    seats_count INTEGER NOT NULL CHECK (seats_count > 0),
    address VARCHAR(500) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Створення таблиці транслювання фільмів
CREATE TABLE IF NOT EXISTS screenings (
    screening_id SERIAL PRIMARY KEY,
    movie_id INTEGER NOT NULL,
    cinema_id INTEGER NOT NULL,
    start_date DATE NOT NULL,
    show_days INTEGER NOT NULL CHECK (show_days > 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    FOREIGN KEY (movie_id) 
        REFERENCES movies(movie_id) 
        ON DELETE CASCADE,
    
    FOREIGN KEY (cinema_id) 
        REFERENCES cinemas(cinema_id) 
        ON DELETE CASCADE
);

-- Створення індексів для покращення продуктивності
CREATE INDEX idx_movies_genre ON movies(genre);
CREATE INDEX idx_movies_rating ON movies(rating);
CREATE INDEX idx_screenings_dates ON screenings(start_date);
CREATE INDEX idx_screenings_cinema ON screenings(cinema_id);
CREATE INDEX idx_screenings_movie ON screenings(movie_id);