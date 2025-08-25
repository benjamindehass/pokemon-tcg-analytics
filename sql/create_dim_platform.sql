CREATE TABLE IF NOT EXISTS 'dim_platform' (
    platform_id STRING NOT NULL,      -- Primary Key
    platform_name STRING,
    website_url STRING,
    fees_percentage FLOAT64
)
;