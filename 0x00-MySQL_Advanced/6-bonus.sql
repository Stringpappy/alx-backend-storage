--Mysql script that Creates a stored procedure AddBonus that adds a new
-- correction for a student data.
DROP PROCEDURE IF EXISTS AddBonus;
DELIMITER $$
CREATE PROCEDURE AddBonus (user_id INT, project_name VARCHAR(255), score FLOAT)
BEGIN
    DECLARE mypro_count INT DEFAULT 0;
    DECLARE mypro_id INT DEFAULT 0;

    SELECT COUNT(id)
        INTO mypro_count
        FROM projects
        WHERE name = project_name;
    IF mypro_count = 0 THEN
        INSERT INTO projects(name)
            VALUES(project_name);
    END IF;
    SELECT id
        INTO mypro_id
        FROM projects
        WHERE name = project_name;
    INSERT INTO corrections(user_id, mypro_id, score)
        VALUES (user_id, mypro_id, score);
END $$
DELIMITER ;
