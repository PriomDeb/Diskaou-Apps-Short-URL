from tkinter import Tk
from tkinter import *
from PIL import Image, ImageTk
import pyglet
import pyshorteners


# Adding fonts
pyglet.font.add_file("fonts/Quicksand_Bold.otf")

class ShortURL:

    def drawUI(self):
        root = Tk()
        version = "1.0"
        root.title(f"Diskaou Short URL Generator v{version}")

        window_x = 800
        window_y = 540

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        centered_x = int(screen_width / 2 - window_x / 2)
        centered_y = int(screen_height / 2 - window_y / 2)

        window_string = f"{window_x}x{window_y}+{centered_x}+{centered_y}"

        # Constant Windows size
        root.geometry(window_string)
        root.minsize(window_x, window_y)
        root.maxsize(window_x, window_y)

        # root.iconbitmap("authenticationUI/anyIcon.ico")

        main_ui = Image.open("ui/shortURLUI.png")
        resize_main_ui = main_ui.resize((window_x, window_y))
        resized_main_ui = ImageTk.PhotoImage(resize_main_ui)

        bg_canvas = Canvas(root, width=window_x, height=window_y)
        bg_canvas.pack(fill=BOTH, expand=True)
        bg_canvas.create_image(0, 0, image=resized_main_ui, anchor="nw")


        global large_url
        global short_url
        large_url = Text(root,
                         bg="black",
                         border=0,
                         highlightthickness=0,
                         font=("Quicksand Book", 14),
                         fg="white"
                         )
        large_url.pack()
        large_url.place(x=104,
                        y=146,
                        width=590,
                        height=70
                        )



        short_url = Text(root,
                         bg="black",
                         border=0,
                         highlightthickness=0,
                         font=("Quicksand Book", 14),
                         fg="white"
                         )
        short_url.pack()
        short_url.place(x=414,
                        y=260,
                        width=276,
                        height=104
                        )

        button_image = PhotoImage(file="ui/button.png")
        short_button = Button(root,
                              text="Short URL",
                              image=button_image,
                              compound=LEFT,
                              font=("Quicksand Bold", 26),
                              highlightthickness=0,
                              border=0,
                              bg="black",
                              fg="white",
                              command=self.generate_short_url,
                              )

        short_button.pack()
        short_button.place(x=104,
                           y=270,
                           width=276,
                           height=100
                           )

        root.mainloop()


    def generate_short_url(self):
        short_url.delete("1.0", END)
        source_url = large_url.get("1.0", END)[:-1]
        initialize_pyshortener = pyshorteners.Shortener()
        target_short_url = initialize_pyshortener.tinyurl.short(source_url)
        short_url.insert(INSERT, target_short_url)







short = ShortURL()
short.drawUI()


# url = "https://www.techgeekbuzz.com/blog/how-to-make-a-url-shortener-in-python/"
# shortener = pyshorteners.Shortener()
# shorted_url = shortener.tinyurl.short(url)
# print(shorted_url)
































