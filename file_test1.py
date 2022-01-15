#
# Read and write files using the built-in Python file methods
#

# def main():  
#   # Open a file for writing and create it if it doesn't exist
#   f = open("textfile.txt","w+")
  
  # Open the file for appending text to the end
  # f = open("textfile.txt","a+")

  # write some lines of data to the file
 # for i in range(10):
 #   f.write("This is line %d\r\n" % (i+1))
  
  # close the file when done
 # f.close()
  
  # Open the file back up and read the contents
f = open("C:\\data\\computing\\software-programming\\Python\\all_wiki_pages.csv","r")
if f.mode == 'r': # check to make sure that the file was opened
    # use the read() function to read the entire file
    # contents = f.read()
    # print (contents)
    l=1
    fl = f.readlines() # readlines reads the individual lines into a list
    for x in fl:
      i=x.find('\t')-1
      j=i+1
      k=x.count('\t')
      if l > k
        print (k, x)

      print (i,j)      print (x[0:i])
      print (x[j:])
    
#  print ('a\tb')
# if __name__ == "__main__":
#   main()
