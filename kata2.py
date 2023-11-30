def largest_lexicographical_string(S):
    while True:
        found_replacement = False
        for i in range(len(S) - 1):
            if int(S[i]) + int(S[i + 1]) <= 9:
                S = S[:i] + str(int(S[i]) + int(S[i + 1])) + S[i + 2:]
                found_replacement = True
                break

        if not found_replacement:
            break
    return S

#Example usage
print(largest_lexicographical_string("247192"))
print(largest_lexicographical_string("22256411"))


def longest_switching_slice(A):
    if len(A) < 2:
        return len(A)
    
    max_length = 1
    current_length =1

    for i in range(1, len(A)):
        if A[i] == A[i - 1] or (i > 1 and A[i] == A[i - 2]):
            current_length +=1

        else:
            current_length = 2

        max_length = max(max_length, current_length)

    return max_length

#Example
A = [1,2,3,2,3,2,3]
print(longest_switching_slice(A))




        
