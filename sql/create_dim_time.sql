CREATE TABLE IF NOT EXISTS 'dim_time' (
    time_id INT64 NOT NULL,           -- Primary Key
    date DATE,
    day_of_week STRING,
    day_of_month INT64,
    month INT64,
    year INT64,
    is_weekend BOOL
)
;