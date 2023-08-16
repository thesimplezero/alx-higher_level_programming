-- Create database hbtn_0d_usa and table state.
-- Description: id(INT) unique, auto-generated, primary key, not null; name VARCHAR(256) not null.
-- If hbtn_0d_usa database exists, script won't fail.
-- If state table exists, script won't fail.

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);