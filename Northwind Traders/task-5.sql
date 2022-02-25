SELECT EXTRACT (year FROM orders.order_date) AS year,
EXTRACT (month FROM orders.order_date) AS month,
COUNT(orders.order_id) AS order_count,
ROUND(SUM((order_details.unit_price*quantity)-(order_details.unit_price*quantity*discount))) AS revenue
FROM orders, order_details
WHERE EXTRACT (year FROM orders.order_date) = 1997
AND orders.order_id = order_details.order_id
GROUP BY EXTRACT (year FROM orders.order_date), EXTRACT(month FROM orders.order_date)