#General Declarations---
import pandas as pd
import mysql.connector as conn
import matplotlib.pyplot as plt
sqlcon=conn.connect(host="localhost",user="root",passwd="hello",database='application')
mycursor = sqlcon.cursor()
print('-------------------------------------------------------------------------------------')
print('                                   1. Admin                                          ')
print('                                   2. Patient                                        ')
print('                                   3. Exit                                           ')
print('-------------------------------------------------------------------------------------')
a=input('Enter your choice....')
print('-------------------------------------------------------------------------------------')
if a in ['Admin','admin','1']:
     password=input('Enter password....')
     if password=='abc':
          while True:
               print('-------------------------------------------------------------------------------------')
               print('Welcome to the Admin login')
               print('Menu for various operations')
               print('1. Add new patient')
               print('2. Add new staff')
               print('3. Display patient details ')
               print('4. Display staff details ')
               print('5. Make changes in patient record ')
               print('6. Make changes in staff record ')
               print('7. Deletion of patient record ')
               print('8. Deletion of staff record ')
               print('9. Display active cases graphically')
               print('10.Close application ')
               print('-------------------------------------------------------------------------------------')
               ch=int(input('Enter the number against the choice you want to proceed with....'))
               print('-------------------------------------------------------------------------------------')
               if ch==1:
                    while True: 
                         pid=input('Enter id of patient....')
                         pname=input("Enter name of patient....")
                         page=input("Enter age of patient....")
                         pgen=input("Enter gender of patient(m/f)....")
                         parea=input('Enter area of patient\'s house....')
                         pdate=input('Enter date of detection(YYYYMMDD)....')
                         print('-------------------------------------------------------------------------------------')
                         add_p = ("INSERT INTO PATIENT (id,name,age,gender,area,detection_date) VALUES (%s,%s,%s,%s,%s,%s)")
                         data_p=(pid,pname,page,pgen,parea,pdate)
                         mycursor.execute(add_p,data_p)
                         sqlcon.commit()
                         print("1 record inserted")
                         print('-------------------------------------------------------------------------------------')
                         new_rec=input("Do you want to enter another records (Y/N)....")
                         print('-------------------------------------------------------------------------------------')
                         if new_rec=='N' or new_rec=='n':
                              break


               elif ch==2:
                    while True: 
                         sid=input('Enter staff id')
                         sname=input("Enter name of employee....")
                         sage=input("Enter age of employee....")
                         sgen=input("Enter gender of employee(m/f)....")
                         sarea=input('Enter area of employee\'s house....')
                         spost=input('Enter the post of the employee....')
                         ssal=input('Enter the salary of employee....')
                         sdate=input('Enter date of joining(YYYYMMDD)....')
                         print('-------------------------------------------------------------------------------------')
                         add_s = ("INSERT INTO STAFF (id,name,age,gender,area,joining_date,post,salary) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)")
                         data_s=(sid,sname,sage,sgen,sarea,sdate,spost,ssal)
                         mycursor.execute(add_s,data_s)
                         sqlcon.commit()
                         print("1 record inserted")
                         print('-------------------------------------------------------------------------------------')
                         new_rec=input("Do you want to enter another records (Y/N)....")
                         print('-------------------------------------------------------------------------------------')
                         if new_rec=='N' or new_rec=='n':
                              break


               elif ch==3:
                    print('1. On the basis of area')
                    print('2. On the basis of gender')
                    print('3. All the patients')
                    print('-------------------------------------------------------------------------------------')
                    chd=int(input('Enter the number against the choice you want to proceed with....'))
                    print('-------------------------------------------------------------------------------------')
                    if chd==1:
                         parea=input("Enter area of city....")
                         print('-------------------------------------------------------------------------------------')
                         qry2="select * from patient where area='%s';" %(parea,)
                         dfsql_1=pd.read_sql(qry2,sqlcon)
                         blankindex=['']*len(dfsql_1)
                         dfsql_1.index=blankindex
                         if str(dfsql_1.empty)=='True':
                              print('There is no record related to entered data')
                         else:
                              print(dfsql_1)
                         print('-------------------------------------------------------------------------------------')
                    elif chd==2:
                         pgen=input("Enter gender of patient....")
                         print('-------------------------------------------------------------------------------------')
                         qry2="select * from patient where gender='%s';" %(pgen,)
                         dfsql_1=pd.read_sql(qry2,sqlcon)
                         blankindex=['']*len(dfsql_1)
                         dfsql_1.index=blankindex
                         if str(dfsql_1.empty)=='True':
                              print('There is no record related to entered data')
                         else:
                              print(dfsql_1)
                         print('-------------------------------------------------------------------------------------')
                    elif chd==3:
                         qry2="select * from patient order by id"
                         dfsql_1=pd.read_sql(qry2,sqlcon)
                         blankindex=['']*len(dfsql_1)
                         dfsql_1.index=blankindex
                         if str(dfsql_1.empty)=='True':
                              print('There is no patient')
                         else:
                              print(dfsql_1)
                         print('-------------------------------------------------------------------------------------')
                    else:
                         print('Entered choice is wrong')
                         print('-------------------------------------------------------------------------------------')



               elif ch==4:
                    print('1. On the basis of id')
                    print('2. On the basis of joining date')
                    print('3. On the basis of post')
                    print('4. All the staff members')
                    print('-------------------------------------------------------------------------------------')
                    chd=int(input('Enter the number against the choice you want to proceed with....'))
                    print('-------------------------------------------------------------------------------------')
                    if chd==1:
                         sid=input("Enter id of employee....")
                         print('-------------------------------------------------------------------------------------')
                         qry2="select * from staff where id=%s;" %(sid,)
                         dfsql_2=pd.read_sql(qry2,sqlcon)
                         blankindex=['']*len(dfsql_2)
                         dfsql_2.index=blankindex
                         if str(dfsql_2.empty)=='True':
                              print('There is no record related to entered data')
                         else:
                              print(dfsql_2)
                         print('-------------------------------------------------------------------------------------')
                    elif chd==2:
                         sdate=input("Enter joining date of employee(YYYYMMDD)....")
                         print('-------------------------------------------------------------------------------------')
                         qry2="select * from staff where joining_date=%s;" %(sdate,)
                         dfsql_2=pd.read_sql(qry2,sqlcon)
                         blankindex=['']*len(dfsql_2)
                         dfsql_2.index=blankindex
                         if str(dfsql_2.empty)=='True':
                              print('There is no record related to entered data')
                         else:
                              print(dfsql_2)
                         print('-------------------------------------------------------------------------------------')
                    elif chd==3:
                         spost=input("Enter post of employee....")
                         print('-------------------------------------------------------------------------------------')
                         qry2="select * from staff where post='%s';" %(spost,)
                         dfsql_2=pd.read_sql(qry2,sqlcon)
                         blankindex=['']*len(dfsql_2)
                         dfsql_2.index=blankindex
                         if str(dfsql_2.empty)=='True':
                              print('There is no record related to entered data')
                         else:
                              print(dfsql_2)
                         print('-------------------------------------------------------------------------------------')
                    elif chd==4:
                         qry2="select * from staff"
                         dfsql_2=pd.read_sql(qry2,sqlcon)
                         blankindex=['']*len(dfsql_2)
                         dfsql_2.index=blankindex
                         if str(dfsql_2.empty)=='True':
                              print('There is no staff member')
                         else:
                              pd.set_option('display.max_columns',None)
                              print(dfsql_2)
                         print('-------------------------------------------------------------------------------------')
                    else:
                         print('Entered choice is wrong')
                         print('-------------------------------------------------------------------------------------')
          

               elif ch==5:
                    print('1.Change name')
                    print('2.Change Area of residence')
                    print('-------------------------------------------------------------------------------------')
                    chd=int(input('Enter the number against the choice you want to proceed with....'))
                    print('-------------------------------------------------------------------------------------')
                    if chd==1:
                         pid=input("Enter ID of patient to change name...")
                         pname=input("Enter new name of patient....")
                         print('-------------------------------------------------------------------------------------')
                         data_p=(pname,pid) 
                         up_p= ("UPDATE PATIENT SET NAME=%s " "WHERE ID=%s")  
                         mycursor.execute(up_p,data_p)
                         sqlcon.commit()
                         print('Name has been changed')
                         print('-------------------------------------------------------------------------------------')
                    elif chd==2:
                         pid=input("Enter ID of patient to change area...")
                         parea=input('Enter new area of residence...')
                         print('-------------------------------------------------------------------------------------')
                         data_p=(parea,pid) 
                         up_p = ("UPDATE PATIENT SET AREA=%s " "WHERE ID=%s")  
                         mycursor.execute(up_p,data_p)
                         sqlcon.commit()
                         print('Residence area has been changed')
                         print('-------------------------------------------------------------------------------------')
                    else:
                         print('Entered choice is wrong')
                         print('-------------------------------------------------------------------------------------')



               elif ch==6:
                    print('1. Change name')
                    print('2. Change joining date')
                    print('3. Change salary')
                    print('4. Change post')
                    print('-------------------------------------------------------------------------------------')
                    chd=int(input('Enter the number against the choice you want to proceed with....'))
                    print('-------------------------------------------------------------------------------------')
                    if chd==1:
                         sid=input("Enter ID of staff member to change name....")
                         sname=input("Enter new name of staff member....")
                         print('-------------------------------------------------------------------------------------')
                         data_s=(sname,sid) 
                         up_s= ("UPDATE STAFF SET NAME=%s " "WHERE ID=%s")  
                         mycursor.execute(up_s,data_s)
                         sqlcon.commit()
                         print('Name of the staff member has been changed')
                         print('-------------------------------------------------------------------------------------')
                    elif chd==2:
                         sid=input("Enter ID of staff to change joining date....")
                         sdate=input('Enter new date of joining(YYYYMMDD)....')
                         print('-------------------------------------------------------------------------------------')
                         data_s=(sdate,sid) 
                         up_s = ("UPDATE STAFF SET joining_date=%s " "WHERE ID=%s")  
                         mycursor.execute(up_s,data_s)
                         sqlcon.commit()
                         print('Joining date of staff member has been changed')
                         print('-------------------------------------------------------------------------------------')
                    elif chd==3:
                         sid=input("Enter ID of staff to change salary....")
                         ssal=input('Enter new salary...')
                         print('-------------------------------------------------------------------------------------')
                         data_s=(ssal,sid) 
                         up_s = ("UPDATE STAFF SET salary=%s " "WHERE ID=%s")  
                         mycursor.execute(up_s,data_s)
                         sqlcon.commit()
                         print('Salary of staff member has been changed')
                         print('-------------------------------------------------------------------------------------')
                    elif chd==4:
                         sid=input("Enter ID of staff to change post....")
                         spost=input('Enter new post....')
                         data_s=(spost,sid)
                         print('-------------------------------------------------------------------------------------')
                         up_s = ("UPDATE STAFF SET post=%s " "WHERE ID=%s")  
                         mycursor.execute(up_s,data_s)
                         sqlcon.commit()
                         print('Post of staff member has been changed')
                         print('-------------------------------------------------------------------------------------')
                    else:
                         print('Entered choice is wrong')
                         print('-------------------------------------------------------------------------------------')


               elif ch==7:
                    pid=input("Enter ID of patient to delete....")
                    del_p = ("DELETE FROM PATIENT WHERE ID=%s")
                    data_p=(pid,)
                    mycursor.execute(del_p,data_p)
                    sqlcon.commit()
                    print('-------------------------------------------------------------------------------------')
                    g=int(pid)
                    sql_qury = "select * from patient"
                    mycursor.execute(sql_qury)
                    mycursor.fetchall()
                    h=int(mycursor.rowcount)
                    for i in range(g,h+1):
                         c=i+1
                         data_s=(i,c) 
                         up_s= ("UPDATE PATIENT SET ID=%s " "WHERE ID=%s")  
                         mycursor.execute(up_s,data_s)
                         sqlcon.commit()
                    
                    
               elif ch==8:
                    sid=input("Enter ID of staff member to delete....")
                    del_s = ("DELETE FROM STAFF WHERE ID=%s")
                    data_s=(sid,)
                    mycursor.execute(del_s,data_s)
                    sqlcon.commit()
                    print('-------------------------------------------------------------------------------------')




               elif ch==9:
                    qry2="select detection_date,count(id) from patient group by detection_date order by detection_date"
                    dfsql_1=pd.read_sql(qry2,sqlcon)
                    c=len(dfsql_1)
                    list1=[]
                    list2=[]
                    if c>0:
                        for i in range(0,c):
                            x=str(dfsql_1.loc[i,'detection_date'])
                            list1.append(x)
                            y=int(dfsql_1.loc[i,'count(id)'])
                            list2.append(y)
                        plt.plot(list1,list2,color='tomato')
                        plt.title('Corona cases in nearby areas')
                        plt.xlabel('Dates')
                        plt.ylabel('Cases')
                        plt.show()
                        print('-------------------------------------------------------------------------------------')
                    else:
                         print('No data to create a graph')



                    
               elif ch==10:
                    print('Thank You for using COVID MANAGEMENT SYSTEM')



                    
               else:
                    print('Entered choice is wrong')

               print('-------------------------------------------------------------------------------------')
               new_rec=input("Do you want to perform any more functions(y/n)...?")
               print('-------------------------------------------------------------------------------------')
               if new_rec=='N' or new_rec=='n':
                    break




     else:
          print('Access denied')
          print('-------------------------------------------------------------------------------------')

          



elif a in ['Patient','patient','2']:
     print('Thankyou for coming forward for your test')
     print('-------------------------------------------------------------------------------------')
     t1=input('Are you suffering from cough (y/n)')
     t2=input('Are you suffering from fever (y/n)')
     t3=input('Are you suffering from sneezing (y/n)')
     t4=input('Are you suffering from weakness (y/n)')
     t5=input('Are you suffering from body pain (y/n)')
     t6=input('Are you having breathing problems (y/n)')
     print('-------------------------------------------------------------------------------------')
     if [t1,t2,t3,t4,t5,t6]==['y','y','y','y','y','y']:
          print('We are really sorry, but according to us you are suffering from corona') 
          print('You are requested to stay quarantined for 14 days')
          sql_qury = "select * from patient"
          mycursor.execute(sql_qury)
          mycursor.fetchall()
          c=mycursor.rowcount + 1
          pid=c
          pname=input("Enter name of patient....")
          page=input("Enter age of patient....")
          pgen=input("Enter gender of patient(m/f)....")
          parea=input('Enter area of patients house....')
          pdate=input('Enter date of detection(YYYYMMDD)....')
          add_p = ("INSERT INTO PATIENT (id,name,age,gender,area,detection_date) VALUES (%s,%s,%s,%s,%s,%s)")
          data_p=(pid,pname,page,pgen,parea,pdate)
          mycursor.execute(add_p,data_p)
          sqlcon.commit()
          print('-------------------------------------------------------------------------------------')
          print('Thankyou for the informaton')
          print('We hope you get well soon !!!')
          print('-------------------------------------------------------------------------------------')
     else:
          print('Congratulations!!!')
          print('You are not having the symptoms of COVID-19')
          print('Please go to a nearby doctor for checkup')
          print('(Information from WHO)')
          print('-------------------------------------------------------------------------------------')




elif a in['Exit','exit','3']:
     print('Thank You for using COVID MANAGEMENT SYSTEM')
     print('-------------------------------------------------------------------------------------')


else:
     print('-------------------------------------------------------------------------------------')
     print('Entered choice is wrong')
     print('-------------------------------------------------------------------------------------')
          


                    
     

mycursor.close()
sqlcon.close()
