#Task 3: List Comprehensions Practice
import csv

def employee_file_reader():
    try:
        lst_of_lst=[]
        fnames=[]
        lnames=[]
        with open("../csv/employees.csv","r") as file:
            file_content=csv.reader(file)
            for row in file_content:
                lst_of_lst.append(row)

        lst_of_lst=lst_of_lst[1:]
        
        for i in range(len(lst_of_lst)):
            fnames.append(lst_of_lst[i][1])
            lnames.append(lst_of_lst[i][2])

        full_names=[name+" "+last for name,last in zip(fnames,lnames)]
        containing_e=[name for name in full_names if "e" in name ]
        print(f'Full names : {full_names}')
        print(f'Names containing e : {containing_e}')

    except Exception as e:
        print(f"An error happened: {e}")

employee_file_reader()

            
