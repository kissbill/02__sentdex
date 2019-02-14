global_list = ['h']

def defineAList():
    local_list = ['1','2','3']
    global_list.append('kaka')
    print( "For checking purposes: in defineAList, list is %s" % local_list )
   # return local_list 

def useTheList(passed_list):
    print( "For checking purposes: in useTheList, list is %s" % passed_list )

def main():
    # returned list is ignored
    returned_list = defineAList()   

    # passed_list inside useTheList is set to global_list
    useTheList(global_list) 

main()