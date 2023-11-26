import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(df, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here

    #Converting the object datatype to datetime datatype
    df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
    df['tpep_dropoff_datetime'] =pd.to_datetime(df['tpep_dropoff_datetime'])

    #Dropping the duplicate columns
    df = df.drop_duplicates().reset_index(drop=True)
    df['trip_id'] = df.index

    #Creating datetime dimension table
    datetime_dim = df[['tpep_pickup_datetime','tpep_dropoff_datetime']].reset_index(drop=True)
    datetime_dim['tpep_pickup_datetime'] = datetime_dim['tpep_pickup_datetime']
    datetime_dim['pickup_hour'] = datetime_dim['tpep_pickup_datetime'].dt.hour
    datetime_dim['pickup_day'] = datetime_dim['tpep_pickup_datetime'].dt.day
    datetime_dim['pickup_month'] = datetime_dim['tpep_pickup_datetime'].dt.month
    datetime_dim['pickup_year'] = datetime_dim['tpep_pickup_datetime'].dt.year
    datetime_dim['pickup_weekday'] = datetime_dim['tpep_pickup_datetime'].dt.weekday

    datetime_dim['tpep_dropoff_datetime'] = datetime_dim['tpep_dropoff_datetime']
    datetime_dim['drop_hour'] = datetime_dim['tpep_dropoff_datetime'].dt.hour
    datetime_dim['drop_day'] = datetime_dim['tpep_dropoff_datetime'].dt.day
    datetime_dim['drop_month'] = datetime_dim['tpep_dropoff_datetime'].dt.month
    datetime_dim['drop_year'] = datetime_dim['tpep_dropoff_datetime'].dt.year
    datetime_dim['drop_weekday'] = datetime_dim['tpep_dropoff_datetime'].dt.weekday

    datetime_dim['datetime_id'] = datetime_dim.index
    datetime_dim = datetime_dim[['datetime_id', 'tpep_pickup_datetime', 'pickup_hour', 
                                'pickup_day', 'pickup_month', 'pickup_year', 'pickup_weekday',
                                'tpep_dropoff_datetime', 'drop_hour', 'drop_day', 'drop_month',
                                'drop_year', 'drop_weekday']]


    #Creating passenger count dimension table
    passenger_count_dim = df[['passenger_count']].reset_index(drop=True)
    passenger_count_dim['passenger_count_id'] = passenger_count_dim.index
    passenger_count_dim = passenger_count_dim[['passenger_count_id', 'passenger_count']]

    #Creating trip diatance dimension table
    trip_distance_dim = df[['trip_distance']].reset_index(drop=True)
    trip_distance_dim['trip_distance_id'] = trip_distance_dim.index
    trip_distance_dim = trip_distance_dim[['trip_distance_id', 'trip_distance']]

    #Creating pickup location dimension table
    pickup_location_dim = df[['pickup_longitude', 'pickup_latitude']].reset_index(drop=True)
    pickup_location_dim['pickup_location_id'] = pickup_location_dim.index
    pickup_location_dim = pickup_location_dim[['pickup_location_id', 'pickup_longitude', 'pickup_latitude']]

    #Creating dropoff location dimension table
    dropoff_location_dim = df[['dropoff_longitude', 'dropoff_latitude']].reset_index(drop=True)
    dropoff_location_dim['dropoff_location_id'] = dropoff_location_dim.index
    dropoff_location_dim = dropoff_location_dim[['dropoff_location_id', 'dropoff_longitude', 'dropoff_latitude']]

    #Creating ratecode dimension table
    ratecode_type = {
        1:'Standard rate',
        2:'JFK',
        3:'Newark',
        4:'Nassau or Westchester',
        5:'Negotiated fare',
        6:'Group ride'
    }
    ratecode_dim = df[['RatecodeID']].reset_index(drop=True)
    ratecode_dim['ratecode_id'] = ratecode_dim.index
    ratecode_dim['ratecode_name'] = ratecode_dim['RatecodeID'].map(ratecode_type)
    ratecode_dim = ratecode_dim[['ratecode_id', 'RatecodeID', 'ratecode_name']]

    #Creating payment type dimension table
    payment_type_name = {
        1:'Credit card',
        2:'Cash',
        3:'No charge',
        4:'Dispute',
        5:'Unknown',
        6:'Voided trip'
    }

    payment_type_dim = df[['payment_type']].reset_index(drop=True)
    payment_type_dim['payment_type_id'] = payment_type_dim.index
    payment_type_dim['payment_name'] = payment_type_dim['payment_type'].map(payment_type_name)
    payment_type_dim = payment_type_dim[['payment_type_id', 'payment_type', 'payment_name']]

    #Creating fact table
    fact_table = df.merge(passenger_count_dim, left_on='trip_id', right_on='passenger_count_id') \
                .merge(trip_distance_dim, left_on='trip_id', right_on='trip_distance_id') \
                .merge(ratecode_dim, left_on='trip_id', right_on='ratecode_id') \
                .merge(pickup_location_dim, left_on='trip_id', right_on='pickup_location_id') \
                .merge(dropoff_location_dim, left_on='trip_id', right_on='dropoff_location_id')\
                .merge(datetime_dim, left_on='trip_id', right_on='datetime_id') \
                .merge(payment_type_dim, left_on='trip_id', right_on='payment_type_id') \
                [['trip_id', 'VendorID', 'datetime_id', 'passenger_count_id', 'trip_distance_id', 
                'pickup_location_id', 'ratecode_id', 'store_and_fwd_flag', 'dropoff_location_id', 
                'payment_type_id', 'fare_amount', 'extra', 'mta_tax', 'tip_amount', 'tolls_amount', 
                'improvement_surcharge', 'total_amount']]


    return {"datetime_dim":datetime_dim.to_dict(orient="dict"),
            "passenger_count_dim":passenger_count_dim.to_dict(orient="dict"),
            "trip_distance_dim":trip_distance_dim.to_dict(orient="dict"),
            "pickup_location_dim":pickup_location_dim.to_dict(orient="dict"),
            "dropoff_location_dim":dropoff_location_dim.to_dict(orient="dict"),
            "ratecode_dim":ratecode_dim.to_dict(orient="dict"),
            "payment_type_dim":payment_type_dim.to_dict(orient="dict"),
            "fact_table":fact_table.to_dict(orient="dict")}


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
