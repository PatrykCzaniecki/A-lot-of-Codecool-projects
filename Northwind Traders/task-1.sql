SELECT product_name AS product, company_name AS company
FROM products
JOIN suppliers
ON products.supplier_id = suppliers.supplier_id
ORDER BY product_name ASC