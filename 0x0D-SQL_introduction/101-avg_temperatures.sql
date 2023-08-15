-- Display average city temperatures (Fahrenheit) sorted by temperature (descending)
SELECT city,
    AVG(value) AS avg_temp
FROM temperatures
GROUP by CITY
ORDER BY avg_temp DESC;