class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        #min. Runtime (66ms) T(C(N)=O(N**2)) and S(C(N)=O(N)) as it requires contiguous memory space at different Level wise iteration
        m=defaultdict(list)#List Declare
        for i in range(len(mat)):#Matrix array List Row and colm Iteration
            for j in range(len(mat[0])):m[i-j].append(mat[i][j])#appending matrix's [indx] row nd colm  val

        for k in m:m[k].sort(reverse=True)#Sorting the Reversed matrix row and col 

        for i in range(len(mat)):#pop the matrix row and col 
            for j in range(len(mat[0])):mat[i][j]=m[i-j].pop()

        return mat#printing the matrix 
