-- Задача №1

SELECT 
    product_name
FROM products 
WHERE unit_price BETWEEN 3 and 6;

-- Задача №2

SELECT
   min(unit_price) as min_price
FROM products 
WHERE category_id = 1; 

-- Задача №3

SELECT 
    supplier_id,
    max(unit_price) 
FROM products
WHERE supplier_id = 1 
    or supplier_id = 3
    or supplier_id = 5
GROUP BY supplier_id
ORDER BY supplier_id;
