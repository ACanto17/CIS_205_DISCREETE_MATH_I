import sys

#read a file, store into array

filename = sys.argv[1]
file = open(filename)
A = []
for line in file:
	A.append(int(line.rstrip()))


def sort205(p,r):
    if p < r:
        q = divide(p,r)
        sort205(p,q-1)
        sort205(q+1, r)

def divide(p,r):
    x = A[r]
    i = p-1


    for j in range(p,r):
        if (A[j] <= x):
            i +=1;
            temp = A[i]

            A[i] = A[j]
            A[j] = temp

    temp = A[i+1]
    A[i+1] = A[r]
    A[r] = temp

    return(i+1)

sort205(0,len(A)-1)

print(A)




# function sort205(p, r) {
#         if (p < r) {
#                 q = divide(p,r);
#                 sort205(p, q-1);
#                 sort205(q+1, r);
#         }
# }
#
# function divide(p, r) {
#         x = A[r];
#         i = p-1;
#
#         for j = p to r-1 {
#                 if (A[j] <= x) {
#                         i += 1;
# 			exchange A[i] with A[j];
#                 }
#         }
# 	exchange A[i+1] with A[r]
#         return (i+1);
# }
