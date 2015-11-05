import Tkinterfrom Tkinter import *from codePresets import insertSnippetimport jsonimport tkFileDialogimport tkMessageBox#import win32api   -- windows only libraryimport tempfile#import win32print  -- windows only libraryimport datetimeroot = Tk()class EditorClass(object):    UPDATE_PERIOD = 100 #ms    editors = []    updateId = None    currentTheme = "Classic Theme" #This is the default theme    def __init__(self, master):        self.__class__.editors.append(self)        self.lineNumbers = ''        #rebinding Select All to Ctrl + A        root.bind_class("Text","<Control-a>", self.selectAll)        #root.bind("<Control-Q>", self.exit_command)        #root.bind("<Control-q>", self.exit_command)        #root.bind("<Control-N>", self.new_command)        #root.bind("<Control-n>", self.new_command)        #root.bind("<Control-S>", self.save_command)        #root.bind("<Control-s>", self.save_command)               # A frame to hold the three components of the widget.        self.frame = Frame(master, bd=2, relief=SUNKEN)        # The widgets vertical scrollbar        self.vScrollbar = Scrollbar(self.frame, orient=VERTICAL)        self.vScrollbar.pack(fill='y', side=RIGHT)        # The Text widget holding the line numbers.        self.lnText = Text(self.frame,                width = 4,                padx = 4,                highlightthickness = 0,                takefocus = 0,                bd = 0,                state='disabled'        )        self.lnText.pack(side=LEFT, fill='y')        # The Main Text Widget        self.text = Text(self.frame,                width=16,                bd=0,                padx = 4,                undo=True        )        self.changeTheme(self.currentTheme)        self.loadDefaults()        self.initializeMainMenu()        self.text.pack(side=LEFT, fill=BOTH, expand=1)        self.text.config(yscrollcommand=self.vScrollbar.set)        self.vScrollbar.config(command=self.text.yview)        if self.__class__.updateId is None:            self.updateAllLineNumbers()    def selectAll(self,event):        event.widget.tag_add("sel","1.0","end")    def loadDefaults(self):        settings=open('settings/user_settings.json')        data = json.load(settings)        #Setting the theme from user settings        self.changeTheme(data["theme"])                settings.close()    #Open sub-menu handler    def open_command(self,event):            file = tkFileDialog.askopenfile(parent=root,mode='rb',title='Select a file')            if file != None:                self.text.delete('1.0',END)                contents = file.read()                root.wm_title(file.name + " : Zen Text Editor")                self.text.insert('1.0',contents)                file.close()    #Save sub-menu handler    def save_command(self,event):            file = tkFileDialog.asksaveasfile(mode='w')            if file != None:                #slicing off the last character from get, as an extra return is appended to the get function call                data = self.text.get('1.0',END+'-1c')                file.write(data)                root.wm_title(file.name + " : Zen Text Editor")                        file.close()    #Exit sub-menu handler    def exit_command(self,event):            if tkMessageBox.askokcancel("Quit ","Do you really want to quit?"):                root.destroy();    #About sub-menu handler    def about_command(self):            label = tkMessageBox.showinfo("About"," Zen Text Editor\n Copyrights @ Technobotz Inc")    #New sub-menu handler    def new_command(self,event):            data = self.text.get('1.0',END+'-1c')            if(data != ''): #with a warning prompt                if tkMessageBox.askokcancel("New ","Do you want to save changes?"):                    save_command()                                self.text.delete('1.0',END)                        else: #if user refuses to save progress                    self.text.delete('1.0',END)            else: #without any warning                self.text.delete('1.0',END)            root.wm_title("Untitled : Zen Text Editor")    #Print sub-menu handler    def print_command(self):            file = tempfile.mktemp(".txt")            open(file,"w").write(self.text.get('1.0',END+'-1c'))            #This part of the code only function in a windows PC            """                        win32api.ShellExecute(                0,                "printto",                file,                '"%s"' % win32print.GetDefaultPrinter (),                ".",                0            )            """    #Default handler , for unimplemented functionalities    def default(self):            print "This command does nothing"    def fetch_date_time(self):            today_date = datetime.datetime.now().date()            today_time = datetime.datetime.now().time()            self.text.insert(Tkinter.INSERT,str(today_date) + ' ' + str(today_time))               def open_settings_window(self):            window = Tkinter.Toplevel(root)            window.title("User Settings")            window.geometry("190x50")            lbl_theme = Tkinter.Label(window,text='Set Theme')            theme = StringVar()            theme.set(self.currentTheme)            input_theme = Tkinter.Entry(window,textvariable=theme)                        #entry_load = Tkinter.Button(window,text='Load')            #lbl_field1 = Tkinter.Label(window,text='Field 1')            #entry_field1 = Tkinter.Entry(window)                        settings_save   = Tkinter.Button(window,text='Save')            settings_cancel = Tkinter.Button(window,text='Cancel')            lbl_theme.grid(row=0, column=0)            input_theme.grid(row=0, column=1)            #lbl_field1.grid(row=1, column=0)            #entry_field1.grid(row=1, column=1)            settings_save.grid(row=2, column=0)            settings_cancel.grid(row=2, column=1)                        #put as many input elements as needed into the array form , separated by comma to save their contents in the user_settings file             form = [input_theme]            settings_cancel['command'] = lambda: self.cancel_settings(window)            settings_save['command'] = lambda: self.save_settings(input_theme.get(),form,window)    def save_settings(self,theme,form,window):            settings=open('settings/user_settings.json')            data = json.load(settings)            #Setting the theme from user settings            data["theme"] = theme            self.changeTheme(data["theme"])                        settings.close() #closing the setting file in read mode            #opening the settings json in write mode            settings=open('settings/user_settings.json',"w")            settings.seek(0)                        json.dump(data, settings)            settings.close()            window.destroy()    def cancel_settings(self,window):            window.destroy()                        def initializeMainMenu(self):              menu = Menu(root)        root.config(menu=menu)        filemenu = Menu(menu)        filemenu.config(tearoff=False)        menu.add_cascade(label="File",menu = filemenu)        filemenu.add_command(label="New", command=self.new_command,accelerator="Ctrl+N")        filemenu.add_command(label="Open",command=self.open_command,accelerator="Ctrl+O")        filemenu.add_command(label="Open Recent",command=self.default)        filemenu.add_separator()        filemenu.add_command(label="Save",command=self.save_command,accelerator="Ctrl+S")        filemenu.add_command(label="Save As",command=self.save_command,accelerator="Ctrl+S")        filemenu.add_separator()        filemenu.add_command(label="Print",command=self.print_command,accelerator="Ctrl+P")        filemenu.add_command(label="Print Preview",command=self.default)                filemenu.add_separator()        filemenu.add_command(label="Exit",command=self.exit_command,accelerator="Ctrl+Q")        filemenu.bind_all("<Control-n>", self.new_command)        filemenu.bind_all("<Control-N>", self.new_command)        filemenu.bind_all("<Control-o>", self.open_command)        filemenu.bind_all("<Control-O>", self.open_command)        filemenu.bind_all("<Control-s>", self.save_command)        filemenu.bind_all("<Control-S>", self.save_command)        filemenu.bind_all("<Control-p>", self.print_command)        filemenu.bind_all("<Control-P>", self.print_command)        filemenu.bind_all("<Control-q>", self.exit_command)        filemenu.bind_all("<Control-Q>", self.exit_command)        editmenu = Menu(menu)        editmenu.config(tearoff=False)                menu.add_cascade(label="Edit",menu=editmenu)        editmenu.add_command(label="Undo",command=self.default,accelerator="Ctrl+Z")        editmenu.add_command(label="Redo",command=self.default,accelerator="Ctrl+Y")        editmenu.add_separator()        editmenu.add_command(label="Cut",command=self.default,accelerator="Ctrl+X")        editmenu.add_command(label="Copy",command=self.default,accelerator="Ctrl+C")                editmenu.add_command(label="Paste",command=self.default,accelerator="Ctrl+V")        editmenu.add_command(label="Delete",command=self.default,accelerator="Ctrl+D")                editmenu.add_separator()        editmenu.add_command(label="Select All",command=self.selectAll,accelerator="Ctrl+A")        editmenu.add_command(label="Time/Date",command=self.fetch_date_time,accelerator="Ctrl+T")        viewmenu = Menu(menu)        viewmenu.config(tearoff=False)        menu.add_cascade(label="View",menu=viewmenu)        viewmenu.add_command(label="Zoom In",command=self.default,accelerator="Ctrl++")        viewmenu.add_command(label="Zoom Out",command=self.default,accelerator="Ctrl+-")        viewmenu.add_separator()        viewmenu.add_command(label="Ruler",command=self.default)        viewmenu.add_command(label="Layout",command=self.default)        viewmenu.add_separator()        viewmenu.add_command(label="Spell Check",command=self.default,accelerator="Ctrl+G")        viewmenu.add_command(label="Dictionary",command=self.default,accelerator="Ctrl+K")        findmenu = Menu(menu)        findmenu.config(tearoff=False)        menu.add_cascade(label="Find",menu=findmenu)        findmenu.add_command(label = "Find", command = self.default,accelerator="Ctrl+F")        findmenu.add_command(label = "Find Next", command= self.default)        findmenu.add_command(label = "Find Previous" , command = self.default)        findmenu.add_separator()        findmenu.add_command(label = "Replace", command = self.default,accelerator="Ctrl+R")        findmenu.add_command(label = "Replace Next", command = self.default)        toolmenu = Menu(menu)        toolmenu.config(tearoff=False)        menu.add_cascade(label="Tools",menu=toolmenu)        toolmenu.add_command(label="New Plugins",command=self.default)        LangList = Tkinter.Menu()        LangList.config(tearoff=False)                toolmenu.add_cascade(label="Insert Snippet",menu=LangList)        availableLanguages = (                'C',                'C++',                'Java',                'Python',                'Go',                'Asm',                'Perl',                'Haskell',                'Ruby',                'C#',                'Erlang',                'Javascript',                'ActionScript',                'Lua',                'Pascal',                'Fortran',                'Tcl',                'Bash',                'Batch',                'VBScript',                'Html',                'Xml',                'NodeJS',                'Abap'            );        for lang in availableLanguages:            LangList.add_command(label=lang,command = lambda lang=lang: self.autoCode(lang))                toolmenu.add_separator()        toolmenu.add_command(label="Manage Shortcuts",command=self.default)        premenu = Menu(menu)        premenu.config(tearoff=False)               menu.add_cascade(label="Preferences",menu=premenu)        premenu.add_command(label="User Settings",command=self.open_settings_window)        premenu.add_command(label="Key Bindings",command=self.default)        premenu.add_separator()        ThemesList = Tkinter.Menu()        ThemesList.config(tearoff=False)        premenu.add_cascade(label="Themes",menu=ThemesList)        availableThemes = (                'Classic Theme',                'Eclipse Theme',                'Light Theme',                'Quartz Theme',                'Dark Theme',                'Trans Theme',                'Iron Theme',                'Shanghai Theme',                'Cyber Theme'            );        for theme in availableThemes:            ThemesList.add_command(label=theme,command = lambda theme=theme: self.changeTheme(theme), underline=0)        helpmenu = Menu(menu)        helpmenu.config(tearoff=False)               menu.add_cascade(label="Help",menu = helpmenu)        helpmenu.add_command(label="About",command=self.about_command)    def autoCode(self,lang):        #Clear the present content of the active file        #Fetch the code template using the insertSnippet external function call        #pretty print the codeSnippet to the editor        self.text.delete('1.0',END)        self.text.insert('1.0',insertSnippet(lang))         def changeTheme(self,theme):            if theme == 'Classic Theme':                self.text.configure(background='#FFFFFF',fg="#000000")                self.lnText.configure(background='#EBEBEB',fg="#333333")            if theme == 'Eclipse Theme':                self.text.configure(background='#FFFFFF',fg="#000000")                self.lnText.configure(background='#EBEBEB',fg="#888888")                            elif theme == 'Light Theme':                self.text.configure(background='#FDF6E3',fg="#586E75")                self.lnText.configure(background='#FBF1D3',fg="#333333")            elif theme == 'Quartz Theme':                self.text.configure(background='#002240',fg="#FFFFFF")                self.lnText.configure(background='#011E3A',fg="#FFFFFF")            elif theme == 'Dark Theme':                self.text.configure(background='#202020',fg="#E6E1DC")                self.lnText.configure(background='#3D3D3D',fg="#222222")            elif theme == 'Trans Theme':                self.text.configure(background='#323232',fg="#FFFFFF")                self.lnText.configure(background='#3B3B3B',fg="#FFFFFF")            elif theme == 'Iron Theme':                self.text.configure(background='#FFFFFF',fg="#4D4D4C")                self.lnText.configure(background='#F6F6F6',fg="#4D4D4C")            elif theme == 'Shanghai Theme':                self.text.configure(background='#002B36',fg="#93A1A1")                self.lnText.configure(background='#01313F',fg="#D0EDF7")            elif theme == 'Cyber Theme':                self.text.configure(background='#272822',fg="#F8F8F2")                self.lnText.configure(background='#2F3129',fg="#8F908A")            self.currentTheme = theme    def getLineNumbers(self):        x = 0        line = '0'        col= ''        ln = ''        # assume each line is at least 6 pixels high        step = 6        nl = '\n'        lineMask = '    %s\n'        indexMask = '@0,%d'        for i in range(0, self.text.winfo_height(), step):            ll, cc = self.text.index( indexMask % i).split('.')            if line == ll:                if col != cc:                    col = cc                    ln += nl            else:                line, col = ll, cc                ln += (lineMask % line)[-5:]        return ln    def updateLineNumbers(self):        tt = self.lnText        ln = self.getLineNumbers()        if self.lineNumbers != ln:            self.lineNumbers = ln            tt.config(state='normal')            tt.delete('1.0', END)            tt.insert('1.0', self.lineNumbers)            tt.config(state='disabled')    @classmethod    def updateAllLineNumbers(cls):        if len(cls.editors) < 1:            cls.updateId = None            return                for ed in cls.editors:            ed.updateLineNumbers()                cls.updateId = ed.text.after(            cls.UPDATE_PERIOD,            cls.updateAllLineNumbers)    def initZenEditor():    #Creating a Paned Window to pack the editor    pane = PanedWindow(root,orient=HORIZONTAL,opaqueresize=True)    #creating an editor Instance    ed = EditorClass(root)    #adding the editor to the PanedWindow    pane.add(ed.frame)    pane.pack(fill='both',expand=1)    #setting geometry    root.geometry("800x400")    #setting the icon for the application (OS-dependent)    #root.iconbitmap(r'./resources/note_icon.ico')    root.title(" Untitled : Zen Text Editor")if __name__ == '__main__':    initZenEditor()    mainloop()