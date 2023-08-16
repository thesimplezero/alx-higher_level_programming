-- Create table id_not_null.
-- Description: id(INT) NOT NULL with default value 1, name VARCHAR(256).
-- If id_not_null table exists, script won't fail.

CREATE TABLE IF NOT EXISTS id_not_null(
    id INT DEFAULT 1,
    name VARCHAR(256)
);