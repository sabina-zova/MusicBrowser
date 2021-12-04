# Music Browser
Program, which extracts the data from the music database and displays it using Tkinter GUI.  
There are 2 classes: `ScrollBox` and `DataListBox`.  
`ScrollBox` class inherits from Tkinter `Listbox` class. It has a `self.scrollbar` attribute, which is a vertical scrollbar allowing to scroll through the list of items displayed in a box.  
`DataListBox` class inherits from `Scrollbox` class. It uses database connection as a data source and can be linked to another boxes, that display a dataset according to the users choice in an original box. Boxes are linked to each other via `<<ListboxSelect>>` command.  
To **run** the program you need to have a database of artists, albums and songs. In this particular case [music.sqlite](music.sqlite). Be aware that your database has to have the same structure and in case the name of database is differemnt, you will have to refactor the main code in places the database name is used.  
<img width="374" alt="Screenshot 2021-12-04 at 21 16 35" src="https://user-images.githubusercontent.com/95089786/144723396-19936e72-f6bf-4c51-8338-29ee802e4904.png">
## Program screenshot
<img width="1024" alt="Screenshot 2021-12-01 at 21 04 14" src="https://user-images.githubusercontent.com/95089786/144307241-009d38aa-df31-476d-9f47-64f4cfbbffdc.png">

## Git (Complete)
``` 
git clone https://github.com/sabina-zova/MusicBrowser.git 
```
