-- Creates a stored procedure AddBonus that adds a new correction for a student.
DELIMITER // ;
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score FLOAT)
BEGIN
  DECLARE id_project INT;
  SELECT id INTO id_project FROM projects WHERE name = project_name;
  IF id_project IS NULL THEN
    INSERT INTO projects (name) VALUES(project_name);
    SET id_project = LAST_INSERT_ID();
  END IF;
  INSERT INTO corrections(user_id, project_id, score)
  VALUES(user_id, id_project, score);
END //
DELIMITER ; //
