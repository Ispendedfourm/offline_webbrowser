import tkinter as tk
from tkinter import ttk
from tkhtmlview import HTMLLabel
from tkinter import filedialog

class SimpleBrowser:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Web Browser")

        self.create_widgets()

    def create_widgets(self):
        # Entry to display the file path or URL
        self.url_entry = ttk.Entry(self.root, width=50)
        self.url_entry.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Button to open a local HTML file or load a URL
        self.open_button = ttk.Button(self.root, text="Open File/Load URL", command=self.load_file_or_url)
        self.open_button.grid(row=0, column=2, padx=10, pady=10)

        # HTML viewer to display web content
        self.html_viewer = HTMLLabel(self.root, html="")
        self.html_viewer.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        # Load the default about.html content
        self.load_default_html()

    def load_default_html(self):
        default_html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About Simple Browser</title>
    </head>
    <body>
    <h1>Welcome to Simple Browser</h1>
    <p>This is a simple web browser created with Python and Tkinter.</p>
    <p>It allows you to open local HTML files or load URLs.</p>
    <p>No Images, CSS or JavaScript is supported in this version.</p>
    </body>
    </html>
        """
        self.display_html(default_html)

    def load_file_or_url(self):
        input_text = self.url_entry.get()

        if input_text.startswith("http://") or input_text.startswith("https://"):
            # If the input looks like a URL, load it
            self.load_url(input_text)
        else:
            # Otherwise, treat it as a file path and try to open the file
            self.load_file(input_text)

    def load_url(self, url):
        try:
            import requests
            response = requests.get(url)
            response.raise_for_status()
            html_content = response.text
            self.display_html(html_content)
        except requests.RequestException as e:
            self.display_html("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Web server IP adress or website not found!</title>
    </head>
    <body>
    <h1>Web server IP adress or website not found! {e}</h1>
    <p>1. URL must be accurate</p>
    <p>2. Check if HTTP or HTTPS is spelled correctly</p>
    <p>3. Check if WWW is spelled correctly or required to visit this website</p>
    <p>4. If you keep seeing this error and if you're internet is not connected, to fix this: Try connecting your internet!</p>
    <p>5. If you keep seeing this error to fix this: Refresh the web browser or reinstall the web browser.</p>
    </body>
    </html>
        """)

    def load_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                html_content = file.read()
                self.display_html(html_content)
        except FileNotFoundError:
            self.display_html("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File not found!</title>
    </head>
    <body>
    <h1>File not found!</h1>
    <p>1. File must be atleast .html or .htm.</p>
    <p>2. Local file has been not found! To fix this: try putting a full file directory</p>
    <p>3. If you keep seeing this error to fix this: Refresh the web browser or reinstall the web browser.</p>
    </body>
    </html>
        """)
        except Exception as e:
            self.display_html("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File or website not found!</title>
    </head>
    <body>
    <h1>File read error! {e}</h1>
    <p>1. Make sure the file is not corrupted</p>
    <p>2. The file is unreadable</p>
    <p>3. If you keep seeing this error and you try to load a website and if you are online to fix this: try connecting it to a network or load a local file!</p>
    </body>
    </html>
        """)

    def display_html(self, html_content):
        self.html_viewer.set_html(html_content)

if __name__ == "__main__":
    root = tk.Tk()
    browser = SimpleBrowser(root)
    root.mainloop()
