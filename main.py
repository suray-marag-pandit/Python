#these are comments

""" these are multiline comments 
as shown here , python ignore 
string literal that is not 
assigned to the variable"""


# Variable
        #variable names are case sensitive
        # A variable is created the moment you first assign a value to it.
        
        # Casting
        # If you want to specify the data type of a variable, this can be done with casting.

        # Example
        # x = str(3)    # x will be '3'
        # y = int(3)    # y will be 3
        # z = float(3)  # z will be 3.0

        # You can get the data type of a variable with the type() function.
        # x = 5
        # y = "John"
        # print(type(x))
        # print(type(y))


        #x = y = z = "Orange" possible
        # fruits = ["apple", "banana", "cherry"]
        # x, y, z = fruits
        # print(x)
        # print(y)
        # print(z)

        # global variables
        #  If you use the global keyword, the variable belongs to the global scope:

        # def myfunc():
        # global x
        # x = "fantastic"

        # myfunc()


# python data types

# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType


        # There are four collection data types in the Python programming language:

                # List is a collection which is ordered and changeable. Allows duplicate members.
                # Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
                # Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
                # Dictionary is a collection which is ordered** and changeable. No duplicate members.


        #LISTS

        # appened , insert , extend
        # remove pop del clear
        # in for while comprehension
        #List comprehension
        # list.sort()
        # list.sort(reverse = true) // descending order
        # list.reverse()  //reverse the original list
        # newlist = list.copy()
        # newlist = list(thislist)
        # newlist = list1+ list2


        # append()	Adds an element at the end of the list
        # clear()	Removes all the elements from the list
        # copy()	Returns a copy of the list
        # count()	Returns the number of elements with the specified value
        # extend()	Add the elements of a list (or any iterable), to the end of the current list
        # index()	Returns the index of the first element with the specified value
        # insert()	Adds an element at the specified position
        # pop()	Removes the element at the specified position
        # remove()	Removes the item with the specified value
        # reverse()	Reverses the order of the list
        # sort()	Sorts the list


#tuples

        # Tuple items are ordered, unchangeable, and allow duplicate values.
        # len(thistuple)

        # tuple with one item is 
        # tuplename = ("hello ",)
        # tuple[1:2]
        # (green, yellow, *red) = fruits
        # (green, *tropic, red) = fruits  //output apple , ['mango', 'papaya', 'pineapple'] , cherry

        # similar to the list


# SETS   

        # thisset = {"apple", "banana", "cherry"}
        # thisset.add("orange")
        # thisset.update(tropical) //where tropical is another set/list/tuple/dict etc
        # thisset.remove("element") (raise an error if not found)
        # thisset.discard("element")  (doesn't raise an error if not found)
        # pop() remove an random item
        # del (delete the set)
        # clear ( empty the set)


        # SETS 
        #union , update , difference , intersection , symmetric_difference , intersection_update
        # Method	Shortcut	Description
        # add()	 	Adds an element to the set
        # clear()	 	Removes all the elements from the set
        # copy()	 	Returns a copy of the set
        # difference()	-	Returns a set containing the difference between two or more sets
        # difference_update()	-=	Removes the items in this set that are also included in another, specified set
        # discard()	 	Remove the specified item
        # intersection()	&	Returns a set, that is the intersection of two other sets
        # intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
        # isdisjoint()	 	Returns whether two sets have a intersection or not
        # issubset()	<=	Returns whether another set contains this set or not
        #         <	Returns whether all items in this set is present in other, specified set(s)
        # issuperset()	>=	Returns whether this set contains another set or not
        #         >	Returns whether all items in other, specified set(s) is present in this set
        # pop()	 	Removes an element from the set
        # remove()	 	Removes the specified element
        # symmetric_difference()	^	Returns a set with the symmetric differences of two sets
        # symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
        # union()	|	Return a set containing the union of sets
        # update()	|=	Update the set with the union of this set and others

                

# Dictionaries



