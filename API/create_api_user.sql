CREATE DATABASE store CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE USER 'api'@'localhost' IDENTIFIED BY 'api_database_password';

GRANT ALL PRIVILEGES ON store.* TO 'api'@'localhost';

FLUSH PRIVILEGES;