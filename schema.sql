-- DROP TABLE emails;
-- DROP TABLE recipients;
-- DROP TABLE recipient_events;


CREATE TABLE IF NOT EXISTS emails (
    id INTEGER,
    event_id INTEGER NOT NULL,
    email_subject VARCHAR(255) NOT NULL,
    email_content TEXT NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    sent BOOLEAN DEFAULT 0,
    PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS recipients (
    id INTEGER,
    email NVARCHAR(255) NOT NULL UNIQUE,
    PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS recipient_events (
    recipient_id INTEGER NOT NULL,
    event_id INTEGER NOT NULL,
    PRIMARY KEY (recipient_id, event_id),
    FOREIGN KEY (recipient_id) REFERENCES recipients(id),
    FOREIGN KEY (event_id) REFERENCES emails(event_id)
);