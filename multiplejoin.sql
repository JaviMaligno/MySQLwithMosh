USE sql_store;

SELECT o.order_id, o.order_date, c.first_name, c.last_name, os.name AS status
FROM orders o 
JOIN customers c 
	ON o.customer_id = c.customer_id
JOIN order_statuses os 
	ON o.status = os.order_status_id;
    
    
SELECT 
	o.order_date, 
    o.order_id, 
    c.first_name AS customer, 
    sh.name AS shipper, 
    os.name AS status
FROM orders o
JOIN customers c
	ON o.customer_id = c.customer_id
JOIN order_statuses os
	ON o.status = os.order_status_id
LEFT JOIN shippers sh 
	ON o.shipper_id = sh.shipper_id;