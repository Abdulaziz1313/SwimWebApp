
CREATE TABLE times (
            swimmer_id integer not null,  
            event_id integer not null,
            time varchar(64) not null,
            ts timestamp default current_timestamp
        );
CREATE TABLE swimmers (
        id integer not null primary key auto_increment,
        name varchar(64) not null,
        age integer not null
    );
CREATE TABLE events (
            id integer not null primary key auto_increment,
            distance varchar(64) not null,
            stroke varchar(64) not null
        );

