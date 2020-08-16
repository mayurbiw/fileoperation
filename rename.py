# Include standard modules
import getopt, sys
import os
import datetime
import collections

#D:\Assignment\directory

full_cmd_arguments = sys.argv
argument_list = full_cmd_arguments[1:]

print(argument_list)

short_options = "f:"
long_options = ["newfilename="]

try:
    arguments, values = getopt.getopt(argument_list, short_options, long_options)
except getopt.error as err:
    # Output error, and return with an error code
    print (str(err))
    sys.exit(2)

file = dict()

# the string used to rename the file
renamestring = '0'

path = 'd:/Assignment/directory'


for current_argument, current_value in arguments:
    if current_argument in ("-f", "--newfilename"):
        print (("Enabling special output mode (%s)") % (current_value))
        renamestring = current_value

if renamestring == '0':
    print("The command is wrong")

#print("The rename string is"+renamestring)
else:
    path = path + '/' + renamestring
    #print(path)
    with os.scandir(path) as dir_contents:
         for entry in dir_contents:
            # print(entry)
            if os.path.isfile(entry):
                name = entry.name
                info = entry.stat()
                file[info.st_ctime] = entry

    od = collections.OrderedDict(sorted(file.items(),reverse= True))

    #print(file)
    # printing files in  soreted order
    print("The file names descending by date time")
    print()

    for k, v in od.items():
        print(v.name,datetime.datetime.fromtimestamp(k).strftime("%d %m %Y, %H:%M"))

    # renaming the files
    count = 1
    for k,entry in od.items():
        filename, file_extension = os.path.splitext(entry.name)
        #print(path)
        os.rename(entry, "d:/Assignment/directory/cats/"+renamestring[0:len(renamestring)-1] + str(count) + file_extension)
        file[k] = renamestring[0:len(renamestring)-1] + str(count) + file_extension
        count = count + 1


    print("The file names descending by date time")
    print()
    od = collections.OrderedDict(sorted(file.items(),reverse= True))
    for k, v in od.items():
        print(v,datetime.datetime.fromtimestamp(k).strftime("%d %m %Y, %H:%M"))
