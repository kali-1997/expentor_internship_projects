
CREATE DATABASE IF NOT EXISTS sales_db;
USE sales_db;

CREATE TABLE IF NOT EXISTS sales (
    order_id VARCHAR(20),
    country VARCHAR(50),
    category VARCHAR(50),
    device_type VARCHAR(20),
    customer_name VARCHAR(100),
    sales_manager VARCHAR(100),
    sales_rep VARCHAR(100),
    estimate_order_val FLOAT,
    cost FLOAT,
    profit FLOAT,
    order_date DATE
);
