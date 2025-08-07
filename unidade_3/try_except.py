x = 'a'

try:
    print(x * x)
except Exception as e:
    print(e)
finally:
    print(x)