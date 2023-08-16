-- Create database hbtn_0d_2 and user user_0d_2.
-- Grant SELECT privilege on hbtn_0d_2 to user_0d_2.
-- Set user_0d_2's password to user_0d_2_pwd.
-- If hbtn_0d_2 exists, script won't fail.
-- If user_0d_2 exists, script won't fail.

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS  'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';