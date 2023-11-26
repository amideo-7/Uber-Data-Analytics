CREATE OR REPLACE TABLE
uberdataanalytics-405417.uber_data_analytics.analytics_table AS(
  SELECT
    fact_table.trip_id,
    fact_table.VendorID,
    datetime_dim.tpep_pickup_datetime,
    datetime_dim.tpep_dropoff_datetime,
    passenger_count_dim.passenger_count,
    trip_distance_dim.trip_distance,
    ratecode_dim.ratecode_name,
    pickup_location_dim.pickup_longitude,
    pickup_location_dim.pickup_latitude,
    dropoff_location_dim.dropoff_longitude,
    dropoff_location_dim.dropoff_latitude,
    payment_type_dim.payment_name,
    fact_table.fare_amount,
    fact_table.extra,
    fact_table.mta_tax,
    fact_table.tip_amount,
    fact_table.tolls_amount,
    fact_table.improvement_surcharge,
    fact_table.total_amount
  FROM
    uberdataanalytics-405417.uber_data_analytics.fact_table
    JOIN uberdataanalytics-405417.uber_data_analytics.datetime_dim 
      ON fact_table.datetime_id = datetime_dim.datetime_id
    JOIN uberdataanalytics-405417.uber_data_analytics.dropoff_location_dim
      ON fact_table.dropoff_location_id = dropoff_location_dim.dropoff_location_id
    JOIN uberdataanalytics-405417.uber_data_analytics.passenger_count_dim 
      ON fact_table.passenger_count_id = passenger_count_dim.passenger_count_id
    JOIN uberdataanalytics-405417.uber_data_analytics.payment_type_dim 
      ON fact_table.payment_type_id = payment_type_dim.payment_type_id
    JOIN uberdataanalytics-405417.uber_data_analytics.pickup_location_dim 
      ON fact_table.pickup_location_id = pickup_location_dim.pickup_location_id
    JOIN uberdataanalytics-405417.uber_data_analytics.ratecode_dim
      ON fact_table.ratecode_id = ratecode_dim.ratecode_id
    JOIN uberdataanalytics-405417.uber_data_analytics.trip_distance_dim
      ON fact_table.trip_distance_id = trip_distance_dim.trip_distance_id
);
