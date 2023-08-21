-- Display average temperatures
SELECT city, AVG(value) FROM temperatures as avg_temp ORDER BY avg_temp DESC;
