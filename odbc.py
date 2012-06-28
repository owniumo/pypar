import pyodbc

def dumprint():
    print "dumprint - Dumping Table"
    cursor.execute("select regmark, dateprov, rezerv from photo")
    rows = cursor.fetchall()
    for row in rows:
        print row.regmark, row.dateprov, row.rezerv

cstring = "Driver={Microsoft Paradox Driver (*.db )};DriverID=26;DefaultDir=C:\Python27\PROJ\db;"

cnxn = pyodbc.connect(cstring, autocommit=True)
cursor = cnxn.cursor()

print "Dumping Table"
cursor.execute("select regmark, dateprov, rezerv from photo")
rows = cursor.fetchall()
for row in rows:
    print row.regmark, row.dateprov, row.rezerv

    
print "inserting"
cursor.execute("insert into photo(regmark, dateprov, rezerv) values (?, ?, ?)", 'pyofuuuf', '2013-12-02', '1')


print "Dumping Table"
cursor.execute("select regmark, dateprov, rezerv from photo")
rows = cursor.fetchall()
for row in rows:
    print row.regmark, row.dateprov, row.rezerv

dumprint

print "closing c"
print cnxn.close

print "ok"

