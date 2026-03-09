#For this assignment use the numbers.txt file.
#A different numbers.txt will be used for grading.
#Read in all the numbers. Display the following information:
#How many numbers in the file
#Total of all the number
#Average
#Highest number
#Lowest number
#Correct answers for the included file:
numbers = []
with open("numbers.txt") as f:
    for x in f:
        numbers.append(int(x.strip()))
    print(f"There are {len(numbers)} numbers in the files")
    print(f"The average of all numbers is {sum(numbers) / len(numbers)}")
    print(f"The total of all the numbers is {sum(numbers)}")
    print(f"The highest number is {max(numbers)} on line {numbers.index(max(numbers))+1}")
    print(f"The lowest number is {min(numbers)} on line {numbers.index(min(numbers))+1}")


