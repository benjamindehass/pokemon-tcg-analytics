CREATE TABLE IF NOT EXISTS 'dim_cards'(
    card_id STRING NOT NULL,          -- Primary Key
    card_name STRING,
    set_id STRING,                    
    set_name STRING,
    release_date DATE,
    rarity STRING,
    card_type STRING,
    illustrator STRING
);