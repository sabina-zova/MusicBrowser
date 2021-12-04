import sqlite3
import tkinter


class ScrollBox(tkinter.Listbox):
    def __init__(self, window, **kwargs):
        super().__init__(window, **kwargs)

        self.scrollbar = tkinter.Scrollbar(window, orient=tkinter.VERTICAL, command=self.yview)

    def grid(self, row, column, rowspan=1, columnspan=1, sticky='nse', **kwargs):
        super().grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan, sticky=sticky, **kwargs)
        self.scrollbar.grid(row=row, column=column, sticky='nse', rowspan=rowspan)
        self['yscrollcommand'] = self.scrollbar.set


class DataListBox(ScrollBox):
    def __init__(self, window, connection, table, field, sort_order=(), **kwargs):
        super().__init__(window, **kwargs)

        self.linked_box = None
        self.link_field = None
        self.link_value = None

        self.cursor = connection.cursor()
        self.table = table
        self.field = field

        self.bind('<<ListboxSelect>>', self.on_select)

        self.sql_selection = "SELECT " + self.field + ", _id" + " FROM " + table
        if sort_order:
            self.sql_order = " ORDER BY " + ",".join(sort_order)
        else:
            self.sql_order = " ORDER BY " + self.field

    def link(self, widget, link_field):
        self.linked_box = widget
        widget.link_field = link_field

    def clear(self):
        self.delete(0, tkinter.END)

    def requery(self, link_value=None):
        if link_value and self.link_field:
            sql = self.sql_selection + " WHERE " + self.link_field + "=?" + self.sql_order
            self.cursor.execute(sql, (link_value, ))
        else:
            self.cursor.execute(self.sql_selection + self.sql_order)

        self.clear()
        for row in self.cursor:
            self.insert(tkinter.END, row[0])

        if self.linked_box:
            self.linked_box.clear()

    def on_select(self, event):
        if self.linked_box:
            if self.curselection():
                index = self.curselection()[0]
                value = self.get(index),
                if self.link_value:
                    value = value[0], self.link_value
                    sql_where = " WHERE " + self.field + "=? AND " + self.link_value + "=?"
                else:
                    sql_where = " WHERE " + self.field + "=?"

                link_id = self.cursor.execute(self.sql_selection + sql_where, value).fetchone()[1]
                self.linked_box.requery(link_id)


if __name__ == "__main__":
    conn = sqlite3.connect("music.sqlite")
    mainWindow = tkinter.Tk()
    mainWindow.title("Music DB Browser")
    mainWindow.geometry("1024x768")

    mainWindow.columnconfigure(0, weight=2)
    mainWindow.columnconfigure(1, weight=2)
    mainWindow.columnconfigure(2, weight=2)
    mainWindow.columnconfigure(3, weight=1)

    mainWindow.rowconfigure(0, weight=1)
    mainWindow.rowconfigure(1, weight=5)
    mainWindow.rowconfigure(2, weight=5)
    mainWindow.rowconfigure(3, weight=1)

    tkinter.Label(mainWindow, text="Artists").grid(row=0, column=0)
    tkinter.Label(mainWindow, text="Albums").grid(row=0, column=1)
    tkinter.Label(mainWindow, text="Songs").grid(row=0, column=2)

    artistList = DataListBox(mainWindow, conn, "artists", "name")
    artistList.grid(row=1, column=0, rowspan=2, sticky="news", padx=(30, 0))
    artistList.config(border=2, relief='sunken')

    artistList.requery()
    
    albumLV = tkinter.Variable(mainWindow)
    albumLV.set(("Choose an album",))
    albumList = DataListBox(mainWindow, conn, 'albums', 'name', sort_order=("name",))
    albumList.grid(row=1, column=1, sticky='news', padx=(30, 0))
    albumList.config(border=2, relief='sunken')

    artistList.link(albumList, "artist")

    songLV = tkinter.Variable(mainWindow)
    songLV.set(("Choose a song ", ))
    songList = DataListBox(mainWindow, conn, "songs", "title", sort_order=("track", "title"))
    songList.grid(row=1, column=2, sticky="news", padx=(30, 0))
    songList.config(border=2, relief='sunken')

    albumList.link(songList, "album")

    mainWindow.mainloop()
    print("Closing database connection")
    conn.close()
