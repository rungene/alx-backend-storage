-- creates a stored procedure ComputeAverageScoreForUser
DELIMITER //
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
  DECLARE avg_score FLOAT;
  SELECT AVG(score) INTO avg_score FROM corrections WHERE user_id = user_id;
  UPDATE users SET average_score = avg_score WHERE id = user_id;
  IF ROW_COUNT() = 0 THEN
    INSERT INTO users (id, average_score) VALUES (user_id, average_score);
  END IF;
END //
DELIMITER ; //
