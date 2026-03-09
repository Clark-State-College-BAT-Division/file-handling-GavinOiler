#For this assignment use the words.txt file.
#Read in all the words. Count how many are palindromes, or words that are spelled the same forwads and backwards.
#For example, wow is a paldindrome.
#A different file wile be used for grading.
#Correct answer for this file: 
palindromes = 0
with open("words.txt") as f:
    for x in f:
        #remove the \n
        if x.strip() == x.strip()[::-1]:
            print(f"{x.strip()} is a palindrome")
            palindromes = palindromes + 1
print(f"There were {palindromes} palindromes")
        