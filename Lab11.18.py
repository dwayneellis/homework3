# CIS 2348 Homework 3 Fall 2020.
# Dwayne Ellis
# Student ID: #######
# Lab 11.18 Filter and sort a list
# Write a program that gets a list of integers from input, and outputs non-negative integers in ascending order

integers = input().split()

# Define an empty list non_neg_int to store all non-negative integers.

non_neg_int = []

for num in integers:

    # Convert the string number into integer.

    num = int(num)

    # Checks whether number is non-negative.

    if num >= 0:

        non_neg_int.append(num)

non_neg_int.sort()

# Print sorted list of non-negative integers.

for i in non_neg_int:
    print(i, end=' ')
