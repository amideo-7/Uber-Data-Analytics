# Uber-Data-Analytics

## Introduction:

This project involved developing an end-to-end data analytics pipeline to process and analyze NYC Taxi and Limousine Commission data. The project utilized the following tools and technologies:

* NYC Taxi and Limousine Commission's TLC Trip Record dataset for Uber data
* Google Cloud Storage bucket for data storage
* Mage-AI for data pipeline creation
* Google Cloud Platform's VM as a compute engine
* Google Cloud BigQuery for data storage and analytics
* Google Looker Studio for interactive dashboard creation

The project successfully generated insights from the Uber data, providing valuable information for decision-making purposes.

## Architecture:

<div align="center>

<img src="https://github.com/amideo-7/Uber-Data-Analytics/blob/03c26acf644d2e8790a64f67a38a17bcb0497b9c/architecture.png" />

</div>

## Dataset:

Yellow and green taxi trip records include fields capturing pick-up and drop-off dates/times, pick-up and drop-off locations, trip distances, itemized fares, rate types, payment types, and driver-reported passenger counts. The data used in the attached datasets were collected and provided to the NYC Taxi and Limousine Commission (TLC) by technology providers authorized under the Taxicab & Livery Passenger Enhancement Programs (TPEP/LPEP).

* Link to Dataset: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page

* Link to Data Dictionary: https://www.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf

## Data Model:

The data model contains 1 fact table and 7 dimension tables describing different dimensions of the dataset. The dimension tables are as follows:

* Pickup Location Dimension
* Dropoff Location Dimension
* Datetime Dimension
* Passenger Count Dimension
* Trip Distance Dimension
* RateCode Dimension
* Payment Type Dimension

<div align="center>

<img src="https://github.com/amideo-7/Uber-Data-Analytics/blob/03c26acf644d2e8790a64f67a38a17bcb0497b9c/dataModel.png" />

</div>

## Data Pipeline:

The data pipeline consists of three main stages:

* **Data Load:** This stage ingests raw data from its source. The data is loaded from a Google Cloud Storage bucket which is used for temporary storage.

* **Data Transform:** This stage processes the raw data. The data is transformed according to a predefined data model, involving tasks such as cleaning, filtering, and aggregating the data.

* **Data Export:** This stage exports the transformed data to Google Cloud BigQuery, a data warehouse. The data is stored in structured tables, enabling efficient analysis and visualization.

<div align="center>

<img src="https://github.com/amideo-7/Uber-Data-Analytics/blob/03c26acf644d2e8790a64f67a38a17bcb0497b9c/mageDataPipelineDashboard.png" />

</div>

<div align="center>

<img src="https://github.com/amideo-7/Uber-Data-Analytics/blob/03c26acf644d2e8790a64f67a38a17bcb0497b9c/mageDataPipelineArchitecture.png" />

</div>

