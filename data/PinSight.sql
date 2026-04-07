PRAGMA foreign_keys = ON;

CREATE TABLE bowlers (
    bowler_id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    nickname TEXT,
    dominant_hand TEXT,
    notes TEXT
);

CREATE TABLE sessions (
    session_id INTEGER PRIMARY KEY,
    bowler_id INTEGER NOT NULL,
    session_date TEXT,
    location TEXT,
    pin_system TEXT,
    notes TEXT,
    FOREIGN KEY (bowler_id) REFERENCES bowlers(bowler_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE games (
    game_id INTEGER PRIMARY KEY,
    session_id INTEGER NOT NULL,
    game_num INTEGER NOT NULL,
    score INTEGER NOT NULL,
    cross_lane INTEGER,
    notes TEXT,
    FOREIGN KEY (session_id) REFERENCES sessions(session_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CHECK (score BETWEEN 0 AND 300),
    CHECK (cross_lane IN (0, 1) OR cross_lane IS NULL)
);

CREATE TABLE frames (
    frame_id INTEGER PRIMARY KEY,
    game_id INTEGER NOT NULL,
    frame_num INTEGER NOT NULL,
    notes TEXT,
    FOREIGN KEY (game_id) REFERENCES games(game_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CHECK (frame_num BETWEEN 1 AND 10),
    UNIQUE (game_id, frame_num)
);

CREATE TABLE balls (
    ball_id INTEGER PRIMARY KEY,
    primary_bowler_id INTEGER NOT NULL,
    ball_name TEXT NOT NULL,
    ball_nickname TEXT,
    coverstock TEXT,
    core_type TEXT,
    is_hook_ball INTEGER,
    is_spare_ball INTEGER,
    notes TEXT,
    FOREIGN KEY (primary_bowler_id) REFERENCES bowlers(bowler_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    CHECK (is_hook_ball IN (0, 1) OR is_hook_ball IS NULL),
    CHECK (is_spare_ball IN (0, 1) OR is_spare_ball IS NULL)
);

CREATE TABLE rolls (
    roll_id INTEGER PRIMARY KEY,
    ball_id INTEGER,
    frame_id INTEGER NOT NULL,
    roll_num INTEGER NOT NULL,
    pins_hit INTEGER NOT NULL,
    starts_split INTEGER,
    hooked INTEGER,
    notes TEXT,
    FOREIGN KEY (ball_id) REFERENCES balls(ball_id)
        ON UPDATE CASCADE
        ON DELETE SET NULL,
    FOREIGN KEY (frame_id) REFERENCES frames(frame_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CHECK (roll_num BETWEEN 1 AND 3),
    CHECK (pins_hit BETWEEN 0 AND 10),
    CHECK (starts_split IN (0, 1) OR starts_split IS NULL),
    CHECK (hooked IN (0, 1) OR hooked IS NULL),
    UNIQUE (frame_id, roll_num)
);

CREATE INDEX idx_sessions_bowler_id ON sessions (bowler_id);
CREATE INDEX idx_games_session_id ON games (session_id);
CREATE INDEX idx_frames_game_id ON frames (game_id);
CREATE INDEX idx_rolls_frame_id ON rolls (frame_id);
CREATE INDEX idx_rolls_ball_id ON rolls (ball_id);
CREATE INDEX idx_balls_primary_bowler_id ON balls (primary_bowler_id);
