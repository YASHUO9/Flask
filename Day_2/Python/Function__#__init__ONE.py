def function():
    print("FUNC() IN ONE.PY")
    
print("TOP LEVEL IN ONE.PY")

#This means when the file will run then the below function will work
if __name__ == '__main__':
    print('ONE.PY IS BEING RUN DIRECTLY !!')
else:
    print('ONE.PY has been imported!')
    