create a file named db.cnf at project root folder
add db details in file like below format
--------------------------------------------------

[client]
database = LittleLemon
host = localhost
user = <username>
password = <password>
default-character-set = utf8

------------------------------------
In project sub-folder create a .env file and add a key named SECRET_KEY in the file
SECRET_KEY= <any big string>

if above is not working modify setting.py as needed.

/restaurant/api-token-auth/
/restaurant/booking/tables
/restaurant/
/restaurant/menu/
/restaurant/menu/:id



