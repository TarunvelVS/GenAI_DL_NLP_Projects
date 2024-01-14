import sqlite3

connection = sqlite3.connect("sample.db")

cursor = connection.cursor()

# Create Products table
table_info_1 = """
CREATE TABLE Products (
    ProductID INTEGER PRIMARY KEY,
    Name TEXT,
    Description TEXT,
    Price REAL,
    Stock INTEGER
); """
cursor.execute(table_info_1)

# Create Users table
table_info_2 = """
CREATE TABLE Users (
    UserID INTEGER PRIMARY KEY,
    Username TEXT UNIQUE,
    Password TEXT,
    Email TEXT UNIQUE,
    CreatedAt TEXT
);
"""
cursor.execute(table_info_2)

# Create Orders table
table_info_3 = """
CREATE TABLE Orders (
    OrderID INTEGER PRIMARY KEY,
    UserID INTEGER,
    OrderDate TEXT,
    TotalAmount REAL,
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
);
"""
cursor.execute(table_info_3)

# Create OrderDetails table
table_info_4 = """
CREATE TABLE OrderDetails (
    OrderDetailID INTEGER PRIMARY KEY,
    OrderID INTEGER,
    ProductID INTEGER,
    Quantity INTEGER,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);
"""
cursor.execute(table_info_4)

insert_info_1 ="""
INSERT INTO Products (ProductID, Name, Description, Price, Stock) VALUES
(1, 'Smartphone', 'Latest model smartphone with advanced features', 699.99, 50),
(2, 'Laptop', 'Lightweight, high-performance laptop', 999.99, 30),
(3, 'Headphones', 'Wireless headphones with noise cancellation', 199.99, 100),
(4, 'Smartwatch', 'Water-resistant smartwatch with health tracking', 299.99, 40),
(5, 'Camera', 'Digital camera with high-resolution lens', 549.99, 20),
(6, 'Bluetooth Speaker', 'Portable Bluetooth speaker with surround sound', 129.99, 60),
(7, 'Tablet', '10-inch tablet with high-resolution display', 449.99, 35),
(8, 'Gaming Console', 'Latest gaming console with VR support', 499.99, 25),
(9, 'E-reader', 'Lightweight e-reader with paper-like display', 129.99, 80),
(10, 'Fitness Tracker', 'Waterproof fitness tracker with heart rate monitor', 99.99, 70);
"""
insert_info_2 = """
INSERT INTO Users (UserID, Username, Password, Email, CreatedAt) VALUES
(1, 'john_doe', 'password123', 'john.doe@example.com', '2024-01-01'),
(2, 'jane_smith', 'password123', 'jane.smith@example.com', '2024-01-02'),
(3, 'alice_jones', 'password123', 'alice.jones@example.com', '2024-01-03'),
(4, 'bob_brown', 'password123', 'bob.brown@example.com', '2024-01-04'),
(5, 'charlie_davis', 'password123', 'charlie.davis@example.com', '2024-01-05'),
(6, 'diana_clark', 'password123', 'diana.clark@example.com', '2024-01-06'),
(7, 'edward_martin', 'password123', 'edward.martin@example.com', '2024-01-07'),
(8, 'fiona_lewis', 'password123', 'fiona.lewis@example.com', '2024-01-08'),
(9, 'george_hall', 'password123', 'george.hall@example.com', '2024-01-09'),
(10, 'hannah_scott', 'password123', 'hannah.scott@example.com', '2024-01-10');
"""

insert_info_3 = """
INSERT INTO Orders (OrderID, UserID, OrderDate, TotalAmount) VALUES
(1, 1, '2024-01-12', 699.99),
(2, 2, '2024-01-12', 1299.98),
(3, 3, '2024-01-12', 199.99),
(4, 4, '2024-01-12', 299.99),
(5, 5, '2024-01-12', 549.99),
(6, 6, '2024-01-12', 129.99),
(7, 7, '2024-01-12', 449.99),
(8, 8, '2024-01-12', 499.99),
(9, 9, '2024-01-12', 129.99),
(10, 10, '2024-01-12', 99.99);
"""

insert_info_4 = """
INSERT INTO OrderDetails (OrderDetailID, OrderID, ProductID, Quantity) VALUES
(1, 1, 1, 1),
(2, 2, 2, 1),
(3, 2, 3, 1),
(4, 3, 3, 1),
(5, 4, 4, 1),
(6, 5, 5, 1),
(7, 6, 6, 1),
(8, 7, 7, 1),
(9, 8, 8, 1),
(10, 9, 9, 1),
(11, 10, 10, 1);

"""

cursor.execute(insert_info_1)
cursor.execute(insert_info_2)
cursor.execute(insert_info_3)
cursor.execute(insert_info_4)

data = cursor.execute("SELECT * FROM Products")

for row in data:
    print(row)


connection.commit()

connection.close()