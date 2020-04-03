
# coding: utf-8

# In[1]:


def gradingStudents(grades):    
    for i in range (0,n):
            int(i)
            if grades[i]>37:
                z=grades[i]
                while(z%5 != 0):
                    z=z+1   
                if (z-grades[i])<3:
                    grades[i]=z
            print(grades[i])   
            
n=int(input("Enter the total number of grades ")) 
grades=list()
for grade in range(0,n):
    x=int(input("Enter the grade ")) 
    grades.append(x) 
print("The rounded grades are as follows ")    
gradingStudents(grades)        

