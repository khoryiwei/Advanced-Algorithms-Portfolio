import threading
import time


# ==========================================
# Recursive Factorial Function
# ==========================================

def factorial(n):
    """
    Recursive function to calculate factorial.
    Time Complexity: O(n)
    """

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


# ==========================================
# Sequential Execution
# ==========================================

def sequential_execution(numbers):
    print("\n========== Sequential Execution ==========")

    total_time = 0

    for number in numbers:

        start = time.perf_counter_ns()

        factorial(number)

        end = time.perf_counter_ns()

        execution_time = end - start
        total_time += execution_time

        print(f"Factorial({number}) = Calculated")
        print(f"Execution Time : {execution_time} ns\n")

    average = total_time / len(numbers)

    print("--------------------------------------")
    print(f"Total Time : {total_time} ns")
    print(f"Average Time : {average:.2f} ns")
    print("--------------------------------------")


# ==========================================
# Worker Thread
# ==========================================

def thread_task(number):

    start = time.perf_counter_ns()

    factorial(number)

    end = time.perf_counter_ns()

    print(
        f"Thread {threading.current_thread().name} "
        f"completed Factorial({number}) "
        f"in {end-start} ns"
    )


# ==========================================
# Multithreading Execution
# ==========================================

def multithreading_execution(numbers):

    print("\n========== Multithreading Execution ==========")

    threads = []

    start = time.perf_counter_ns()

    for number in numbers:

        thread = threading.Thread(
            target=thread_task,
            args=(number,)
        )

        threads.append(thread)

        thread.start()

    for thread in threads:
        thread.join()

    end = time.perf_counter_ns()

    total = end - start

    average = total / len(numbers)

    print("--------------------------------------")
    print(f"Total Time : {total} ns")
    print(f"Average Time : {average:.2f} ns")
    print("--------------------------------------")


# ==========================================
# Performance Comparison
# ==========================================

def performance_comparison(numbers):

    print("\n========================================")
    print("Performance Comparison")
    print("========================================")

    # Sequential

    start = time.perf_counter_ns()

    for number in numbers:
        factorial(number)

    end = time.perf_counter_ns()

    sequential_time = end - start

    # Multithreading

    threads = []

    start = time.perf_counter_ns()

    for number in numbers:

        thread = threading.Thread(
            target=factorial,
            args=(number,)
        )

        threads.append(thread)

        thread.start()

    for thread in threads:
        thread.join()

    end = time.perf_counter_ns()

    thread_time = end - start

    print(f"Sequential Execution : {sequential_time} ns")
    print(f"Multithreading : {thread_time} ns")
    print()

    if thread_time < sequential_time:
        print("Result : Multithreading is faster.")
    else:
        print("Result : Sequential execution is faster.")


# ==========================================
# Main Program
# ==========================================

def main():

    numbers = [200, 300, 400, 500]

    while True:

        print("\n========================================")
        print(" MULTITHREADING FACTORIAL SYSTEM ")
        print("========================================")
        print("1. Sequential Execution")
        print("2. Multithreading Execution")
        print("3. Performance Comparison")
        print("4. Exit")
        print("========================================")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":

            sequential_execution(numbers)

        elif choice == "2":

            multithreading_execution(numbers)

        elif choice == "3":

            performance_comparison(numbers)

        elif choice == "4":

            print("Exiting Program...")
            break

        else:

            print("Invalid choice.")


if __name__ == "__main__":
    main()