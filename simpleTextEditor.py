import Tkinter
from Tkinter import *
from ScrolledText import *
import tkFileDialog
import tkMessageBox
import win32api
import tempfile
import win32print


root = Tk()

def waste():
    textPad = ScrolledText(root,width=100,height=30,fg="#ffffff")
    textPad.configure(background='#6F706B')

    #create a menu

    #Open sub-menu handler
    def open_command():
        file = tkFileDialog.askopenfile(parent=root,mode='rb',title='Select a file')
        if file != None:
            textPad.delete('1.0',END)
            contents = file.read()
            root.wm_title(file.name + " : Zen Text Editor")
            textPad.insert('1.0',contents)
            file.close()

    #Save sub-menu handler
    def save_command():
        file = tkFileDialog.asksaveasfile(mode='w')
        if file != None:
            #slicing off the last character from get, as an extra return is appended to the get function call
            data = textPad.get('1.0',END+'-1c')
            file.write(data)
            root.wm_title(file.name + " : Zen Text Editor")        
            file.close()

    #Exit sub-menu handler
    def exit_command():
        if tkMessageBox.askokcancel("Quit ","Do you really want to quit?"):
            root.destroy();

    #About sub-menu handler
    def about_command():
        label = tkMessageBox.showinfo("About"," Zen Text Editor\n Copyrights @ Technobotz Inc")


    #New sub-menu handler
    def new_command():
        data = textPad.get('1.0',END+'-1c')
        if(data != ''): #with a warning prompt
            if tkMessageBox.askokcancel("New ","Do you want to save changes?"):
                save_command()            
                textPad.delete('1.0',END)        
            else: #if user refuses to save progress
                textPad.delete('1.0',END)
        else: #without any warning
            textPad.delete('1.0',END)

    #Print sub-menu handler
    def print_command():
        file = tempfile.mktemp(".txt")
        open(file,"w").write(textPad.get('1.0',END+'-1c'))
        win32api.ShellExecute(
            0,
            "printto",
            file,
            '"%s"' % win32print.GetDefaultPrinter (),
            ".",
            0
        )

    #Default handler , for unimplemented functionalities
    def default():
        print "This command does nothing"
            
    menu = Menu(root)
    root.config(menu=menu)

    filemenu = Menu(menu)
    menu.add_cascade(label="File",menu = filemenu)
    filemenu.add_command(label="New", command=new_command)
    filemenu.add_command(label="Open",command=open_command)
    filemenu.add_command(label="Open Recent",command=default)
    filemenu.add_separator()
    filemenu.add_command(label="Save",command=save_command)
    filemenu.add_command(label="Save As",command=save_command)
    filemenu.add_separator()
    filemenu.add_command(label="Print",command=print_command)
    filemenu.add_separator()
    filemenu.add_command(label="Exit",command=exit_command)

    findmenu = Menu(menu)
    menu.add_cascade(label="Find",menu=findmenu)
    findmenu.add_command(label = "Find", command = default)
    findmenu.add_command(label = "Find Next", command= default)
    findmenu.add_command(label = "Find Previous" , command = default)
    findmenu.add_separator()
    findmenu.add_command(label = "Replace", command = default)
    findmenu.add_command(label = "Replace Next", command = default)

    viewmenu = Menu(menu)
    menu.add_cascade(label="View",menu=viewmenu)
    viewmenu.add_command(label="Zoom In",command=default)
    viewmenu.add_command(label="Zoom Out",command=default)
    viewmenu.add_separator()
    viewmenu.add_command(label="Ruler",command=default)
    viewmenu.add_command(label="Layout",command=default)
    viewmenu.add_separator()
    viewmenu.add_command(label="Spell Check",command=default)
    viewmenu.add_command(label="Dictionary",command=default)

    toolmenu = Menu(menu)
    menu.add_cascade(label="Tools",menu=toolmenu)
    toolmenu.add_command(label="New Plugins",command=default)
    toolmenu.add_command(label="New Snippet",command=default)
    toolmenu.add_separator()
    toolmenu.add_command(label="Manage Shortcuts",command=default)

    premenu = Menu(menu)
    menu.add_cascade(label="Preferences",menu=premenu)
    premenu.add_command(label="User Settings",command=default)
    premenu.add_command(label="Key Bindings",command=default)
    premenu.add_separator()
    premenu.add_command(label="Themes",command=default)

    helpmenu = Menu(menu)
    menu.add_cascade(label="Help",menu = helpmenu)
    helpmenu.add_command(label="About",command=about_command)
    #end of menu creation

class EditorClass(object):

    UPDATE_PERIOD = 100 #ms

    editors = []
    updateId = None

    def __init__(self, master):
        
        self.__class__.editors.append(self)

        self.lineNumbers = ''

        # A frame to hold the three components of the widget.
        self.frame = Frame(master, bd=2, relief=SUNKEN)

        # The widgets vertical scrollbar
        self.vScrollbar = Scrollbar(self.frame, orient=VERTICAL)
        self.vScrollbar.pack(fill='y', side=RIGHT)

        # The Text widget holding the line numbers.
        self.lnText = Text(self.frame,
                width = 4,
                padx = 4,
                highlightthickness = 0,
                takefocus = 0,
                bd = 0,
                background = 'lightgrey',
                foreground = 'magenta',
                state='disabled'
        )
        self.lnText.pack(side=LEFT, fill='y')

        # The Main Text Widget
        self.text = Text(self.frame,
                width=16,
                bd=0,
                padx = 4,
                undo=True,
                background = 'white'
        )
        self.initializeMainMenu()
        self.text.pack(side=LEFT, fill=BOTH, expand=1)

        self.text.config(yscrollcommand=self.vScrollbar.set)
        self.vScrollbar.config(command=self.text.yview)

        if self.__class__.updateId is None:
            self.updateAllLineNumbers()

    def initializeMainMenu(self):
       
        #Open sub-menu handler
        def open_command():
            file = tkFileDialog.askopenfile(parent=root,mode='rb',title='Select a file')
            if file != None:
                self.text.delete('1.0',END)
                contents = file.read()
                root.wm_title(file.name + " : Zen Text Editor")
                self.text.insert('1.0',contents)
                file.close()

        #Save sub-menu handler
        def save_command():
            file = tkFileDialog.asksaveasfile(mode='w')
            if file != None:
                #slicing off the last character from get, as an extra return is appended to the get function call
                data = self.text.get('1.0',END+'-1c')
                file.write(data)
                root.wm_title(file.name + " : Zen Text Editor")        
                file.close()

        #Exit sub-menu handler
        def exit_command():
            if tkMessageBox.askokcancel("Quit ","Do you really want to quit?"):
                root.destroy();

        #About sub-menu handler
        def about_command():
            label = tkMessageBox.showinfo("About"," Zen Text Editor\n Copyrights @ Technobotz Inc")


        #New sub-menu handler
        def new_command():
            data = textPad.get('1.0',END+'-1c')
            if(data != ''): #with a warning prompt
                if tkMessageBox.askokcancel("New ","Do you want to save changes?"):
                    save_command()            
                    self.text.delete('1.0',END)        
                else: #if user refuses to save progress
                    self.text.delete('1.0',END)
            else: #without any warning
                self.text.delete('1.0',END)

        #Print sub-menu handler
        def print_command():
            file = tempfile.mktemp(".txt")
            open(file,"w").write(self.text.get('1.0',END+'-1c'))
            win32api.ShellExecute(
                0,
                "printto",
                file,
                '"%s"' % win32print.GetDefaultPrinter (),
                ".",
                0
            )

        #Default handler , for unimplemented functionalities
        def default():
            print "This command does nothing"
                
        menu = Menu(root)
        root.config(menu=menu)

        filemenu = Menu(menu)
        filemenu.config(tearoff=False)
        
        menu.add_cascade(label="File",menu = filemenu)
        filemenu.add_command(label="New", command=new_command)
        filemenu.add_command(label="Open",command=open_command)
        filemenu.add_command(label="Open Recent",command=default)
        filemenu.add_separator()
        filemenu.add_command(label="Save",command=save_command)
        filemenu.add_command(label="Save As",command=save_command)
        filemenu.add_separator()
        filemenu.add_command(label="Print",command=print_command)
        filemenu.add_command(label="Print Preview",command=default)        
        filemenu.add_separator()
        filemenu.add_command(label="Exit",command=exit_command)

        editmenu = Menu(menu)
        editmenu.config(tearoff=False)
        
        menu.add_cascade(label="Edit",menu=editmenu)
        editmenu.add_command(label="Undo",command=default)
        editmenu.add_command(label="Redo",command=default)
        editmenu.add_separator()
        editmenu.add_command(label="Cut",command=default)
        editmenu.add_command(label="Copy",command=default)        
        editmenu.add_command(label="Paste",command=default)
        editmenu.add_command(label="Delete",command=default)        
        editmenu.add_separator()
        editmenu.add_command(label="Select All",command=default)
        editmenu.add_command(label="Time/Date",command=default)

        viewmenu = Menu(menu)
        viewmenu.config(tearoff=False)
        
        menu.add_cascade(label="View",menu=viewmenu)
        viewmenu.add_command(label="Zoom In",command=default)
        viewmenu.add_command(label="Zoom Out",command=default)
        viewmenu.add_separator()
        viewmenu.add_command(label="Ruler",command=default)
        viewmenu.add_command(label="Layout",command=default)
        viewmenu.add_separator()
        viewmenu.add_command(label="Spell Check",command=default)
        viewmenu.add_command(label="Dictionary",command=default)

        findmenu = Menu(menu)
        findmenu.config(tearoff=False)
        
        menu.add_cascade(label="Find",menu=findmenu)
        findmenu.add_command(label = "Find", command = default)
        findmenu.add_command(label = "Find Next", command= default)
        findmenu.add_command(label = "Find Previous" , command = default)
        findmenu.add_separator()
        findmenu.add_command(label = "Replace", command = default)
        findmenu.add_command(label = "Replace Next", command = default)

        toolmenu = Menu(menu)
        toolmenu.config(tearoff=False)
        
        menu.add_cascade(label="Tools",menu=toolmenu)
        toolmenu.add_command(label="New Plugins",command=default)
        toolmenu.add_command(label="New Snippet",command=default)
        toolmenu.add_separator()
        toolmenu.add_command(label="Manage Shortcuts",command=default)

        premenu = Menu(menu)
        menu.add_cascade(label="Preferences",menu=premenu)
        premenu.add_command(label="User Settings",command=default)
        premenu.add_command(label="Key Bindings",command=default)
        premenu.add_separator()
        
        ThemesList = Tkinter.Menu()
        ThemesList.config(tearoff=False)
        
        premenu.add_cascade(label="Themes",menu=ThemesList)

        availableThemes = (
                'Light Theme',
                'Quartz Theme',
                'Dark Theme',
                'Trans Theme',
                'Iron Theme',
                'Shanghai Theme',
                'TajMahal Theme',
                'Rosy Theme'
            );
        
        for theme in availableThemes:
            ThemesList.add_command(label=theme,command=default)

        helpmenu = Menu(menu)
        helpmenu.config(tearoff=False)
        
        menu.add_cascade(label="Help",menu = helpmenu)
        helpmenu.add_command(label="About",command=about_command)
        #end of menu creation
   
    def getLineNumbers(self):
        
        x = 0
        line = '0'
        col= ''
        ln = ''
        
        # assume each line is at least 6 pixels high
        step = 6
        
        nl = '\n'
        lineMask = '    %s\n'
        indexMask = '@0,%d'
        
        for i in range(0, self.text.winfo_height(), step):
            
            ll, cc = self.text.index( indexMask % i).split('.')

            if line == ll:
                if col != cc:
                    col = cc
                    ln += nl
            else:
                line, col = ll, cc
                ln += (lineMask % line)[-5:]

        return ln

    def updateLineNumbers(self):

        tt = self.lnText
        ln = self.getLineNumbers()
        if self.lineNumbers != ln:
            self.lineNumbers = ln
            tt.config(state='normal')
            tt.delete('1.0', END)
            tt.insert('1.0', self.lineNumbers)
            tt.config(state='disabled')
        
    @classmethod
    def updateAllLineNumbers(cls):

        if len(cls.editors) < 1:
            cls.updateId = None
            return
        
        for ed in cls.editors:
            ed.updateLineNumbers()
        
        cls.updateId = ed.text.after(
            cls.UPDATE_PERIOD,
            cls.updateAllLineNumbers)    

def initZenEditor():

    #Creating a Paned Window to pack the editor
    pane = PanedWindow(root,orient=HORIZONTAL,opaqueresize=True)

    #creating an editor Instance
    ed = EditorClass(root)

    #adding the editor to the PanedWindow
    pane.add(ed.frame)

    pane.pack(fill='both',expand=1)

    #setting geometry
    root.geometry("800x400")
    
    #setting the icon for the application
    root.iconbitmap(r'.\resources\note_icon.ico')

    root.title(" Untitled : Zen Text Editor");
    #textPad.pack()    

if __name__ == '__main__':
    initZenEditor();
    mainloop();
