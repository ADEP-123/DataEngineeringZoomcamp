#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from sqlalchemy import create_engine

df1 = pd.read_csv("taxi_zone_lookup.csv")

dtype = {
    "VendorID": "Int64",
    "passenger_count": "Int64",
    "trip_distance": "float64",
    "RatecodeID": "Int64",
    "store_and_fwd_flag": "string",
    "PULocationID": "Int64",
    "DOLocationID": "Int64",
    "payment_type": "Int64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "congestion_surcharge": "float64"
}

df2 = pd.read_parquet("green_tripdata_2025-11.parquet")
df2 = df2.astype(dtype)

engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')

df2.head(0).to_sql(name='trip_data', con=engine, if_exists='append')
df2.to_sql(name='trip_data', con=engine, if_exists='append')

df1.head(0).to_sql(name='taxi_zone', con=engine, if_exists='append')
df1.to_sql(name='taxi_zone', con=engine, if_exists='append')






