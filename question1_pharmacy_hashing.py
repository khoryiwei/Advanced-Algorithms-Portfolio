import time


class Medicine:
    def __init__(self, medicine_id, name, category, price, quantity):
        self.medicine_id = medicine_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return (
            f"ID: {self.medicine_id} | "
            f"Name: {self.name} | "
            f"Category: {self.category} | "
            f"Price: RM{self.price:.2f} | "
            f"Quantity: {self.quantity}"
        )


class HashTable:
    def __init__(self, size=23):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, medicine):
        index = self.hash_function(medicine.medicine_id)
        start_index = index

        while self.table[index] is not None:
            if self.table[index].medicine_id == medicine.medicine_id:
                self.table[index] = medicine
                return True

            index = (index + 1) % self.size

            if index == start_index:
                print("Hash table is full. Cannot insert new medicine.")
                return False

        self.table[index] = medicine
        return True

    def search(self, medicine_id):
        index = self.hash_function(medicine_id)
        start_index = index

        while self.table[index] is not None:
            if self.table[index].medicine_id == medicine_id:
                return self.table[index]

            index = (index + 1) % self.size

            if index == start_index:
                break

        return None

    def display(self):
        print("\n========== Pharmacy Hash Table ==========")
        for index, medicine in enumerate(self.table):
            if medicine is None:
                print(f"Bucket {index}: Empty")
            else:
                print(f"Bucket {index}: {medicine}")


def linear_array_search(medicine_array, medicine_id):
    for medicine in medicine_array:
        if medicine.medicine_id == medicine_id:
            return medicine
    return None


def create_sample_data():
    return [
        Medicine(101, "Paracetamol", "Tablet", 6.50, 120),
        Medicine(202, "Cough Syrup", "Syrup", 12.90, 40),
        Medicine(303, "Vitamin C", "Supplement", 18.00, 75),
        Medicine(404, "Antacid", "Tablet", 9.50, 60),
        Medicine(505, "Ibuprofen", "Tablet", 8.80, 95),
        Medicine(606, "Eye Drops", "Drops", 14.20, 30),
        Medicine(707, "Allergy Relief", "Tablet", 11.50, 45),
        Medicine(808, "Hand Sanitizer", "External Use", 7.90, 100),
        Medicine(909, "Antiseptic Cream", "Cream", 10.70, 35),
        Medicine(110, "Oral Rehydration Salt", "Powder", 5.20, 85)
    ]


def performance_test(hash_table, medicine_array):
    search_keys = [101, 303, 505, 808, 110, 999, 888, 777, 666, 555]

    hash_total_time = 0
    array_total_time = 0

    print("\n========== Search Performance Test ==========")
    print("Search keys include existing and non-existing medicine IDs.\n")

    print("{:<12} {:<20} {:<20}".format("Medicine ID", "Hash Table (ns)", "Array Search (ns)"))
    print("-" * 55)

    for key in search_keys:
        start = time.perf_counter_ns()
        hash_table.search(key)
        end = time.perf_counter_ns()
        hash_time = end - start
        hash_total_time += hash_time

        start = time.perf_counter_ns()
        linear_array_search(medicine_array, key)
        end = time.perf_counter_ns()
        array_time = end - start
        array_total_time += array_time

        print("{:<12} {:<20} {:<20}".format(key, hash_time, array_time))

    print("-" * 55)
    print(f"Total Hash Table Search Time: {hash_total_time} ns")
    print(f"Total Array Search Time: {array_total_time} ns")
    print(f"Average Hash Table Search Time: {hash_total_time / len(search_keys):.2f} ns")
    print(f"Average Array Search Time: {array_total_time / len(search_keys):.2f} ns")


def insert_new_medicine(hash_table, medicine_array):
    try:
        medicine_id = int(input("Enter Medicine ID: "))
        name = input("Enter Medicine Name: ")
        category = input("Enter Category: ")
        price = float(input("Enter Price (RM): "))
        quantity = int(input("Enter Quantity: "))

        medicine = Medicine(medicine_id, name, category, price, quantity)
        inserted = hash_table.insert(medicine)

        if inserted:
            medicine_array.append(medicine)
            print("Medicine inserted successfully.")

    except ValueError:
        print("Invalid input. Please enter correct data types.")


def main():
    hash_table = HashTable(size=23)
    medicine_array = create_sample_data()

    for medicine in medicine_array:
        hash_table.insert(medicine)

    while True:
        print("\n========== Pharmacy Inventory System ==========")
        print("1. Display all medicines")
        print("2. Insert new medicine")
        print("3. Search medicine by ID")
        print("4. Run performance comparison")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            hash_table.display()

        elif choice == "2":
            insert_new_medicine(hash_table, medicine_array)

        elif choice == "3":
            try:
                medicine_id = int(input("Enter Medicine ID to search: "))
                result = hash_table.search(medicine_id)

                if result:
                    print("\nMedicine found:")
                    print(result)
                else:
                    print("Medicine not found.")

            except ValueError:
                print("Invalid ID. Please enter a number.")

        elif choice == "4":
            performance_test(hash_table, medicine_array)

        elif choice == "5":
            print("Exiting Pharmacy Inventory System.")
            break

        else:
            print("Invalid choice. Please select between 1 and 5.")


if __name__ == "__main__":
    main()