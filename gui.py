import tkinter as tk
from tkinter import filedialog
import json

from dat_utils import load_data_from_dat


def browse_encoding_path():
    encoding_path = filedialog.askopenfilename()
    encoding_path_entry.delete(0, tk.END)
    encoding_path_entry.insert(0, encoding_path)


def browse_names_path():
    names_path = filedialog.askopenfilename()
    names_path_entry.delete(0, tk.END)
    names_path_entry.insert(0, names_path)


def get_data():
    encoding_path = encoding_path_entry.get()
    names_path = names_path_entry.get()

    try:
        face_data = load_data_from_dat(encoding_path, names_path)
        file_path = filedialog.asksaveasfilename(
            defaultextension=".json", filetypes=[("JSON files", "*.json")]
        )
        if file_path:
            with open(file_path, "w") as f:
                json.dump(face_data, f)
                output_label.config(text="Data saved to {}".format(file_path))

    except Exception as e:
        output_label.config(text="Error: {}".format(e))

root = tk.Tk()
root.title("Load Data From Dat")

input_frame = tk.Frame(root)
input_frame.pack(pady=10)

encoding_path_label = tk.Label(input_frame, text="Encodings DAT path:")
encoding_path_entry = tk.Entry(input_frame)
encoding_path_label.grid(row=0, column=0, sticky=tk.E)
encoding_path_entry.grid(row=0, column=1)

encoding_path_button = tk.Button(
    input_frame, text="Browse", command=browse_encoding_path
)
encoding_path_button.grid(row=0, column=2, padx=10)

names_path_label = tk.Label(input_frame, text="Names DAT path:")
names_path_entry = tk.Entry(input_frame)
names_path_label.grid(row=1, column=0, sticky=tk.E)
names_path_entry.grid(row=1, column=1)

names_path_button = tk.Button(input_frame, text="Browse", command=browse_names_path)
names_path_button.grid(row=1, column=2, padx=10)

get_data_button = tk.Button(root, text="Save to JSON", command=get_data)
get_data_button.pack(pady=10)

output_label = tk.Label(root, text="")
output_label.pack()

root.mainloop()