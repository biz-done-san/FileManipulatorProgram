# FileManipulatorProgram

Recursion Backend Project 1

## Usage

### Reverse

- if argv[1] == "reverse" ... copy contents of inputpath to outputpath and reverse it.
- argv[2]: inputpath(filepath) ... This file exists when the program is executed.
- argv[3]: outputpath(filepath) ... This file DOSEN'T exist when the program is executed.

```
$ python3 file_manipulator.py "reverse" "path/to/inputFile" "path/to/outputFile"
```

### Copy

- if argv[1] == "copy" ... copy contents of inputpath to outputpath.
- argv[2]: inputpath(filepath) ... This file exists when the program is executed.
- argv[3]: outputpath(filepath) ... This file DOSEN'T exist when the program is executed.

```
$ python3 file_manipulator.py "copy" "path/to/inputFile" "path/to/outputFile"
```

### Duplicate

- if argv[1] == "duplicate-contents" ... do loop duplicating content of inputpath
- argv[2]: inputpath(filepath) ... This file exists when the program is executed.
- argv[3]: n(counter) ... This counter is used for counting duplicator

```
$ python3 file_manipulator.py "duplicate-contents" "path/to/inputFile" n
```

### Replace

- if argv[1] == "replace-string" ...
- argv[2]: inputpath(filepath) ... This file exists when the program is executed.
- argv[3]: needle(string) ... This string is used for searching the contents
- argv[4]: newstring(string) ... This string is used for replacing the strings

```
$ python3 file_manipulator.py "replace-string" "path/to/inputFile" needle newstring
```
