class clientSql:
    GET = "SELECT * FROM client Where CIF = {}"
    INSERT = "INSERT INTO client (CIF, Name, LastName, Link, age, isAdult) values ('{}', '{}', '{}', '{}', '{}', '{}')"