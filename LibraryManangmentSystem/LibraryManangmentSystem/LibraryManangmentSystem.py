from os import remove


class library:
    def __init__(self,lib):
        self.file=lib        
    def readFile(self):
            with open(self.file, 'r') as _file:
                contentLine = 0
                for line in _file:
                    contentLine += 1
                    print(f"book: {line.strip()}")
                    
    def addBook(self):
        
        bookName=input("Book Name:")
        authorName=input("Author Name:")
        firstRelease=int(input("First Release:"))
        PageOfNumber=int(input("Number of Page:"))

        booksList=f"{bookName}\n{authorName}\n{str(firstRelease)}\n{str(PageOfNumber)}".splitlines()
        with open(self.file, "a+") as _file:
            _file.write(",".join(booksList)+"\n")
            print(f"book:{bookName} author:{authorName}")
            
    def removeBook(self):
        title=input("Choose remove the book")
       
        with open(self.file ,'r') as dosya:
         lines = dosya.readlines()

        with open(self.file, 'w') as dosya:
         for line in lines:
            if title not in line:
                dosya.write(line)

    



print("Welcome to Library Manangment System!!!")
while(1):
   print("****") 
   print("1)List books")
   print("2)Add book")
   print("3)Remove book")
   print("4)QUIT")

   choose=int(input("Choose process:"))
   if choose==1:
       fileContent=library("books.txt")
       fileContent.readFile()
       
   elif choose==2:
    
       fileContent=library("books.txt")
       fileContent.addBook()
   
   elif choose==3:
       fileContent=library("books.txt")
       fileContent.removeBook()
   else:
       break
