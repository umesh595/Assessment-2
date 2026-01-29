#Executing the decorator and passing the original function as argument 
def execution_logger(func):
    #original function gets hided in this wrapper when this executes the original function is called at result=func(*args)
    def wrapper(*args):
        print("Starting execution of multiply_numbers")
        result=func(*args)
        print("Completed execution of multiply_numbers")
        return result
    return wrapper
#when this executes python internally rewrites this as m_n=dec(m_n) then the original function is passed to decorator as func and then the wrapper is returned and then the arguments are passed to wrapper and then it executes returning in the result
@execution_logger
def multiply_numbers(x,y):
    return x*y
f=multiply_numbers(4,5)
print(f)