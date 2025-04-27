def greet(fx):
    def msg():
        print("good morning")
        fx()
        print("ok byy")
    
    return msg
  
def hello():
    print("hello world")


# can do this normally instead of creating a new variable and calling it we can use decoratos like
# hello1=greet(hello)
# hello1()

@greet
def helo():
    print("using decorator")

helo()