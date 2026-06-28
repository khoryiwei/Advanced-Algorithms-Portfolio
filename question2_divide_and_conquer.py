import time


class Transaction:
    def __init__(self, transaction_id, customer_name, product_name, amount, transaction_date):
        self.transaction_id = transaction_id
        self.customer_name = customer_name
        self.product_name = product_name
        self.amount = amount
        self.transaction_date = transaction_date

    def __str__(self):
        return (
            f"ID: {self.transaction_id} | "
            f"Customer: {self.customer_name} | "
            f"Product: {self.product_name} | "
            f"Amount: RM{self.amount:.2f} | "
            f"Date: {self.transaction_date}"
        )


def create_sample_transactions():
    return [
        Transaction(1008, "Alice", "Keyboard", 199.90, "2026-06-10"),
        Transaction(1003, "Bob", "Mouse", 89.90, "2026-06-11"),
        Transaction(1010, "Charlie", "Monitor", 899.00, "2026-06-12"),
        Transaction(1001, "David", "USB Drive", 35.90, "2026-06-13"),
        Transaction(1005, "Emma", "Headset", 259.00, "2026-06-14"),
        Transaction(1002, "Frank", "SSD", 399.00, "2026-06-15"),
        Transaction(1007, "Grace", "Webcam", 179.90, "2026-06-16"),
        Transaction(1009, "Henry", "Laptop Stand", 149.90, "2026-06-17"),
        Transaction(1004, "Ivy", "Microphone", 329.00, "2026-06-18"),
        Transaction(1006, "Jack", "Speaker", 289.00, "2026-06-19")
    ]


def display_transactions(transactions):
    print("\n================ Transaction Records ================")
    for transaction in transactions:
        print(transaction)


def merge_sort(transactions):
    # Base case: list with one or zero elements is already sorted
    if len(transactions) <= 1:
        return transactions

    # Divide step: split the list into two halves
    mid = len(transactions) // 2
    left_half = transactions[:mid]
    right_half = transactions[mid:]

    # Conquer step: recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Combine step: merge the sorted halves
    return merge(left_sorted, right_sorted)


def merge(left, right):
    sorted_transactions = []
    i = 0
    j = 0

    # Compare transaction IDs and merge in ascending order
    while i < len(left) and j < len(right):
        if left[i].transaction_id <= right[j].transaction_id:
            sorted_transactions.append(left[i])
            i += 1
        else:
            sorted_transactions.append(right[j])
            j += 1

    # Add remaining records from the left half
    while i < len(left):
        sorted_transactions.append(left[i])
        i += 1

    # Add remaining records from the right half
    while j < len(right):
        sorted_transactions.append(right[j])
        j += 1

    return sorted_transactions


def binary_search(transactions, target_id):
    left = 0
    right = len(transactions) - 1

    while left <= right:
        mid = (left + right) // 2

        if transactions[mid].transaction_id == target_id:
            return transactions[mid]

        elif target_id < transactions[mid].transaction_id:
            right = mid - 1

        else:
            left = mid + 1

    return None


def linear_search(transactions, target_id):
    for transaction in transactions:
        if transaction.transaction_id == target_id:
            return transaction
    return None


def compare_search_performance(transactions):
    sorted_transactions = merge_sort(transactions)
    search_keys = [1001, 1005, 1010, 9999, 8888]

    binary_total = 0
    linear_total = 0

    print("\n================ Search Performance Comparison ================")
    print("{:<18} {:<20} {:<20}".format("Transaction ID", "Binary Search (ns)", "Linear Search (ns)"))
    print("-" * 65)

    for key in search_keys:
        start = time.perf_counter_ns()
        binary_search(sorted_transactions, key)
        end = time.perf_counter_ns()
        binary_time = end - start
        binary_total += binary_time

        start = time.perf_counter_ns()
        linear_search(transactions, key)
        end = time.perf_counter_ns()
        linear_time = end - start
        linear_total += linear_time

        print("{:<18} {:<20} {:<20}".format(key, binary_time, linear_time))

    print("-" * 65)
    print(f"Total Binary Search Time: {binary_total} ns")
    print(f"Total Linear Search Time: {linear_total} ns")
    print(f"Average Binary Search Time: {binary_total / len(search_keys):.2f} ns")
    print(f"Average Linear Search Time: {linear_total / len(search_keys):.2f} ns")


def main():
    transactions = create_sample_transactions()
    sorted_status = False

    while True:
        print("\n====================================================")
        print("        ONLINE SHOPPING TRANSACTION SYSTEM")
        print("====================================================")
        print("1. Display all transactions")
        print("2. Sort transactions using Merge Sort")
        print("3. Search transaction using Binary Search")
        print("4. Search transaction using Linear Search")
        print("5. Compare search performance")
        print("6. Exit")
        print("====================================================")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            display_transactions(transactions)

        elif choice == "2":
            print("\nBefore Sorting:")
            display_transactions(transactions)

            start = time.perf_counter_ns()
            transactions = merge_sort(transactions)
            end = time.perf_counter_ns()

            sorted_status = True

            print("\nTransactions sorted successfully using Merge Sort.")
            print(f"Merge Sort Execution Time: {end - start} ns")

            print("\nAfter Sorting:")
            display_transactions(transactions)

        elif choice == "3":
            if not sorted_status:
                transactions = merge_sort(transactions)
                sorted_status = True
                print("\nTransactions were sorted first because Binary Search requires sorted data.")

            try:
                target_id = int(input("Enter transaction ID to search: "))
                result = binary_search(transactions, target_id)

                if result:
                    print("\nTransaction found using Binary Search:")
                    print(result)
                else:
                    print("Transaction not found.")

            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == "4":
            try:
                target_id = int(input("Enter transaction ID to search: "))
                result = linear_search(transactions, target_id)

                if result:
                    print("\nTransaction found using Linear Search:")
                    print(result)
                else:
                    print("Transaction not found.")

            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == "5":
            compare_search_performance(transactions)

        elif choice == "6":
            print("Exiting Online Shopping Transaction System.")
            break

        else:
            print("Invalid choice. Please select between 1 and 6.")


if __name__ == "__main__":
    main()