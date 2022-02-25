SELECT customers.company_name, COUNT(customers.customer_id) AS orders,
STRING_AGG(orders.order_id ::varchar,',') AS order_ids
FROM customers
JOIN orders
ON customers.customer_id = orders.customer_id
WHERE country = 'USA'
GROUP BY customers.customer_id
HAVING COUNT(customers.customer_id) < 5
ORDER BY orders ASC