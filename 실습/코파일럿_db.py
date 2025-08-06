import sqlite3
import random

class ElectronicsDB:
    def __init__(self, db_name="electronics.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS products (
                    product_id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    price INTEGER NOT NULL
                )
            """)

    def insert_product(self, product_id, name, price):
        with self.conn:
            self.conn.execute(
                "INSERT INTO products (product_id, name, price) VALUES (?, ?, ?)",
                (product_id, name, price)
            )

    def update_product(self, product_id, name=None, price=None):
        with self.conn:
            if name and price:
                self.conn.execute(
                    "UPDATE products SET name=?, price=? WHERE product_id=?",
                    (name, price, product_id)
                )
            elif name:
                self.conn.execute(
                    "UPDATE products SET name=? WHERE product_id=?",
                    (name, product_id)
                )
            elif price:
                self.conn.execute(
                    "UPDATE products SET price=? WHERE product_id=?",
                    (price, product_id)
                )

    def delete_product(self, product_id):
        with self.conn:
            self.conn.execute(
                "DELETE FROM products WHERE product_id=?",
                (product_id,)
            )

    def select_products(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM products")
        return cursor.fetchall()

    def close(self):
        self.conn.close()

# 샘플 데이터 100개 생성 및 삽입
def generate_sample_data(db):
    for i in range(1, 101):
        name = f"전자제품_{i}"
        price = random.randint(10000, 1000000)
        db.insert_product(i, name, price)

if __name__ == "__main__":
    db = ElectronicsDB()
    generate_sample_data(db)
    products = db.select_products()
    for p in products:
        print(p)