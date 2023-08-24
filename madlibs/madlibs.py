#Madlibs project - In this project there is gonna be a whole paragraph with few blanks inside them. We have to fill the blanks using the string concatenation and make a decent looking paragraph.
#We can do this project in 3 methods-
#name = Sandeep
#1. Using str = print("Hello , How are you" + name) 
#2. Using format() - print("Hello , How are you {}.format(name)")
#3. Using fstring - print(f"Hello , How are you  {name}") - This method is good as it is good looking and understandable.

verb = input("Enter verb ")
verb2 = input("Enter verb ")
verb3 = input("Enter verb ")
verb4 = input("Enter verb ")
adj = input("Enter Adjective ")
adj1 = input("Enter Adjective ")
adj2 = input("Enter Adjective ")
adj3 = input("Enter Adjective ")
adj4 = input("Enter Adjective ")
adj5 = input("Enter Adjective ")

madlibs = f"But I'm going to just write the code in front of you rather than have you look at it in the book. So what we're going to do is, I've got my text editor up here and let me start by {verb} a new folder. New folder for my chapter 9 exercise, and then I'm going to go and make an untitled file. That was from the previous one. And I'll do what I {verb2} do. Print 'Hello' and save it. And save it here into exercise 09, and ex_09.py. So now I have a folder that's in my py4e folder and that happens to be in my desktop. py4e is my folder on my {verb3} and now l have all of these subfolders cd ex_08. ls is dir on Windows, ls, oops I gotta go up one, ex_09 ls. So I've got that {verb4} right there. Now I'm going to want to read some files. And so I'm going to bring some files down. A couple of files. Python for everybody code3/intro.txt, so I've {adj} this URL. And I'm going to save it, save {adj2} as, and it's really important that I {adj3} it in the same folder as I'm {adj4} to write my code, just so that when I open this {adj5} it knows where it's at."

print(madlibs)
