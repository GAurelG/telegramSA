# database creation and initial setup

The postgres container was created to start a database named teledb with the same db name in the tests.

## connecting using psql

To have the psql client on the linux client we have to install packages related to postgres, either the postgres package, or it might exist a postgres-client package.

`psql -h localhost -U teledb -d teledb`

then enter the password for the db user.

## Create the schema and initial table

one database management system can contain several database with some user allowed to connect (or not) to them.
In each database, you can create multiple schema, one schema contains table that can be linked together.
Once we create the schema, we need to add it to the search_path so that the psql command gives us the information 
we are looking for. We need to reference all schema we want in it. `SHOW search_path` does exactly what it says.

    ```CREATE SCHEMA chatdenorm;```
    ```
    CREATE TABLE chatdenorm.fiau1(
        id SERIAL PRIMARY KEY,
        chat VARCHAR(50),
        messageID INTEGER,
        sender VARCHAR(20),
        message TEXT,
        hastags TEXT,
        links TEXT,
        media TEXT,
        raw_message TEXT
    );
    ```
    ```SET search_path TO chatdenorm, public;```

We create a composite ID as combination of chat and messageID as we don't know if the messageID given by the export is unique across all chats, or only across one chat. 

Could create a more normalised version to have the hastags and links accessible via a join.
In this chat I will only have a few members, usually 2 so no need to normalize users.
Same for the chat, I envision to only work on one chat first. We can think of having several later.
Having multiple chat could help explore correlation between chats sentiments and maybe improve the evaluation.


    ```CREATE SCHEMA chatjoin;```
    ```
    CREATE TABLE chatjoin.fiau1(
        id SERIAL PRIMARY KEY,
        chat VARCHAR(50),
        messageID INTEGER,
        sender VARCHAR(20),
        message TEXT,
        media TEXT,
        raw_message TEXT
    );

    CREATE TABLE chatjoin.hastags(
        id SERIAL PRIMARY KEY,
        message_id INTEGER REFERENCES fiau1(id),
        hashtag VARCHAR(100)
    );

    CREATE TABLE chatjoin.links(
       id SERIAL PRIMARY KEY,
       message_id INTEGER REFERENCES fiau1(id),
       links TEXT
    );

    ```
