from pandastable import Table

class TableViewer:
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        self.table = None

    def show_table(self, dataframe):
        for widget in self.parent_frame.winfo_children():
            widget.destroy()
        self.table = Table(self.parent_frame, dataframe=dataframe, showtoolbar=True, showstatusbar=True)
        self.table.show()
