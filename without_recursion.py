first_term=0
second_term=1
n=int(input("Enter the number of terms for fibonacci "))
print(first_term,second_term,end=" ")
while(n-2):
    next_term=first_term+second_term
    first_term=second_term
    second_term=next_term
    print(next_term,end=" ")
    n=n-1