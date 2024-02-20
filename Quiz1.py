import csv


# create a file object to open the file in read mode

# create a csv object from the file object


#skip the header row


#create an outfile object for the pocessed record

#open the file and creates a file object
students = open('students.csv', 'r')
outfile = open('processedStudents.csv', 'w')

csv_file = csv.reader(students)

csv_file1 = csv.writer(outfile)

#this will skip the first record which is the header
next(csv_file)
    
for rec in csv_file:
    #print(rec)
    outfile.write(f'{rec[0]}, {rec[2]}, {rec[3]}, {rec[6]}, {rec[7]}, {rec[8]}\n')
    gpa = float(rec[8])
    rounded_gpa = round(gpa, 2)
    if rounded_gpa < 3.0:
        outfile.write(f'{rec[0]}, {rec[2]}, {rec[3]}, {rec[6]}, {rec[7]}, {rec[8]}\n')




outfile.close()


import csv

#create a new dictionary named 'student_dict'
student_dict = {

 'bob  norbert':  2.70,

 'wally  kendall':  2.80,

 'roberto  morales': 2.50,

 'luke  brazzi': 2.20

}

#use a loop to iterate through each row of the file


infile = open ('processedStudents.csv', 'r')
outfile = open ('student_dict', 'w')

csv_file = csv.reader(infile)
csv_file1 = csv.writer(outfile)

    #check if the GPA is below 3.0. If so, write the record to the outfile
next(csv_file)

for rec in csv_file:
    gpa = float(rec[5])
    if gpa < 3:
        outfile.write(f'{rec[1]} {rec[2]}, {rec[5]}\n')
    
        



    # append the record to the dictionary with the student Full name in proper case 
    # as the Key and the value as the GPA
    
print (student_dict)
print (student_dict['luke  brazzi'])


outfile.close()

#print the entire dictionary


#Print the corresponding GPA for student 'Luke Brazzi'



#close the outfile





#display the wordcloud
'''
from pathlib import Path
from wordcloud import WordCloud
import imageio.v2 as imageio
import matplotlib.pyplot as plt


text = Path("RomeoAndJuliet.txt").read_text()
mask_image = imageio.imread("mask_heart.png")
wordcloud = WordCloud(colormap="prism", mask=mask_image, background_color="white")
wordcloud = wordcloud.generate(text)
wordcloud = wordcloud.to_file("RomeoAndJulietHeart.png")
plt.imshow(wordcloud)
plt.show()

'''