--SQL code that  Creates a stored procedure ComputeAverageScoreForUser that
-- computes and stores the average score for a student.
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser (user_id INT)
BEGIN
    DECLARE agg_score INT DEFAULT 0;
    DECLARE mypro_count INT DEFAULT 0;

    SELECT SUM(score)
        INTO agg_score;
        FROM corrections;
        WHERE corrections.user_id = user_id;
    SELECT COUNT(*)
        INTO mypro_count;
        FROM corrections;
        WHERE corrections.user_id = user_id;

    UPDATE users
        SET users.average_score = IF(mypro_count = 0, 0, agg_score / mypro_count)
        WHERE users.id = user_id;
END $$
DELIMITER ;
