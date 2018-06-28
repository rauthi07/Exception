#Q1
'''try:
    a = 3
    if a < 4:
        a = a / (a - 3)
        print(a)
except ZeroDivisionError:
    print('ZeroDivisionError')'''

#Q2
'''try:
    l = [1, 2, 3]
    print(l[3])
except IndexError as message:
    print('Exception:', message)'''

#Q3output
#name error

#Q4
'''AbyB(2.0, 3.0)  :else:
	              print c
AbyB(3.0, 3.0)  :except ZeroDivisionError:
	                    print "a/b result in '''
#Q5
'''try:
    from _mats import *
except ImportError as message:
    print("Exception", message)'''

'''try:
    A=int(input('enter any integer no:'))
    print(A)
except ValueError as message:
    print ('Exception:',message)'''

'''try:
    l = [1, 2, 3]
    print(l[3])
except IndexError as message:
    print('Exception:', message)'''

#Q6
'''class AgeTooSmallError(Exception):
    pass
def main():
    age = int(input("Enter Age"))
    try:
    
        if (age<18):
            print("entered age is less than 18")
            raise AgeTooSmallError("Entered age is less than 18")

        else:
            print("Enter age less than 18")
    except NameError:
        print(' please enter age')'''
