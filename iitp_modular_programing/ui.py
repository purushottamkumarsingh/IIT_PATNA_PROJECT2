import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from data_handler import DataHandler
from cleaner import DataCleaner
from table_viewer import TableViewer

class MissingDataCleanerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Missing Data Cleaner")
        self.root.geometry("900x600")

        self.file_path = None
        self.df = None
        self.table_viewer = None

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Select CSV File:").pack(pady=5)
        tk.Button(self.root, text="Browse", command=self.load_file).pack()

        tk.Label(self.root, text="Select Fill Method:").pack(pady=5)
        self.method_var = tk.StringVar()
        self.method_dropdown = ttk.Combobox(
            self.root, textvariable=self.method_var, values=["Mean", "Median", "Mode"]
        )
        self.method_dropdown.pack()

        tk.Button(self.root, text="Clean Data", command=self.clean_data).pack(pady=10)
        tk.Button(self.root, text="Save Cleaned File", command=self.save_file).pack(pady=5)

        self.table_frame = tk.Frame(self.root)
        self.table_frame.pack(fill="both", expand=True)
        self.table_viewer = TableViewer(self.table_frame)

    def load_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if self.file_path:
            try:
                self.df = DataHandler.load_csv(self.file_path)
                self.table_viewer.show_table(self.df)
                messagebox.showinfo("Success", "File loaded successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load file: {e}")

    def clean_data(self):
        if self.df is None:
            messagebox.showerror("Error", "Please load a CSV file first.")
            return
        method = self.method_var.get()
        try:
            cleaner = DataCleaner(self.df)
            self.df = cleaner.fill_missing(method)
            self.table_viewer.show_table(self.df)
            messagebox.showinfo("Success", "Missing values filled successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def save_file(self):
        if self.df is None:
            messagebox.showerror("Error", "No cleaned data to save.")
            return
        save_path = filedialog.asksaveasfilename(defaultextension=".csv",
                                                 filetypes=[("CSV files", "*.csv")])
        if save_path:
            try:
                DataHandler.save_csv(self.df, save_path)
                messagebox.showinfo("Success", f"File saved at {save_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file: {e}")
