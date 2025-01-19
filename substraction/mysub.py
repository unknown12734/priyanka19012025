def mysubstraction(x,y):
    try:
        sub = x - y
    except Exception as e:
        print(e)
    finally:
        print("process completed!")
    return sub