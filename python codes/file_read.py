import os,shutil,tempfile

def create_write_read():
  with open("my_notes.txt",mode='w+') as note:
    note.write("first line\n")
    note.write("second line\n")
    note.write("third line\n")
    note.seek(0)
    print("Intial note content\n",note.read())
    
    
    # print(note.readline()) read one line after the cursor stop point which is the start of the note at 0
    # print(note.readlines()) read the whole line in list after the point which the cursor stops
  
  
# create_write_read()


def add_read():
  with open('my_notes.txt',mode='a+') as add_note:
    add_note.write("fourth line added\n")
    add_note.write("fiveth line added\n")
    add_note.flush()
    add_note.seek(0)
    print(add_note.read())

# add_read()


def create_backup():
  path_to_store = "backup_notes"
  os.makedirs(path_to_store, exist_ok=True)
  shutil.copy("my_notes.txt",path_to_store)
  shutil.move("backup_notes/my_notes.txt","backup_notes/final_notes.txt")

# create_backup()

def create_named_temp():
  with tempfile.NamedTemporaryFile(mode='w+',delete=False) as temp:
    temp.write("quote one\n")
    temp.write("quote two\n")
    temp.write("quote three\n")
    print(temp.name)
    print(temp.read())
  os.makedirs("quotes",exist_ok=True)
  shutil.move(temp.name,"quotes/moved_txt.txt")

# create_named_temp()

def create_read_temp():
  with tempfile.SpooledTemporaryFile(max_size=50,mode="w+") as temp:
    temp.write("sentences one\n")
    temp.write("sentences two\n")
    temp.write("sentences three\n")
    temp.write("sentences four\n")
    temp.write("sentences five\n")
    temp.seek(0)
    for senteces in temp.readlines():
      print(senteces.upper())
      
# create_read_temp()


def combined():
  with tempfile.NamedTemporaryFile(mode="w+",delete=False,suffix=".txt") as temp:
    temp.write("file uploaded by user\n")
    temp.write("Data")
    temp.flush()
    temp.seek(0)
    
  with tempfile.SpooledTemporaryFile(max_size=50,mode="w+") as processed:
    with open(temp.name,mode="r") as disk_temp:
      for line in disk_temp:
        processed.write(line.upper()) 
    processed.seek(0)
    print(processed.read())
  
  
  os.makedirs("uploads",exist_ok=True)
  shutil.move(temp.name,"uploads/user_data.txt")
  print(temp.name)
  print(os.path.abspath(temp.name))
  
combined()
  