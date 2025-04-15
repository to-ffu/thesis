from pathlib import Path
from tkinter import Tk, Canvas, Label, Button, PhotoImage
import cv2
from PIL import Image, ImageTk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\DREAM PC\OneDrive\Desktop\New folder\build\assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# ------------------------- SETUP MAIN WINDOW -----------------------------
window = Tk()
window.geometry("1440x1024")
window.configure(bg="#FFFFFF")
window.resizable(False, False)

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=1024,
    width=1440,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

# Title
canvas.create_text(
    40, 20,
    anchor="nw",
    text="BAWN",
    fill="#000000",
    font=("Arial Black", 28 * -1)
)

# ------------------------- SIDEBAR LOGIC -----------------------------

sidebar_visible = False
sidebar = None  # Will be created when first toggled

def create_sidebar(parent):
    sidebar_canvas = Canvas(
        parent,
        bg="#FFFFFF",
        height=1024,
        width=424,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    sidebar_canvas.place(x=1016, y=0)  # Positioned to the right side

    # Load button images
    img1 = PhotoImage(file=relative_to_assets("frame2/button_1.png"))
    img2 = PhotoImage(file=relative_to_assets("frame2/button_2.png"))
    img3 = PhotoImage(file=relative_to_assets("frame2/button_3.png"))
    img4 = PhotoImage(file=relative_to_assets("frame2/button_4.png"))
    img5 = PhotoImage(file=relative_to_assets("frame2/button_5.png"))

    # Back/close button
    Button(sidebar_canvas, image=img1, borderwidth=0, command=toggle_sidebar, relief="flat").place(x=30, y=31, width=49, height=49)
    Button(sidebar_canvas, image=img2, borderwidth=0, command=lambda: print("Main Panel"), relief="flat").place(x=0, y=99, width=424, height=58)
    Button(sidebar_canvas, image=img4, borderwidth=0, command=lambda: print("Activity Log"), relief="flat").place(x=0, y=157, width=424, height=58)
    Button(sidebar_canvas, image=img3, borderwidth=0, command=lambda: print("Playback"), relief="flat").place(x=0, y=215, width=424, height=58)
    Button(sidebar_canvas, image=img5, borderwidth=0, command=lambda: print("Camera Management"), relief="flat").place(x=0, y=273, width=424, height=58)

    # Prevent garbage collection
    sidebar_canvas.img_refs = [img1, img2, img3, img4, img5]

    return sidebar_canvas

def toggle_sidebar():
    global sidebar_visible, sidebar
    if sidebar_visible:
        sidebar.place_forget()
    else:
        if sidebar is None:
            sidebar = create_sidebar(window)
        else:
            sidebar.place(x=1016, y=0)
    sidebar_visible = not sidebar_visible

# ------------------------- HAMBURGER BUTTON -----------------------------

menu_image = PhotoImage(file=relative_to_assets("frame1/button_1.png"))  # Your hamburger icon
menu_button = Button(
    image=menu_image,
    borderwidth=0,
    highlightthickness=0,
    command=toggle_sidebar,
    relief="flat"
)
menu_button.place(x=1380, y=20, width=40, height=40)

# ------------------------- VIDEO PANELS -----------------------------

frame_width = 660
frame_height = 430

video_positions = [
    (60, 80), (740, 80),
    (60, 530), (740, 530)
]

video_labels = []
text_labels = []

for i, (x, y) in enumerate(video_positions):
    canvas.create_rectangle(x, y, x + frame_width, y + frame_height, outline="#CCCCCC")
    video = Label(window, bg="black")
    video.place(x=x, y=y, width=frame_width, height=frame_height)
    video_labels.append(video)

    text = Label(window, text=f"Camera {i+1}", bg="white", fg="black", font=("Arial", 10))
    text.place(x=x + 10, y=y + frame_height - 20)
    text_labels.append(text)

# ------------------------- VIDEO FEEDS -----------------------------

camera_sources = [
    r"C:\Users\DREAM PC\Downloads\pet1 (1).mp4",
    r"C:\Users\DREAM PC\Downloads\dog2.mp4",
    r"C:\Users\DREAM PC\Downloads\dog3.mp4",
    r"C:\Users\DREAM PC\Downloads\pet3 (1).mp4"
]
caps = [cv2.VideoCapture(src) for src in camera_sources]

frame_counters = [0] * len(caps)
frame_skip = 3

def update_frames():
    for i, cap in enumerate(caps):
        ret, frame = cap.read()
        frame_counters[i] += 1
        if not ret:
            continue
        if frame_counters[i] % frame_skip != 0:
            continue
        frame = cv2.resize(frame, (frame_width, frame_height))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        video_labels[i].imgtk = imgtk
        video_labels[i].config(image=imgtk)

    window.after(30, update_frames)

update_frames()

# Cleanup on close
def on_closing():
    for cap in caps:
        cap.release()
    window.destroy()

window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()
