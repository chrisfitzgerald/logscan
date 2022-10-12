def logscan(text):
    with open(text, 'r') as searchfile:
        for line in searchfile:
            if '[0x0001]' in line:
                print (line + '\n   See: https://github.com/chrisfitzgerald/logscan \n')
            if '[0x0002]' in line:
                print (line + '\n   See: https://github.com/chrisfitzgerald/logscan \n')
        #   if '<<Additional Exceptions Message>>' in line:
        #        print (line + '\n   See: This SOP Link.\n')
        else:
            print ('We couldn\'t find any other errors')
