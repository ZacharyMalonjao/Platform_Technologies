The Repository contains three folders, with the raw_dataset folder as the  main datasource. 
Our data pipeline has 2 stages of cleaning, one is API-level cleaning and second is ETL-level cleaning.

The API-level cleaning is found in the filtered_datasets folder.

The ETL-level cleaning is in the transformed_datasets folder.

Each folder contains one Jupyter notebook containing the code, and three csvs that were modified as a result.

PLATFORM_TECHNOLOGIES/
├── filtered_datasets/
│   ├── api_simulated_cleaning.ipynb
│   ├── event_logs(1).csv
│   ├── marketing_summary(1).csv
│   └── trend_report(1).csv
├── raw_datasets/
│   ├── event_logs.csv
│   ├── marketing_summary.csv
│   └── trend_report.csv
├── transformed_datasets/
│   ├── event_logs_forecast.csv
│   ├── marketing_summary_forecast.csv
│   ├── transforming.ipynb
│   ├── trend_report_forecast.csv
│   └── user_segments.csv
└── README.md
