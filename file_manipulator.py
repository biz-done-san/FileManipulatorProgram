import os
import sys

class File:
    cmds = ["reverse", "copy", "duplicate-contents", "replace-string"]
    
    # Main
    # [Function Name(Parameters)]           - [Return Value]    : [Overview]
    # ========================================================================================================================
    # manipulate(arguments)                 - string            : Main method. Call "Validator" and "Executor"
    #     

    @staticmethod
    def manipulate(arguments):
        if not File.validate(arguments):
            return "Wrong arguments...!!"
        else:
            return File.execute(arguments)
    
    # Validator
    # 
    # [Function Name(Parameters)]           - [Return Value]    : [Overview]
    # ========================================================================================================================
    # validate(arguments)                   - boolean           : Main validate method
    # isValidLength(arguments)              - boolean           : Verify arguments length
    # isValidCommand(cmd)                   - boolean           : Verify arguments in commands
    # isValidArgsOfReverse(arguments)       - boolean           : Verify arguments to execute "reverse" command
    # isValidArgsOfCopy(arguments)          - boolean           : Verify arguments to execute "copy" command
    # isValidArgsOfDuplicate(arguments)     - boolean           : Verify arguments to execute "duplicate-contents" command
    # isValidArgsOfReplace(arguments)       - boolean           : Verify arguments to execute "replace-string" command
    # verifyOutputPath(outputPath)          - boolean           : Veryfy overwriting output file if output path is exist
    # 

    @staticmethod
    def validate(arguments):
        if not File.isValidLength(arguments):
            return False
        
        cmd = arguments[1]
        if not File.isValidCommand(cmd):
            return False
        
        if cmd == File.cmds[0]:
            return File.isValidArgsOfReverse(arguments)
        elif cmd == File.cmds[1]:
            return File.isValidArgsOfCopy(arguments)
        elif cmd == File.cmds[2]:
            return File.isValidArgsOfDuplicate(arguments)
        elif cmd == File.cmds[3]:
            return File.isValidArgsOfReplace(arguments)
        else:
            return False
    
    @staticmethod
    def isValidLength(arguments):
        argLen = len(arguments)
        return 4 <= argLen and argLen <= 5

    @staticmethod
    def isValidCommand(command):
        return command in File.cmds

    @staticmethod
    def isValidArgsOfReverse(arguments):
        return Helper.isFileExist(arguments[2]) and  File.verifyOutputPath(arguments[3])
    
    @staticmethod
    def isValidArgsOfCopy(arguments):
        return Helper.isFileExist(arguments[2]) and File.verifyOutputPath(arguments[3])
           
    @staticmethod
    def isValidArgsOfDuplicate(arguments):
        return Helper.isFileExist(arguments[2]) and Helper.canConvertAtoI(arguments[3]) and int(arguments[3]) >= 0
        
    @staticmethod
    def isValidArgsOfReplace(arguments):
        return Helper.isFileExist(arguments[2]) and File.verifyOutputPath(arguments[4])

    @staticmethod
    def verifyOutputPath(outputPath):
        allowOverwriting = 1
        
        if Helper.isFileExist(outputPath):
            allowOverwriting = Helper.inputUserYorN("The destination file already exists. Do you want to overwrite it?（y/N）: ")
        
        while allowOverwriting == -1:
            allowOverwriting = Helper.inputUserYorN("A different input was made. Do you want to overwrite the destination file?（y/N）: ")
        
        return bool(allowOverwriting)

    # Executor
    # 
    # [Function Name(Parameters)]           - [Return Value]    : [Overview]
    # ========================================================================================================================
    # execute(arguments)                    - string             : Main execute method
    # reverse(inputPath, outputPath)        - string             : Copy and reverse input file to output file
    # copy(inputPath, outputPath)           - string             : Copy input file to output file
    # duplicate(inputPath, n)               - string             : Duplicate the input file n times and write to it
    # replace(inputPath, needle, newstring) - string             : Replace needle to newstring in input file
    #

    @staticmethod
    def execute(arguments):
        cmd = arguments[1]
        if cmd == File.cmds[0]:
            return File.reverse(arguments[2], arguments[3])
        elif cmd == File.cmds[1]:
            return File.copy(arguments[2], arguments[3])
        elif cmd == File.cmds[2]:
            count = int(arguments[3])
            return File.duplicate(arguments[2], count)
        elif cmd == File.cmds[3]:
            return File.replace(arguments[2], arguments[3], arguments[4])
        else:
            return "Sorry, Something went wrong..."

    @staticmethod
    def reverse(inputPath, outputPath):
        print("Read file...")        
        with open(inputPath) as f:
            contents = f.read()
        print("Finshed reading file!!")
    
        contents = contents[::-1]

        print("Write file...")
        with open(outputPath, 'w') as f:
            f.write(contents)
        print("Finshed writing file!!")

        return "DONE!!!!"
    
    @staticmethod
    def copy(inputPath, outputPath):
        print("Read file...")        
        with open(inputPath) as f:
            contents = f.read()
        print("Finshed reading file!!")
    
        print("Write file...")
        with open(outputPath, 'w') as f:
            f.write(contents)
        print("Finshed writing file!!")

        return "DONE!!!!"
    
    @staticmethod
    def duplicate(inputPath, n):
        if n == 0:
            return "Didn't duplicate..."
        
        print("Read file...")
        with open(inputPath) as f:
            contents = f.read()
        print("Finshed reading file!!")

        print("duplicate string...")
        with open(inputPath, 'a') as f:
            while n > 0:
                f.write(contents)
                n -= 1
        print("Finshed Duplicating string!!")
        
        return "DONE!!!!"

    
    @staticmethod
    def replace(inputPath, needle, newstring):
        print("Read file...")
        with open(inputPath) as f:
            contents = f.read()
        print("Finshed reading file!!")

        contents = contents.replace(needle, newstring)

        print("Write file...")
        with open(inputPath, 'wt') as f:
            f.write(contents)
        print("Finshed writing file!!")

        return "DONE!!!!"

class Helper:
    # Helper
    # 
    # [Function Name(Parameters)]           - [Return Value]    : [Overview]
    # ========================================================================================================================
    # isFileExist(filepath)                  - boolean           : Check file exist
    # inputUserYorN(question)               - int               : Input and check the user prompt only Yes or No
    # canConvertAtoI(s)                     - boolean           : Verify Convertible for the string to integer
    #

    @staticmethod
    def isFileExist(filepath):
        return os.path.isfile(filepath)
    
    @staticmethod
    def inputUserYorN(question):
        inputUserPrompt = input(question)
        if inputUserPrompt == 'y' or inputUserPrompt == 'Y':
            return 1
        elif inputUserPrompt == 'n' or inputUserPrompt == 'N':
            return 0
        else:
            return -1
    
    @staticmethod
    def canConvertAtoI(s):
        try:
            int(s, 10)
            return True
        except:
            return False

if __name__ == "__main__":
    print(File.manipulate(sys.argv))