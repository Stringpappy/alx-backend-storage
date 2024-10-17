-- iMysql scriptCreates a view need_meeting that lists all student
--that have a score  under 80 (strict) and no last_meeting or more than 1 mont
DROP VIEW IF EXISTS need_meeting;
CREATE VIEW need_meeting AS
    SELECT name
        FROM students
        WHERE score < 80 AND
            (
                last_meeting IS NULL
                OR last_meeting < SUBDATE(CURRENT_DATE(), INTERVAL 1 MONTH)
            )
;
