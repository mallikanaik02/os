#!/bin/bash

# Count Vowels
echo "Enter a string:"
read str

count=0

for ((i=0; i<${#str}; i++))
do
    ch=${str:$i:1}

    case $ch in
        [aeiouAEIOU])
            count=$((count+1))
            ;;
    esac
done

echo "Number of vowels = $count"

# String Concatenation
echo
echo "Enter first string:"
read str1

echo "Enter second string:"
read str2

result=$str1$str2

echo "Concatenated String = $result"

# Palindrome Check
echo
echo "Enter a string to check palindrome:"
read word

rev=""

for ((i=${#word}-1; i>=0; i--))
do
    rev="$rev${word:$i:1}"
done

if [ "$word" = "$rev" ]
then
    echo "$word is a Palindrome"
else
    echo "$word is Not a Palindrome"
fi