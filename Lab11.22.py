# CIS 2348 Homework 3 Fall 2020.
# Dwayne Ellis
# Student ID: #######
# Lab 11.22 Word frequencies
# Write a program that reads a list of words. Then, the program outputs those words and their frequencies.

# Read input from user and split word list by space and store as a list
words = input()

Word_List = words.split()

# Loop runs till the length of word list
for i in range(len(Word_List)):

    # Printing output with word and count
    print(Word_List[i], Word_List.count(Word_List[i]))
