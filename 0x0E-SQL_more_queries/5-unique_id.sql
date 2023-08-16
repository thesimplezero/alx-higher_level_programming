-- Create table unique_id.
-- Description: id (INT) with default value 1 and must be unique, name VARCHAR(256).
-- If unique_id table exists, script won't fail.

CREATE TABLE IF NOT EXISTS unique_id(
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);