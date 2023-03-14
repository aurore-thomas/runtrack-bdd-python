SELECT *
    -> FROM Etudiants
    -> WHERE age = (SELECT MAX(age) FROM Etudiants);