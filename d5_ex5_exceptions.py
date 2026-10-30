try:
    statements
except ExceptionType:
    statements
except ExceptionType1, ExceptionType2:
    statements
except ExceptionType as e:
    # am acces la excepție
    statements
except (ExceptionType1, ExceptionType2) as e:
    statements
except: # catch-all
    statements
else:
    # everything ok
    statements
finally:
    # always will be run
    statements

# cum facem un catch-all în timp ce capturăm excepția?
try:
    something
except Exception as e:
    print("no something")
    print(e)


