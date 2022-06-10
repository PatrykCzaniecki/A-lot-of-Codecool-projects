SELECT category_name AS category, COUNT (category_name) AS number_of_products
FROM categories
JOIN products
ON categories.category_id = products.category_id
GROUP BY category_name
ORDER BY number_of_products DESC