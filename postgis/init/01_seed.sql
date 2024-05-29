CREATE EXTENSION IF NOT EXISTS postgis;

CREATE OR REPLACE FUNCTION load_csv(table_name TEXT, file_path TEXT)
RETURNS VOID AS $$
BEGIN
    EXECUTE format('
        CREATE TABLE IF NOT EXISTS %I (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255),
            latitude DECIMAL,
            longitude DECIMAL
        )', table_name);

    EXECUTE format('
        COPY %I (
            name,
            latitude, 
            longitude
        )
        FROM %L
        DELIMITER '',''
        CSV;', table_name, file_path);
END;
$$ LANGUAGE plpgsql;

SELECT load_csv('points_of_interest', '/data/points-of-interest.csv');
SELECT load_csv('destinations', '/data/destinations.csv');
SELECT load_csv('start', '/data/start.csv');