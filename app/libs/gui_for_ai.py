import tkinter as tk

class AnimatedMicbutton:
    def __init__(self, root):
        self.root = root
        self.is_recording = False
        self.wave_radius = 20
        self.wave_id = None
        
        
        self.header = tk.Frame(root, width=300, height=50, bg="black")
        self.header.pack_propagate(False) # Prevents frame from shrinking to fit text
        self.header.pack()
        
        self.title_label = tk.Label(self.header, text="Titan AI", fg="orange", bg="black", font=("Arial", 14, "bold"))
        self.title_label.pack(expand=True)

        
        
        self.mic_center_x = 150 
        self.mic_center_y = 25 

        self.canvas = tk.Canvas(root, width=300, height=50, bg="black", highlightthickness=0)
        self.canvas.pack()

        self.mic_core = self.canvas.create_oval(
            self.mic_center_x - 10, self.mic_center_y - 10,
            self.mic_center_x + 10, self.mic_center_y + 10,
            fill="red", outline=''
        )

        self.control_button = tk.Button(root, text="Start Recording", command=self.toggle_recording)
        self.control_button.pack(pady=10)

    def toggle_recording(self):
        self.is_recording = not self.is_recording
        if self.is_recording:
            self.control_button.config(text="Stop Recording")
            self.animate_wave()
        else:
            self.control_button.config(text="Start Recording")
            self.stop_animation()

    def stop_animation(self):
        if self.wave_id:
            self.root.after_cancel(self.wave_id)
            self.wave_id = None
        # Clean waves but keep the red core
        for item in self.canvas.find_all():
            if item != self.mic_core:
                self.canvas.delete(item)

    def animate_wave(self):
        if not self.is_recording:
            return
        
        # Clear previous wave before drawing next
        for item in self.canvas.find_all(): 
            if item != self.mic_core:
                self.canvas.delete(item)

        radius = self.wave_radius
        self.canvas.create_oval(
            self.mic_center_x - radius, self.mic_center_y - radius,
            self.mic_center_x + radius, self.mic_center_y + radius,
            outline="red", width=2
        )

        self.wave_radius += 2
        if self.wave_radius > 40: # Reset when it hits edge
            self.wave_radius = 12
            
        self.wave_id = self.root.after(50, self.animate_wave)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Titan AI")
    
    # Calculate screen center for the top of the screen
    window_width = 300
    window_height = 160 
    screen_width = root.winfo_screenwidth()
    x_cordinate = int((screen_width / 2) - (window_width / 2))
    
    root.geometry(f"{window_width}x{window_height}+{x_cordinate}+0")
    
    app = AnimatedMicbutton(root)
    root.mainloop()
