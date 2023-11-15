#read excel data from python

import xlrd

# choose or select sheet from where you have to read data


loc=("path of sheet ")

wb=xlrd.open_workbook(loc)

sheet=wb.sheet_by_index(0)   #--->>0 is the sheet 1 like array index

print(sheet.cell_value(0,0))  #---> print value at that index


print(sheet.ncols)        #---->>>print number of columns

print(sheet.nrows)        #---->>>print number of rows

#to print column 

for i in range(sheet.ncols):
    print(sheet.cell_value(0,i))


#to print rows 

for i in range(sheet.ncols):
    print(sheet.cell_value(i,0))

#print rows values 

print(sheet.row_values(1))

#print columns values 

print(sheet.col_values(1))


