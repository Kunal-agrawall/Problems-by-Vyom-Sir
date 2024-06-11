'''
Problem Statement-
A chocolate factory is packing chocolates into the packets. 
The chocolate packets here represent an array  of N number of integer values. 
The task is to find the empty packets(0) of chocolate and push it to the end of the conveyor belt(array).

Example 1 :
N=8 and arr = [4,5,0,1,9,0,5,0].

There are 3 empty packets in the given set. 
These 3 empty packets represented as O should be pushed towards the end of the array.

Input :

N=8

[4,5,0,1,9,0,5,0]
Element of arr[O] to arr[N-1], While input each element is separated by newline

Output:

4 5 1 9 5 0 0 0

Example 2:

Input:

N=6

[6,0,1,8,0,2]- Element of arr[0] to arr[N-1], While input each element is separated by newline

Output:

6 1 8 2 0 0
'''

def move_zeros_to_end(chocolate_packets):
    non_zero_position = 0

    for i in range(len(chocolate_packets)):
        if chocolate_packets[i] != 0:
            chocolate_packets[non_zero_position] = chocolate_packets[i]
            non_zero_position += 1

    for i in range(non_zero_position, len(chocolate_packets)):
        chocolate_packets[i] = 0

    return chocolate_packets

def main():
    chocolate_packets = [int(x) for x in input("Enter the chocolate packets separated by spaces: ").split()]
    result = move_zeros_to_end(chocolate_packets)
    print("Packets after moving empty ones to the end:", result)

if __name__ == "__main__":
    main()
