-- import in hbtn_0c_0 database the temperatures database

SELECT city, AVG(value) 'avg_temp' FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
