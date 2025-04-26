import os
from time import sleep
from utils import intro, shutdown
open_file = None
open_filename = None
content = ''

intro()

while True:
    choose = int(input('''Choose:\n[1] Create File\n[2] Open File\n[3] Close File\n[4] Read File
[5] Write File\n[6] Delete File\n[7] Logout\n#: ''').strip())
    try:
        match choose:
            case 1: # Create File
                try:
                    name = input('Name the file: ').strip()
                    create = open(f'{name}.txt','x')
                    create.close()
                    sleep(1)
                    print(f'\nFile "{name}.txt" created!')
                except FileExistsError as fe:
                    print(f'\nError. The file "{name}" already exist.\nError: {fe}')
                print('-'*100)

            case 2: # Open File
                try:
                    enter = input('Which file do you want to open?\n#: ').strip()
                    open_file = open(enter,'r')
                    open_filename = enter
                    content = open_file.read()
                    sleep(1)
                    print('\nFile opened!')
                except FileNotFoundError as nfe:
                    print(f'\nThe file "{enter}" could not be found or does not exist.\nError: {nfe}')
                except IOError as ioe:
                    print('\nAn I/O error occurred.')
                print('-'*100)

            case 3: # Close File
                if open_file and not open_file.closed:
                    close = str(input('Close the file? [Y/N]\n#: ')).upper().strip()
                    if close in ('Y', 'YES'):
                        open_file.close()
                        print('\nFile closed!')
                        sleep(1)
                    elif close in ('N', 'NO'):
                        print('File "close" operation cancelled . . .')
                        sleep(1)
                    else:
                        print('Invalid answer!')
                else:
                    print('\nNo file is currently open!')
                print('-'*100)

            case 4: # Read File
                if open_file and not open_file.closed:
                    print(content)
                else:
                    print('\nThere is not an active open file at the moment.')
                print('-'*100)

            case 5: # Write File:
                if open_filename:
                    file_write = str(input('Do you wish to [W]rite or [R]ewrite?\n#: ')).upper().strip()
                    txt = input('Enter text:\n-> ').strip()
                    open_file.close()

                    if file_write in ('R', 'REWRITE'):
                        with open(open_filename, 'w') as f_rw:
                            f_rw.write(txt)
                        print('\nFile rewritten!')
                    elif file_write in ('W', 'WRITE'):
                        with open(open_filename, 'a') as f_w:
                            f_w.write(txt)
                        print('\nFile appended!')
                    else:
                        print('\nInvalid answer!')
                    
                    open_file = open(open_filename, 'r')
                    content = open_file.read()
                else:
                    print('\nFile not opened or found!')
                print('-'*100)

            case 6: # Delete File
                file_delete = str(input('Which file do you wish to delete?\n#: ')).strip()
                if os.path.exists(file_delete):
                    if open_file and not open_file.closed and open_filename == file_delete:
                        open_file.close()
                    os.remove(file_delete)
                    print(f'\nFile "{file_delete}" deleted successfully!')
                else:
                    print("\nThe file was not found or doesn't exist")
                print('-'*100)

            case 7: # Logout
                if open_file and not open_file.closed:
                    open_file.close()
                shutdown()
                break

            case _:
                print('Invalid option! Type a valid operation between 1-7!')
                print('-'*100)

    except ValueError as ve:
        print(f'\nError! Type a number.')
        print('-'*100)
    except IOError as ioe:
        print(f'\nCritical I/O error!\nError: {ioe}')
        print('-'*100)