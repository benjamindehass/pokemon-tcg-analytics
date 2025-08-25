CREATE TABLE IF NOT EXISTS 'dim_seller' (
    seller_id STRING NOT NULL,        -- Primary Key
    seller_name STRING,
    reputation_score INT64,
    location STRING
)
;