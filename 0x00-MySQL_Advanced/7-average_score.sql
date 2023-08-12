-- creates a stored procedure ComputeAverageScoreForUser
DELIMITER //
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
  DECLARE average_score FLOAT;
  SELECT AVG(score) INTO average_score FROM corrections WHERE user_id = user_id;
  UPDATE users SET average_score = average_score WHERE id = user_id;
  IF ROW_COUNT() = 0 THEN
    INSERT INTO users (id, average_score) VALUES (user_id, average_score);
  END IF;
END //
DELIMITER ; //
