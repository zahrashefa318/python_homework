import csv
import os
import custom_module 
from datetime import datetime
employees={}
employee_id_column=0
minutes1={}
minutes2={}
minutes_set=set()
minutes_list =[]
#Task 2: Read a CSV File----------------------------------------------------------------
def read_employees():
    rows=[]
    cols=[]
    all_rows=[]
    try:
        with open('../csv/employees.csv','r') as file:
            file_content=csv.reader(file)
            for row in file_content:
                all_rows.append(row)
            
        cols=all_rows[0]

        for row in all_rows[1:]:
            rows.append(row)
        employees["fields"]=cols
        employees["rows"]=rows
        return employees
    except Exception as e:
        print(f"An exception occurred :  {type(e).__name__}")


employees=read_employees()


#Task 3: Find the Column Index----------------------------------------------------------
def column_index(col_name):
    if col_name in employees['fields']:
        employee_id_column=employees['fields'].index(col_name)
        return employee_id_column


employee_id_column=column_index( "employee_id")


#Task 4: Find the Employee First Name---------------------------------------------------
def first_name(row_number):
    col_index=column_index('first_name')
    dic_rows=employees['rows']
    value=dic_rows[row_number][col_index]
    return value


#Task 5: Find the Employee: a Function in a Function------------------------------------
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column])==employee_id
    matches=list(filter(employee_match,employees['rows']))
    return matches

#Task 6: Find the Employee with a Lambda------------------------------------------------
def employee_find_2(employee_id):
    matches=list(filter(lambda row: int(row[employee_id_column])== employee_id, employees['rows']))
    return matches


#Task 7: Sort the Rows by last_name Using a Lambda--------------------------------------
def sort_by_last_name():
    employees['rows'].sort(key=lambda row: row[column_index('last_name')])
    sorted_rows=employees['rows']
    return sorted_rows
    
     
sort_by_last_name()  


#Task 8: Create a dict for an Employee--------------------------------------------------
def employee_dict(row):
    keys=[]
    for fname in employees['fields']:
        keys.append(fname)
    keys=keys[1:]
    row=row[1:]
    employee_dictionary=dict(zip(keys,row))
    return employee_dictionary

print(employee_dict([5,'James','Torres','+267 +1-471-316-0190x308']))


#Task 9: A dict of dicts, for All Employees-------------------------------------------
def all_employees_dict():
    ids=[]
    employee_dict_list=[]
    for row in employees['rows']:
        ids.append(row[0])
        employee_dict_list.append(employee_dict(row))
    dic_of_dict=dict(zip(ids,employee_dict_list))

    return dic_of_dict


#Task 10: Use the os Module-------------------------------------------------------------
def get_this_value():
    env_val=os.getenv("THISVALUE")
    return env_val


#Task 11: Creating Your Own Module------------------------------------------------------
def set_that_secret(new_sec):
    new_secret=custom_module.set_secret(new_sec)

set_that_secret("zahra123")
print(custom_module.secret)


#Task 12: Read minutes1.csv and minutes2.csv--------------------------------------------
def read_minutes():
    try:
        min1_rows=[]
        min2_rows=[]
        min1_dic={}
        min2_dic={}
        with open('../csv/minutes1.csv','r')as file1, open('../csv/minutes2.csv','r')as file2:
            minute1_content=csv.reader(file1)
            minute2_content=csv.reader(file2)
            for min1,min2 in zip(minute1_content,minute2_content):
                min1_rows.append(min1)
                min2_rows.append(min2)
        min1_fields=min1_rows[0]
        min2_fields=min2_rows[0]
        min1_rows=min1_rows[1:]
        min2_rows=min2_rows[1:]
        min1_tuples=[]
        min2_tuples=[]
        
        for r1,r2 in zip(min1_rows,min2_rows):
            min1_tuples.append(tuple(r1))
            min2_tuples.append(tuple(r2))
        print("hi shefa")
        min1_dic["fields"]=min1_fields
        min2_dic["fields"]=min2_fields
        min1_dic["rows"]=min1_tuples
        min2_dic["rows"]=min2_tuples
        return min1_dic, min2_dic 
            
    except Exception as e:
        print(f"An exception occurred: {type(e).__name__}")

minutes1, minutes2 = read_minutes()


#Task 13: Create minutes_set--------------------------------------------------------------
def create_minutes_set():
    min1_set=set(minutes1["rows"])
    min2_set=set(minutes2["rows"])
    united_set=min1_set.union(min2_set)
    return united_set

minutes_set = create_minutes_set()


#Task 14: Convert to datetime-------------------------------------------------------------
def create_minutes_list():
    min_list=list(minutes_set)
    formatted_min_list=list(map(lambda x: (x[0], datetime.strptime(x[1],"%B %d, %Y")), min_list))
    return formatted_min_list
minutes_list=create_minutes_list()


#Task 15: Write Out Sorted List-----------------------------------------------------------
def write_sorted_list():
    minutes_list.sort(key=lambda tpl: tpl[1], reverse=False)
    sorted_min_list=minutes_list
    str_date_fmt_list=list(map(lambda tpl: (tpl[0], datetime.strftime(tpl[1],"%B %d, %Y")),sorted_min_list))

    with open('./minutes.csv',"w") as file:
        w=csv.writer(file)
        w.writerow(minutes1["fields"])
        w.writerows(str_date_fmt_list)
        
    return str_date_fmt_list   
