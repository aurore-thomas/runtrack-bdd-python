SELECT *
    -> FROM Etudiants
    -> WHERE age = (SELECT MIN(age) FROM Etudiants);