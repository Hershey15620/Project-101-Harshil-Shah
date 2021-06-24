import os 
import dropbox
path = "/home"
print(os.path.join(path, "User/Desktop", "file.txt")) 
path = "User/Documents"
print(os.path.join(path, "/home", "file.txt")) 
path = "/User"
print(os.path.join(path, "Downloads", "file.txt", "/home")) 
path = "/home"
print(os.path.join(path, "User/Public/", "Documents", "")) 
  
def upload_file(imgname):
    access_token= "sl.AzXgsj2H75jAepd4fEYZ1RbEo-Q0t9b1DLze_TXxXOi4QvjvH4HgR_GOHuB5kjczn4J7W0nsXgOjQ9W_V09solnHTqyLtvXTFb7f8AJ78mxdXwiD2O5LtbtOvDUMxkaeMHrYeW4"
    file=imgname
    file_from= file
    file_to="/testfolder/"+(imgname)
    dbx= dropbox.Dropbox(access_token)