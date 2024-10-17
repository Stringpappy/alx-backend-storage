-- script that create func safe div that divide numbers
DROP FUNCTION IF EXISTS SafeDiv;
DELIMITER $$
CREATE FUNCTION SafeDiv (a INT, b INT)
RETURNS FLOAT DETERMINISTIC
BEGIN
    DECLAR outcome FLOAT DEFAULT 0;

    IF b != 0 THEN
        SET outcome = a / b;
    END IF;
    RETURN outome;
END $$
DELIMITER ;
