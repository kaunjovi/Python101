

# Hello world from Python. 
print "Hello, World!"

# * multiplications 
print 1 + 2 
print 1 * 2 

print "hello" + "world"
# print "hello" * "world" #No, you can't do that. 
print "hello" * 10 # wtf? Yeah, this actually works. 


# This prints out: A list: [1, 2, 3]
mylist = [1,2,3]
print "A list: %s" % mylist


# Create a list of numbers
some_numbers = [] 
some_numbers.append(100)
some_numbers.append(200)
# and print them out all at once 
print some_numbers

# Create a list in one line 
some_random_numbers = [1,3,4,5]
print some_random_numbers
   
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers 
print all_numbers
print "The list is %d objects long" % len(all_numbers)