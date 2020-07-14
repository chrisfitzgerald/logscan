def logscan(text):
    with open(text, 'r') as searchfile:
        for line in searchfile:
            if 'LiquiGlobal updates failed on MASTER from the change log at' in line:
                print (line + '\n   See: https://kcura.lightning.force.com/lightning/r/ka01T000000QQxUQAW/view for more information.\n')
            elif 'The ResultSet is closed' in line:
                print (line + '\n   See: https://kcura.lightning.force.com/lightning/r/ka01T000000UkQ4QAK/view for more information.\n')
            elif 'waiting for server to start........ stopped waiting' in line:
                print (line + '\n   See: https://kcura.lightning.force.com/lightning/r/ka01T000000UmCiQAK/view for more information.\n')
            elif 'LOW_MEMORY' in line:
                print (line + '\n   See: https://kcura.lightning.force.com/lightning/r/ka01T000000UjDOQA0/view for more information.\n')
            elif 'unknown protocol' in line:
                print (line + '\n   See: https://kcura.lightning.force.com/lightning/r/ka01T000000UpMMQA0/view for more information.\n')
            elif 'Keystore was tampered with, or password was incorrect' in line:
                print (line + '\n   See: https://kcura.lightning.force.com/lightning/r/ka01T000000UieiQAC/view for more information.\n')
            elif 'Address already in use: bind' in line:
                print (line + '\n   See: https://kcura.lightning.force.com/lightning/r/ka01T000000UihzQAC/view for more information.\n')
        else:
            print ('We couldn\'t find any other errors')
