from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox, Toplevel, Label




OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\DREAM PC\OneDrive\Desktop\New folder\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def handle_login():
    password = entry_1.get().strip()
    username = entry_2.get().strip()


    if username == "admin" and password == "bawn123":
        window.destroy()  # ❌ Close login window
        open_main_panel()  # ✅ Open main panel
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")


def open_main_panel():
    main_panel = Toplevel(window)
    main_panel.title("BAWN Main Panel")
    main_panel.geometry("800x600")
    main_panel.configure(bg="#FFFFFF")
    Label(main_panel, text="Welcome to the Main Panel!", font=("Arial", 20), bg="#FFFFFF").pack(pady=50)
    # You can build your main panel UI here


# === Main Login Window ===
window = Tk()
window.geometry("1440x1024")
window.configure(bg="#FFFFFF")
window.title("BAWN Login")


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


image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
canvas.create_image(720.0, 512.0, image=image_image_1)


image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
canvas.create_image(720.0, 37.0, image=image_image_2)


button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
).place(x=1358.0, y=7.0, width=64.0, height=53.0)


image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
canvas.create_image(719.0, 511.0, image=image_image_3)


image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
canvas.create_image(989.0, 511.0, image=image_image_4)


button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=handle_login,  # ✅ Replace with real login function
    relief="flat"
).place(x=890.0, y=606.0, width=199.0, height=52.0)


# === Username Entry (Now entry_2) ===
entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
canvas.create_image(993.5, 427.0, image=entry_image_2)
entry_2 = Entry(  # This is now for username (admin)
    bd=0,
    bg="#F0EFEF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=749.0,
    y=406.0,
    width=489.0,
    height=40.0
)


# === Password Entry (Now entry_1) ===
entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
canvas.create_image(995.0, 540.0, image=entry_image_1)
entry_1 = Entry(  # This is now for password
    bd=0,
    bg="#F0EFEF",
    fg="#000716",
    highlightthickness=0,
    show="*"  # 👈 Masks the password
)
entry_1.place(
    x=750.0,
    y=519.0,
    width=490.0,
    height=40.0
)
button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
).place(x=720.0, y=227.0, width=50.0, height=72.0)


window.resizable(False, False)
window.mainloop()
