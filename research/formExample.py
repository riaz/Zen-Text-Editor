import Tkinter

def save_data(form):
    for widget in form:
        print widget.get()

def load_data(id_value, form):
    for i, widget in enumerate(form):
        widget.delete(0, 'end')
        widget.insert(0, id_value * (i + 2))

root = Tkinter.Tk()

lbl_id = Tkinter.Label(text=u'ID')
entry_id = Tkinter.Entry()
entry_load = Tkinter.Button(text=u'Load')
lbl_field1 = Tkinter.Label(text=u'Field 1')
entry_field1 = Tkinter.Entry()
entry_save = Tkinter.Button(text=u'Save')

lbl_id.grid(row=0, column=0)
entry_id.grid(row=0, column=1)
entry_load.grid(row=0, column=2)
lbl_field1.grid(row=1, column=0)
entry_field1.grid(row=1, column=1)
entry_save.grid(row=2, column=2)

form = [entry_field1]
entry_load['command'] = lambda: load_data(entry_id.get(), form)
entry_save['command'] = lambda: save_data(form)

root.mainloop()