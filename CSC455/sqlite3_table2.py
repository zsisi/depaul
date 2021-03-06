# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 18:46:49 2015

@author: jasminedumas
"""

import sqlite3

ChauffeurTable = '''CREATE TABLE ChauffeurCity(
  Chauffeur_city CHAR(15),
  Chauffeur_state CHAR(15),

  CONSTRAINT Chf_pk
    PRIMARY KEY(Chauffeur_city),

  CONSTRAINT Chf_fk
    FOREIGN KEY (Chauffeur_city)
      REFERENCES RecordNumber(Chauffeur_city)
);
'''

# Open a connection to database
conn2 = sqlite3.connect("publicchauffeur.db")

# Request a cursor from the database
cursor2 = conn2.cursor()

# Get rid of the tables if we already created it
cursor2.execute('DROP TABLE IF EXISTS ChauffeurCity')

# Create the table in publicchauffeur.db
cursor2.execute(ChauffeurTable)

# Open file for reading
fd2 = open('Public_Chauffeurs_Short.csv', 'r')
# Read all lines from the file into allLines variable
allLines2 = fd2.readlines()
fd2.close() # Close the file

# put in a subset of only city and state
# For each line in the file 
for line2 in allLines2[1:]:   # that subset excludes the column names in row 0
    for word in line2:
        if word is "NULL":
            word.replace("NULL", None)   
    
    # convert "A,B,C\n" line into ["A", "B", "C"] list of values.
    valueList2 = line2.strip().split(",")

    # Load the values into the ChauffeurCity table 
    # (2 columns in the 9 through 11 index in the csv file)
    cursor2.execute("INSERT OR IGNORE INTO ChauffeurCity VALUES (?,?);", valueList2[9:11])


# Check what we inserted into the table
allSelectedRows2 = cursor2.execute("SELECT * FROM ChauffeurCity;").fetchall()

# For every row, print the results of the query above, separated by a tab
for eachRow in allSelectedRows2:
    for value in eachRow:
        print (value, "\t",)
    print ("\n",) # \n is the end of line symbol
len(allSelectedRows2)
# Finalize inserts and close the connection to the database
conn2.commit()
conn2.close()
