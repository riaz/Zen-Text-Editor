import Tkinterfrom Tkinter import *import jsonimport tkFileDialogimport tkMessageBoximport win32apiimport tempfileimport win32printroot = Tk()class EditorClass(object):    UPDATE_PERIOD = 100 #ms    editors = []    updateId = None    def __init__(self, master):        self.__class__.editors.append(self)        self.lineNumbers = ''        # A frame to hold the three components of the widget.        self.frame = Frame(master, bd=2, relief=SUNKEN)        # The widgets vertical scrollbar        self.vScrollbar = Scrollbar(self.frame, orient=VERTICAL)        self.vScrollbar.pack(fill='y', side=RIGHT)        # The Text widget holding the line numbers.        self.lnText = Text(self.frame,                width = 4,                padx = 4,                highlightthickness = 0,                takefocus = 0,                bd = 0,                background = '#EBEBEB',                foreground = '#333333',                state='disabled'        )        self.lnText.pack(side=LEFT, fill='y')        # The Main Text Widget        self.text = Text(self.frame,                width=16,                bd=0,                padx = 4,                undo=True,                background = '#FFFFFF',                foreground = '#000000'        )        self.loadDefaults()        self.initializeMainMenu()        self.text.pack(side=LEFT, fill=BOTH, expand=1)        self.text.config(yscrollcommand=self.vScrollbar.set)        self.vScrollbar.config(command=self.text.yview)        if self.__class__.updateId is None:            self.updateAllLineNumbers()    def loadDefaults(self):        settings=open('research/json_data.json')        data = json.load(settings)        #Setting the theme from user settings        self.changeTheme(data["theme"])                settings.close()            def initializeMainMenu(self):              #Open sub-menu handler        def open_command():            file = tkFileDialog.askopenfile(parent=root,mode='rb',title='Select a file')            if file != None:                self.text.delete('1.0',END)                contents = file.read()                root.wm_title(file.name + " : Zen Text Editor")                self.text.insert('1.0',contents)                file.close()        #Save sub-menu handler        def save_command():            file = tkFileDialog.asksaveasfile(mode='w')            if file != None:                #slicing off the last character from get, as an extra return is appended to the get function call                data = self.text.get('1.0',END+'-1c')                file.write(data)                root.wm_title(file.name + " : Zen Text Editor")                        file.close()        #Exit sub-menu handler        def exit_command():            if tkMessageBox.askokcancel("Quit ","Do you really want to quit?"):                root.destroy();        #About sub-menu handler        def about_command():            label = tkMessageBox.showinfo("About"," Zen Text Editor\n Copyrights @ Technobotz Inc")        #New sub-menu handler        def new_command():            data = self.text.get('1.0',END+'-1c')            if(data != ''): #with a warning prompt                if tkMessageBox.askokcancel("New ","Do you want to save changes?"):                    save_command()                                self.text.delete('1.0',END)                        else: #if user refuses to save progress                    self.text.delete('1.0',END)            else: #without any warning                self.text.delete('1.0',END)            root.wm_title("Untitled : Zen Text Editor")        #Print sub-menu handler        def print_command():            file = tempfile.mktemp(".txt")            open(file,"w").write(self.text.get('1.0',END+'-1c'))            win32api.ShellExecute(                0,                "printto",                file,                '"%s"' % win32print.GetDefaultPrinter (),                ".",                0            )        #Default handler , for unimplemented functionalities        def default():            print "This command does nothing"                        menu = Menu(root)        root.config(menu=menu)        filemenu = Menu(menu)        filemenu.config(tearoff=False)        menu.add_cascade(label="File",menu = filemenu)        filemenu.add_command(label="New", command=new_command)        filemenu.add_command(label="Open",command=open_command)        filemenu.add_command(label="Open Recent",command=default)        filemenu.add_separator()        filemenu.add_command(label="Save",command=save_command)        filemenu.add_command(label="Save As",command=save_command)        filemenu.add_separator()        filemenu.add_command(label="Print",command=print_command)        filemenu.add_command(label="Print Preview",command=default)                filemenu.add_separator()        filemenu.add_command(label="Exit",command=exit_command)        editmenu = Menu(menu)        editmenu.config(tearoff=False)                menu.add_cascade(label="Edit",menu=editmenu)        editmenu.add_command(label="Undo",command=default)        editmenu.add_command(label="Redo",command=default)        editmenu.add_separator()        editmenu.add_command(label="Cut",command=default)        editmenu.add_command(label="Copy",command=default)                editmenu.add_command(label="Paste",command=default)        editmenu.add_command(label="Delete",command=default)                editmenu.add_separator()        editmenu.add_command(label="Select All",command=default)        editmenu.add_command(label="Time/Date",command=default)        viewmenu = Menu(menu)        viewmenu.config(tearoff=False)        menu.add_cascade(label="View",menu=viewmenu)        viewmenu.add_command(label="Zoom In",command=default)        viewmenu.add_command(label="Zoom Out",command=default)        viewmenu.add_separator()        viewmenu.add_command(label="Ruler",command=default)        viewmenu.add_command(label="Layout",command=default)        viewmenu.add_separator()        viewmenu.add_command(label="Spell Check",command=default)        viewmenu.add_command(label="Dictionary",command=default)        findmenu = Menu(menu)        findmenu.config(tearoff=False)        menu.add_cascade(label="Find",menu=findmenu)        findmenu.add_command(label = "Find", command = default)        findmenu.add_command(label = "Find Next", command= default)        findmenu.add_command(label = "Find Previous" , command = default)        findmenu.add_separator()        findmenu.add_command(label = "Replace", command = default)        findmenu.add_command(label = "Replace Next", command = default)        toolmenu = Menu(menu)        toolmenu.config(tearoff=False)        menu.add_cascade(label="Tools",menu=toolmenu)        toolmenu.add_command(label="New Plugins",command=default)        toolmenu.add_command(label="New Snippet",command=default)        toolmenu.add_separator()        toolmenu.add_command(label="Manage Shortcuts",command=default)        premenu = Menu(menu)        premenu.config(tearoff=False)               menu.add_cascade(label="Preferences",menu=premenu)        premenu.add_command(label="User Settings",command=default)        premenu.add_command(label="Key Bindings",command=default)        premenu.add_separator()        ThemesList = Tkinter.Menu()        ThemesList.config(tearoff=False)        premenu.add_cascade(label="Themes",menu=ThemesList)        availableThemes = (                'Classic Theme',                'Eclipse Theme',                'Light Theme',                'Quartz Theme',                'Dark Theme',                'Trans Theme',                'Iron Theme',                'Shanghai Theme',                'Cyber Theme'            );        for theme in availableThemes:            ThemesList.add_command(label=theme,command = lambda theme=theme: self.changeTheme(theme), underline=0)        helpmenu = Menu(menu)        helpmenu.config(tearoff=False)               menu.add_cascade(label="Help",menu = helpmenu)        helpmenu.add_command(label="About",command=about_command)    def changeTheme(self,theme):            if theme == 'Classic Theme':                self.text.configure(background='#FFFFFF',fg="#000000")                self.lnText.configure(background='#EBEBEB',fg="#333333")            if theme == 'Eclipse Theme':                self.text.configure(background='#FFFFFF',fg="#000000")                self.lnText.configure(background='#EBEBEB',fg="#888888")                            elif theme == 'Light Theme':                self.text.configure(background='#FDF6E3',fg="#586E75")                self.lnText.configure(background='#FBF1D3',fg="#333333")            elif theme == 'Quartz Theme':                self.text.configure(background='#002240',fg="#FFFFFF")                self.lnText.configure(background='#011E3A',fg="#FFFFFF")            elif theme == 'Dark Theme':                self.text.configure(background='#202020',fg="#E6E1DC")                self.lnText.configure(background='#3D3D3D',fg="#222222")            elif theme == 'Trans Theme':                self.text.configure(background='#323232',fg="#FFFFFF")                self.lnText.configure(background='#3B3B3B',fg="#FFFFFF")            elif theme == 'Iron Theme':                self.text.configure(background='#FFFFFF',fg="#4D4D4C")                self.lnText.configure(background='#F6F6F6',fg="#4D4D4C")            elif theme == 'Shanghai Theme':                self.text.configure(background='#002B36',fg="#93A1A1")                self.lnText.configure(background='#01313F',fg="#D0EDF7")            elif theme == 'Cyber Theme':                self.text.configure(background='#272822',fg="#F8F8F2")                self.lnText.configure(background='#2F3129',fg="#8F908A")    def getLineNumbers(self):        x = 0        line = '0'        col= ''        ln = ''        # assume each line is at least 6 pixels high        step = 6        nl = '\n'        lineMask = '    %s\n'        indexMask = '@0,%d'        for i in range(0, self.text.winfo_height(), step):            ll, cc = self.text.index( indexMask % i).split('.')            if line == ll:                if col != cc:                    col = cc                    ln += nl            else:                line, col = ll, cc                ln += (lineMask % line)[-5:]        return ln    def updateLineNumbers(self):        tt = self.lnText        ln = self.getLineNumbers()        if self.lineNumbers != ln:            self.lineNumbers = ln            tt.config(state='normal')            tt.delete('1.0', END)            tt.insert('1.0', self.lineNumbers)            tt.config(state='disabled')    @classmethod    def updateAllLineNumbers(cls):        if len(cls.editors) < 1:            cls.updateId = None            return                for ed in cls.editors:            ed.updateLineNumbers()                cls.updateId = ed.text.after(            cls.UPDATE_PERIOD,            cls.updateAllLineNumbers)    def initZenEditor():    #Creating a Paned Window to pack the editor    pane = PanedWindow(root,orient=HORIZONTAL,opaqueresize=True)    #creating an editor Instance    ed = EditorClass(root)    #adding the editor to the PanedWindow    pane.add(ed.frame)    pane.pack(fill='both',expand=1)    #setting geometry    root.geometry("800x400")    #setting the icon for the application    root.iconbitmap(r'.\resources\note_icon.ico')    root.title(" Untitled : Zen Text Editor")if __name__ == '__main__':    initZenEditor()    mainloop()