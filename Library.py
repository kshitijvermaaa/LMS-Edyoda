#!/usr/bin/env python
# coding: utf-8

# In[31]:


import random
import time


# In[32]:


admin_dict = {'admin':'admin'}
candidate_dict = {'cand':'cand'}


# In[29]:


candidate_details = {}
books = {4465: ['harry potter', 'jk rowling', 500, 'kisda32', 2012, 4465], 2212:['DataStructures', 'Mohit', 500, 'kisda32', 2021, 2212]}
# booklist_copy= []
candidatebookhistory = {}
class Library():
    def __init__(self):
        print('Welcome to central Library')
        time.sleep(2)
        self.login_menu()
        
    def login_menu(self):
        time.sleep(1)
        reg_inp = int(input(" 1. Login as an Admin\n 2. Login as a Candidate (default username and pass is 'cand')\n 3. Create a new account for candidates"))
        if reg_inp == 1:
            self.uname = str(input("Enter your username: "))
            self.password = str(input("Enter your password: "))
            for values in admin_dict:
                if (self.uname == values and self.password == admin_dict[values]):
                    print("Access granted Mr.{0}, Login Successful".format(self.uname))
                    Admin()
                    
                else:
                    print("Details Not Found, Please Register")
                    
                    
        elif reg_inp == 2:
            self.uname = str(input("Enter your email: "))
            self.password = str(input("Enter your password: "))
            for values in candidate_dict:
                if (self.uname == values and self.password == candidate_dict[values]):
                    print("Access granted Mr.{0}, Login Successful".format(self.uname))
                    Candidates()
                
        
        elif reg_inp == 3:
            self.fullname = input("Enter your Full Name: ")
            self.dob = int(input("Enter your DOB in numbers without any seperator e.g. 21071998: "))
            self.contactnumber = int(input("Enter your Mobile Number: "))
            self.email = str(input("Enter your email: "))
            self.password = str(input("Enter your password: "))
            self.student_id = random.randint(10000,99999)
            candidate_dict[self.email] = self.password
            cand_details_list = [self.fullname,self.dob,self.contactnumber,self.email] 
            candidate_details[self.student_id] = cand_details_list
            time.sleep(1)
            print("Thank You, Account Created with username {0} and student id {1}, Please Take a note of the id.".format(self.email,self.student_id))
            self.login_menu()
        else:
            print("Sorry, Invalid Choice")
            self.login_menu()
    def anothercandidate(self):
        y = input("Press any key to continue")
        y = Library()
        
class Admin:
    def __init__(self):
        time.sleep(1)
        print("Welcome to admin's corner")
        take_inp = int(input("1.Make a new admin.\n2.Add a book to the depository.\n3.Update any book through the book id.\n4.Delete any Book.\n5.View all the Books.\n6.Exit"))
        if take_inp == 1:
            self.addadmin()
        elif take_inp == 2:
            self.addbook()
        elif take_inp == 3:
            self.updatebook()
        elif take_inp == 4:
            self.deletebook()
        elif take_inp == 5:
            self.viewbooks()
        elif take_inp == 6:
            self.exit()
            
    def addadmin(self):
        time.sleep(1)
        self.uname = str(input("Enter your username: "))
        self.password = str(input("Enter your password: "))
        admin_dict[self.uname] = self.password
        time.sleep(2)
        print("Thank You, for creating an admin account")
        self.anotheradmmin()
        
        
    def anotheradmmin(self):
        x = input("Press any key to continue")
        x = Library()
    
    def addbook(self):
        time.sleep(1)
        self.bookname = input("Enter the name of the book: ")
        self.authorname = input("Enter the name of the author of the book: ")
        self.totalpages = int(input("Enter the total pages of the book: "))
        self.pubyear = int(input("Enter the year in which book was published: "))
        self.isbn = input("Enter the isbn of the book: ")
        self.bookid = random.randint(1000,9999)
        self.listofbook = [self.bookname,self.authorname,self.totalpages,self.isbn,self.pubyear,self.bookid]
        books[self.bookid] = self.listofbook
        time.sleep(2)
        print("Successfully Logged the book into the database, Thank You")
        Admin()
        
#     def addbookcopy(self):
#         no_of_copy = int(input("Enter the number of copies of the book you want to add"))
#         for n in range(0,no_of_copy):
#             self.copy_bookid = random.randint(1000,9999)
#             self.copyofbooks = [self.bookname,self.authorname,self.totalpages,self.isbn,self.pubyear,self.copyofbooks]
#             booklist_copy.append(self.copyofbooks)
#             Admin()
    def updatebook(self):
        self.updbook = int(input("Enter the book id you want to update: "))
        if self.updbook:
            for keys in books:
                if keys == self.updbook:
                    self.bookname = input("Enter the name of the book: ")
                    self.authorname = input("Enter the name of the author of the book: ")
                    self.totalpages = int(input("Enter the total pages of the book: "))
                    self.pubyear = int(input("Enter the year in which book was published: "))
                    self.isbn = input("Enter the isbn of the book: ")
                    self.updt_list = [self.bookname,self.authorname,self.totalpages,self.pubyear,self.isbn]
                    books.pop(self.updbook)
                    books[self.updbook] = self.updt_list
                    print("Successfully Logged the book into the database, Thank You")
                    Admin()
                else:
                    print("Cant find that book id, Sorry")
                    self.updatebook()
        else:
            print("Enter something")
            self.updatebook()
    
    
    def deletebook(self):
        print("Our Library has these books:", books)
        self.delbookid = int(input("Enter the book id you want to Delete: "))
        for keys in books:
            if keys == self.delbookid:
                books.pop(self.delbookid)
                print("Book with ID {} removed successfully".format(self.delbookid))
                self.__init__()
            else:
                print("No such Book id found,try again")
                self.deletebook()
    
    def viewbooks(self):
        print("Our Library has below given books:- ")
        if books:
            print(books)
        else:
            print("Currently no books are there in the library")
        print("***********************************************************************************")
        time.sleep(2)
        self.__init__()
    def exit(self):
        Library()
                    
class Candidates:
    def __init__(self):
        print("Welcome to candidates corner")
        cand_inp = int(input("1.See your Borrowed Books.\n2.Borrow a Book."))
        if cand_inp == 1:
            self.borrowedbooks()
        elif cand_inp == 2:
            self.borrowabook()
        elif cand_inp == 3:
            self.depositbook()
        else:
            print("Incorrect Choice")
            self.__init__()
    def borrowedbooks(self):
        print("Browsing our data base.......")
        time.sleep(2)
        print(self.lsit)
        time.sleep(2)
        self.__init__()
    
    
    def borrowabook(self):
        cand_id = input("Enter your Student ID to confirm the borrowing proccess")
        time.sleep(1)
        print(books)
        boookid = int(input("Enter the book id for which you want to borrow the book"))
        if boookid:
            for keys in books:
                if boookid == keys:
                    self.lsit = [books.get(boookid)]
                    candidatebookhistory[cand_id] = self.lsit
                    books.pop(boookid)
                    print("Book has been issued, Thank you")
                    print("Please return it within 15 days")
                    
                    break
        self.__init__()
    
a = Library()
