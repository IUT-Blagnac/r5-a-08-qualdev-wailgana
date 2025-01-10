import tkinter as tk

class ClickCounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Click Counter")

        self.click_count = 0
        self.double_click_count = 0

        # Label to display the click counts
        self.label = tk.Label(root, text="Click count: 0\nDouble click count: 0", font=("Arial", 16))
        self.label.pack(pady=20)

        # Button to count the clicks
        self.click_button = tk.Button(root, text="Click me!", font=("Arial", 15), command=self.increment_count)
        self.click_button.pack(pady=10)

        # Button to reset the counts
        self.reset_button = tk.Button(root, text="Reset", font=("Arial", 15), command=self.reset_count)
        self.reset_button.pack(pady=10)

        # Button to simulate double click count
        self.double_click_button = tk.Button(root, text="Double Click here!", font=("Arial", 15), command=self.add_double_clicks)
        self.double_click_button.pack(pady=10)

    def increment_count(self):
        """Increments the click count and updates the label."""
        self.click_count += 1
        self.update_label()

    def reset_count(self):
        """Resets both click counts and updates the label."""
        self.click_count = 0
        self.double_click_count = 0
        self.update_label()

    def add_double_clicks(self):
        """Adds 2 clicks to the count every time the button is clicked."""
        self.click_count += 2
        self.double_click_count += 1
        self.update_label()

    def update_label(self):
        """Update the display label with current click counts."""
        self.label.config(text=f"Click count: {self.click_count}\nDouble click count: {self.double_click_count}")

# Create the main window
root = tk.Tk()

if __name__ == "__main__":
    app = ClickCounterApp(root)
    root.mainloop()
