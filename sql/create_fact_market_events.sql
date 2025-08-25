CREATE TABLE IF NOT EXISTS 'fact_market_events' (
    event_id STRING NOT NULL,          -- Primary Key
    card_id STRING,                    -- Foreign Key to dim_card
    seller_id STRING,                  -- Foreign Key to dim_seller
    time_id INT64,                     -- Foreign Key to dim_time
    platform_id STRING,                -- Foreign Key to dim_platform
    market_price FLOAT64,
    listing_price FLOAT64,
    quantity INT64,
    total_sale_value FLOAT64,
    event_timestamp TIMESTAMP
)
PARTITION BY DATE(event_timestamp)    -- Partition by date to optimize time-based queries
CLUSTER BY card_id, platform_id       -- Cluster by these keys to improve performance for filtering
;