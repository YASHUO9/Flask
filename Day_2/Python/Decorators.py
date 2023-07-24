#--These are mostly used in the Falsk----#

def new_decorator(func):
    """Intro decorator function"""
    def wrap_func():
        print("Some ocde before executing function")
        
        func()
        
        print("Code here, after exectuing func()")
        
    return wrap_func
    
@new_decorator
def func_needs_decorator():
    print("Please decorate me!!")
    
#Newly method:    
func_needs_decorator()


#Traditional Method
# func_needs_decorator = new_decorator(func_needs_decorator)