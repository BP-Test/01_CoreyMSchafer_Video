# Before python executes any code it sets  a few special variables.
# and name is one of them.

print('This will always be run')
def main():
    print (f"First Module's Main MethodName :{__name__}")


if __name__ == '__main__':
    main()