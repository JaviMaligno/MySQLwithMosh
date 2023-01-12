-- count how many times each product has been ordered

SELECT p.product_id, p.name, SUM(COALESCE(oi.quantity,0))
FROM products p 
LEFT JOIN order_items oi
ON oi.product_id = p.product_id
GROUP BY p.product_id