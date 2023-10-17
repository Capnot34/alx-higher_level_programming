-- script to get full description of the table first_table from hbtn_0c_0
SELECT 
    'first_table' AS 'Table', 
    COLUMN_NAME AS 'Column', 
    COLUMN_TYPE AS 'Type', 
    IS_NULLABLE AS 'Nullable', 
    COLUMN_DEFAULT AS 'Default', 
    COLUMN_KEY AS 'Key', 
    EXTRA AS 'Extra' 
FROM 
    information_schema.COLUMNS 
WHERE 
    TABLE_SCHEMA = 'hbtn_0c_0' AND TABLE_NAME = 'first_table';

-- Retrieve the create statement
SELECT 
    'first_table' AS 'Table',
    TABLE_COMMENT AS 'Create Table' 
FROM 
    information_schema.TABLES 
WHERE 
    TABLE_SCHEMA = 'hbtn_0c_0' AND TABLE_NAME = 'first_table';
