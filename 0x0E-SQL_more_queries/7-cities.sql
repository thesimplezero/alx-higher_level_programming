-- Create database hbtn_0d_usa and tables city.
-- City table description: id(INT) not null, auto-generated, primary key; state_id as foreign key referencing states table's id; name VARCHAR(256) not null.
-- If hbtn_0d_usa database exists, script won't fail.
-- If cities table exists, script won't fail.

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT, 
    FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states(id),
    name VARCHAR(256) NOT NULL
);