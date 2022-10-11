def logscan(text):
    with open(text, 'r') as searchfile:
        for line in searchfile:
            if '<<Insert Exception 1 Message>>' in line:
                print (line + '\n   See: This SOP Link. \n')
            elif '<<Insert Exception 2 Message>>' in line:
                print (line + '\n   See: This SOP Link.\n')
            #elif '<<Additional Exceptions Message>>' in line:
                #print (line + '\n   See: This SOP Link.\n')
        else:
            print ('We couldn\'t find any other errors')
