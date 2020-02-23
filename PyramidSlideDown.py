def longest_slide_down(pyramid):
   a=[[0 for i in range(len(pyramid[i]))] for i in range(len(pyramid))]
   a[0][0] = pyramid[0][0]
   for i in range(1,len(pyramid)):
       for j in range(len(pyramid[i])):
           if j==0:
               a[i][j] = a[i-1][j] + pyramid[i][j]
           elif j>0 and j<len(pyramid[i])-1:
               a[i][j] = max(a[i-1][j-1] + pyramid[i][j],a[i-1][j] + pyramid[i][j])
           elif j== len(pyramid[i])-1:
               a[i][j] = a[i-1][j-1] + pyramid[i][j]

   return max(a[len(a)-1])