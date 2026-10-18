#Task 1: Writing and Testing a Decorator---------------------------------------------------
import logging
import time

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s - %(message)s - %(asctime)s", 
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="./decorator.log")

logger=logging.getLogger(__name__)

#Declare a decorator called logger_decorator
def logger_decorator(func):
    def wrapper(*args,**kwargs):
        value=func(*args, **kwargs)
        logger.info(f"Function_name: {func.__name__}, Positional_args: { args if args else "None"}, Keyword_args: {kwargs if kwargs else "None"}, Returned_value: {value} ")
        
    return wrapper
#A function that can take tuple of args or key word args or both .
@logger_decorator
def argument_type(*args,**kwargs):
   all_elems=[]
   for element in args:
       all_elems.append([element, type(element).__name__ ])
   for element in kwargs:
       value=kwargs[element]
       all_elems.append([value, type(value).__name__])        
   return all_elems
        


@logger_decorator
def sleep_time():
    time.sleep(1)
    return"One second"



#Declare a function that takes no parameters and returns nothing
@logger_decorator
def greeting():
    print("Hello World!")



#Declare a function that takes a variable number of positional arguments and returns True
@logger_decorator
def positioal_args(*args):
    if args:
        return True



#Declare a function that takes no positional arguments and a variable number of keyword arguments, and that returns logger_decorator
@logger_decorator
def kw_args(**kwargs):
    if kwargs:
        return logger_decorator




#Within the mainline code, call each of these functions
argument_type("zahra","shefa",30)
argument_type(name="zahra",lastname="shefa",age=28)
argument_type("zahra",25,True)
argument_type("zahra",False,)
argument_type(1,2,3,"zahra","shefa",a="1")

sleep_time()

greeting()

positioal_args(1,2,3,"a")
positioal_args()

kw_args(name="zahra",age=22)


