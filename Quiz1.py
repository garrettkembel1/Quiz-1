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

for rec in csv_file:
    outfile.write(f'{rec[0]}, {rec[2]}, {rec[3]}, {rec[6]}, {rec[7]}, {rec[8]}\n')

#this will skip the first record which is the header
next(csv_file)

for rec in csv_file:
    #print(rec)
    Gpa = float(rec[8])
    if Gpa < 3:
        outfile.write(f'{rec[0]}, {rec[2]}, {rec[3]}, {rec[6]}, {rec[7]}, {rec[8]}\n')


outfile.close()



#create a new dictionary named 'student_dict'



#use a loop to iterate through each row of the file


    #check if the GPA is below 3.0. If so, write the record to the outfile
    
        



    # append the record to the dictionary with the student Full name in proper case 
    # as the Key and the value as the GPA
    





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