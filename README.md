# Music Browser
Program, which extracts the data from the music database and displays it using Tkinter GUI.  
There are 2 classes: `ScrollBox` and `DataListBox`.  
`ScrollBox` class inherits from Tkinter `Listbox` class. It has a `self.scrollbar` attribute, which is a vertical scrollbar allowing to scroll through the list of items displayed in a box.  
`DataListBox` class inherits from `Scrollbox` class. It uses database connection as a data source and can be linked to another boxes, that display a dataset according to the users choice in an original box. Boxes are linked to each other via `<<ListboxSelect>>` command.
<img width="1024" alt="Screenshot 2021-12-01 at 21 04 14" src="https://user-images.githubusercontent.com/95089786/144307241-009d38aa-df31-476d-9f47-64f4cfbbffdc.png">
