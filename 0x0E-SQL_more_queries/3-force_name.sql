-- Create table force_name in MySQL server.
-- Table description: id(INT), name(VARCHAR(256)) not NULL.
-- If force_name table exists, script won't fail.

CREATE TABLE IF NOT EXISTS force_name(
    id INT,
    name VARCHAR(256) NOT NULL
);