#!/bin/bash

echo "Enter a number:"
read num

# Even or Odd
if [ $((num % 2)) -eq 0 ]
then
    echo "$num is Even"
else
    echo "$num is Odd"
fi

# Prime Check
prime=1

if [ $num -le 1 ]
then
    prime=0
else
    for ((i=2; i<=num/2; i++))
    do
        if [ $((num % i)) -eq 0 ]
        then
            prime=0
            break
        fi
    done
fi

if [ $prime -eq 1 ]
then
    echo "$num is Prime"
else
    echo "$num is Not Prime"
fi

# Factorial
fact=1

for ((i=1; i<=num; i++))
do
    fact=$((fact * i))
done

echo "Factorial of $num is $fact"


