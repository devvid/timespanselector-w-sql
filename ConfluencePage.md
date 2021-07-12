# Timespan Selector SQL

The timespan selector widget enables users a new method to search through large datasets by selecting a date range and timespan over the selected days. The design includes a calender view which enables a date range selection, the time duration is configured by selecting a "from time" and a "to time" in the format hh:mm:ss.

![Timespan selector design](6-Example.png)

## SQL Query

The core SQL statement to use to query the data base is detailed below.

```sql
select * from <table_name> where created::timestamp::date BETWEEN '2020-05-06' AND '2020-05-10' and created::time BETWEEN '00:30:00' AND '01:30:00'
```

The frontend application simply needs to capture the users data range selection & timerange and then pass to the backend to formated into the correct SQL statment.
