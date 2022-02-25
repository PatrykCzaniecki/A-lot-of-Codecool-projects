SELECT product_name, ROUND(SUM((order_details.unit_price*quantity)-(order_details.unit_price*quantity*discount))) AS sum
FROM order_details
JOIN products
ON order_details.product_id = products.product_id
GROUP BY product_name
ORDER BY sum ASC
LIMIT 10