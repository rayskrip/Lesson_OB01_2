# 1. Создай класс `Store`:
#  -Атрибуты класса:
# - `name`: название магазина.
# - `address`: адрес магазина.
# - `items`: словарь, где ключ - название товара, а значение - его цена. Например, `{'apples': 0.5, 'bananas': 0.75}`.
# - Методы класса:
# - `__init__ - конструктор, который инициализирует название и адрес, а также пустой словарь для `items`.
# -  метод для добавления товара в ассортимент.
# - метод для удаления товара из ассортимента.
# - метод для получения цены товара по его названию. Если товар отсутствует, возвращайте `None`.
# - метод для обновления цены товара.
# 2. Создай несколько объектов класса `Store`:
# Создай не менее трех различных магазинов с разными названиями, адресами и добавь в каждый из них несколько товаров.
# 3. Протестировать методы:
# Выбери один из созданных магазинов и протестируй все его методы:
# добавь товар, обнови цену, убери товар и запрашивай цену.

class Store():
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price
        print(f"Товар '{item_name}' добавлен по цене {price}.")

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар '{item_name}' удален из ассортимента.")
        else:
            print(f"Товар '{item_name}' не найден.")

    def get_item_price(self, item_name):
        return self.items.get(item_name, None)

    def update_item_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена товара '{item_name}' обновлена до {new_price}.")
        else:
            print(f"Товар '{item_name}' не найден в ассортименте.")


# Создание объектов класса Store
store1 = Store("Веган", "ул. Абрикосовая, 1")
store1.add_item("яблоки", 120)
store1.add_item("бананы", 150)

store2 = Store("Мясные продукты", "ул. Мясницкая, 10")
store2.add_item("говядина", 1000)
store2.add_item("курица", 700)

store3 = Store("Молоко", "ул. Молочная, 5")
store3.add_item("молоко", 100)
store3.add_item("сыр", 1200)

# Тест
print(f"Товары в {store1.name}: {store1.items}")
store1.update_item_price("яблоки", 100)
print("Цена яблок после обновления:", store1.get_item_price("яблоки"))
store1.remove_item("бананы")
print(f"Товары в {store1.name} после удаления: {store1.items}")
