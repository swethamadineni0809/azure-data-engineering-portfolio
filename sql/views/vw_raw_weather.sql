CREATE OR ALTER VIEW vw_raw_weather AS
SELECT
    JSON_VALUE(r.jsonContent, '$.name') AS city,
    CAST(JSON_VALUE(r.jsonContent, '$.main.temp') AS FLOAT) AS temperature,
    JSON_VALUE(r.jsonContent, '$.weather[0].description') AS description,
    CAST(JSON_VALUE(r.jsonContent, '$.dt') AS BIGINT) AS event_time
FROM OPENROWSET(
    BULK 'raw/*/*/*/*.json',
    DATA_SOURCE = 'adls_raw',
    FORMAT = 'CSV',
    FIELDTERMINATOR = '0x0b',
    FIELDQUOTE = '0x0b'
)
WITH (
    jsonContent NVARCHAR(MAX)
) AS r
WHERE ISJSON(r.jsonContent) = 1;
