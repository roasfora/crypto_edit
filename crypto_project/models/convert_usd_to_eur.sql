WITH bitcoin_prices_cleaned AS (
    SELECT
        TO_TIMESTAMP(SPLIT_PART(timestamp, ' GMT', 1), 'Dy, DD Mon YYYY HH24:MI:SS') AS btc_timestamp,
        CAST(price AS FLOAT) AS btc_price,
        currency
    FROM {{ source('crypto_data', 'bitcoin_prices') }}
),

eur_to_usd_rates_cleaned AS (
    SELECT
        TO_TIMESTAMP(SPLIT_PART(timestamp, ' GMT', 1), 'Dy, DD Mon YYYY HH24:MI:SS') AS rate_timestamp,
        CAST(eur_to_usd_rate AS FLOAT) AS eur_to_usd_rate
    FROM {{ source('crypto_data', 'eur_to_usd_rates') }}
),

matched_data AS (
    SELECT
        btc.btc_timestamp,
        btc.btc_price,
        btc.currency,
        rate.eur_to_usd_rate,
        rate.rate_timestamp
    FROM bitcoin_prices_cleaned btc
    LEFT JOIN LATERAL (
        SELECT eur_to_usd_rate, rate_timestamp
        FROM eur_to_usd_rates_cleaned rate
        WHERE rate.rate_timestamp <= btc.btc_timestamp
        ORDER BY rate.rate_timestamp DESC
        LIMIT 1
    ) rate ON TRUE
),

converted_data AS (
    SELECT
        btc_timestamp,
        btc_price,
        btc_price / eur_to_usd_rate AS price_in_eur,
        currency,
        eur_to_usd_rate,
        rate_timestamp
    FROM matched_data
)

SELECT *
FROM converted_data
