# Name: Amar Srinivasan
# SI 206
# HW6 - Regular Expressions

import re
import os

def read_file(filename):
    """ Return a list of the lines in the file with the passed filename """
    
    # Open the file and get the file object
    source_dir = os.path.dirname(__file__) #<-- directory name
    full_path = os.path.join(source_dir, filename)
    infile = open(full_path,'r')
    
    # Read the lines from the file object into a list
    lines = infile.readlines()
    
    # Close the file object
    infile.close()
    
    # return the list of lines
    return lines

            
def find_dates(filename):
    """ Return a list of valid dates from the text file. 
    
        filename -- the name of the file to read from
        return -- the list of valid dates found in the file
    """
    pass
    
    # initialize a list of dates to an empty list
    date_list = []
    # read the lines from the file into a list
    lines = read_file(filename)
    # define the regular expression
    date_re = "\d{1,2}-\d{1,2}-\d{2,4}|\d{1,2}/\d{1,2}/\d{2,4}|\d{1,2}\.\d{1,2}\.\d{2,4}"
    # loop through the list of lines from the file
    for line in lines:
    	# get the list of items that match the regular expression from the current line
        date_list = date_list + re.findall(date_re,line)
    	# add the list of items that matched to the list of dates found so far
    
    # return the list of dates
    return date_list


def find_emails(filename):
    """ Return a list of valid emails in the text file with the given filename """
    email_list = []
    lines = read_file(filename)
    email_re = "[\.\w]+@[\.\w]+"
    for line in lines:
        email_list = email_list + re.findall(email_re,line)
    print(email_list)
    return email_list



def find_phoneNumbers(filename):
    """ Return a list of valid phone numbers in the text file with the given filename """
    phone_list = []
    lines = read_file(filename)
    phone_re = "\d{10}|\d{3}\.\d{3}\.\d{4}|\d{3}\s\d{3}\s\d{4}|\d{3}-\d{3}-\d{4}|\d{3}/\d{3}-\d{4}|\(\d{3}\)\s\d{3}-\d{4}"
    for line in lines:
        phone_list = phone_list + re.findall(phone_re,line)
    print(phone_list)
    return phone_list

## Extra credit
def count_word(filename, word):
    """ Return the number of times a given word or its plural (add s) appears in the file 
    
        fileName -- the name of the file to read from
        word -- the word to look for
        return -- a count of the number of times the word or its plural appears in the file 
    """
    word_list = []
    lines = read_file(filename)

    #Account for lowercase and uppercase at the beginning
    word_re =  "\s[" + word[0].lower() + "|" + word[0].upper() + "]" + word[1:] + "s?"
    for line in lines:
        word_list = word_list + re.findall(word_re,line)
    count = len(word_list)
    return count
    
        

## Do not modify the code below
## This function is for grading and debugging purposes
## statistics function reports your score based on the number of matches you got correct. 
def statistics(list1, list2):
    #print("Function output: ",list1)
    #print("Actual output: ", list2)
    matches = set(list2).intersection(set(list1)) 
    score = (len(matches)/len(list2))*20
    if len(matches)==len(list2):
        # no mismatches
        print("You found all the matches! Woohooo! Your score is: ", int(score))
    else:
        print("Looks like you missed some matches. Your score is:", int(score))
        print("You missed:", list(set(list2) - matches))

if __name__ == "__main__":
    filename = "The_Adventures_of_Sherlock_Holmes.txt"
    
    #Report the accuracy of find_dates function
    print("Testing find_dates function")
    statistics(find_dates(filename), [
        '11/29/02',
        '9/14/2020',
        '12-1-98',
        '12/09/19',
        '10-9-1890',
        '8.13.18',
        '11/31/16',
        '10-12-2021',
        '12.7.2018',
        '3.4.1991',
        '3/2/10',
        '5-16-1919',
        '2.4.91'])

    
    print("--------------------------------------------")
    #Report the accuracy of find_emails function
    print("Testing find_emails function")
    statistics(find_emails(filename), [
        'source@collab.sakaiproject.org',
        'm05ECIaH010327@nakamura.uits.iupui.edu',
        'louis@media.berkeley.edu',
        'rjlowe@iupui.edu',
        'cwen@iupui.edu',
        'gsilver@umich.edu',
        'apache@localhost','antranig@caret.cam.ac.uk',
        'gopal.ramasammycook@gmail.com'
    ])


    print("--------------------------------------------")
    # Report the accuracy of find_phoneNumbers function
    print("Testing find_phoneNumbers function")
    statistics(find_phoneNumbers(filename), [
        '674-763-9655',
        '694/876-8944',
        '767.764.7643',
        '385-765-9867',
        '3348769876',
        '(879) 765-3457',
        '765/987-8765',
        '9864636672',
        '780 764 3456',
        '780 345 6703',
        '675.673.6876',
        '670-465-3426',
        '780/654-5783',
        '567-796-8943',
        '(670) 765-5632',
        '456-565-5430',
        '764/433-5675',
        '543.545.4533',
        '309-321-4345'
    ])
    
    count = count_word(filename,"lip")
    if count == 10:
        print("You earned 3 extra points for finding the correct number")
    else:
        print("Count word for shoud return 10 and it returned: " + str(count))
    
    




