CREATE TABLE IF NOT EXISTS emails (
    id INT AUTO_INCREMENT PRIMARY KEY,
    event_id INT NOT NULL,
    email_subject NVARCHAR(255) NOT NULL,
    email_content TEXT NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    sent BOOLEAN DEFAULT 0
);

CREATE TABLE IF NOT EXISTS recipients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email NVARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS recipient_events (
    recipient_id INT NOT NULL,
    event_id INT NOT NULL,
    PRIMARY KEY (recipient_id, event_id),
    FOREIGN KEY (recipient_id) REFERENCES recipients(id)
);