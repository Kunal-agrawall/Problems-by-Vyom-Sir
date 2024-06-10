'''
Problem Statement-
There is a JAR full of candies for sale at a mall counter. JAR has the capacity N, that is
JAR can contain maximum N candies when JAR is full. At any point of time. JAR can
have M number of Candies where M&lt;=N. Candies are served to the customers. JAR is

never remain empty as when last k candies are left. JAR if refilled with new candies in
such a way that JAR get full.
Problem Statement:
Write a code to implement above scenario. Display JAR at counter with available number
of candies. Input should be the number of candies one customer can order at point of
time. Update the JAR after each purchase and display JAR at Counter.
Output should give number of Candies sold and updated number of Candies in JAR.
If Input is more than candies in JAR, return: “INVALID INPUT”
Given,
N=10, where N is NUMBER OF CANDIES AVAILABLE
K =&lt; 5, where k is number of minimum candies that must be inside JAR ever.
'''
candies_left = 10
min_candies = 5

def refill_jar():
    global candies_left
    candies_left = 10
    print("JAR refilled.")

def sell_candies(num_sold):
    global candies_left
    if num_sold <= candies_left:
        candies_left -= num_sold
        print(f"Number of candies sold: {num_sold}")
        print(f"Updated number of candies in JAR: {candies_left}")
        if candies_left <= min_candies:
            refill_jar()
    else:
        print("INVALID INPUT. Not enough candies available.")

print(f"Number of candies available in JAR: {candies_left}")

while True:
    try:
        order = int(input("Enter the number of candies you want to buy: "))
        if order <= 0:
            print("Invalid input. Please enter a positive number.")
            continue
        sell_candies(order)
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if input("Do you want to continue? (yes/no): ").strip().lower() not in ['yes', 'y']:
        break
