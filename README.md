\# AOI Weather Data API



This API accepts an Excel file and returns weather data as JSON.



\## How to Use



1\. Run: `uvicorn app:app --reload`

2\. POST Excel file to `/upload` with `file` field

3\. Get JSON like: `{ "2024-07-21": "Sunny", ... }`



