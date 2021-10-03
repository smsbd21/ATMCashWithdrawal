from tkinter import*

# window init
window = Tk()
window.title("BB-SMS-08")
window.geometry('955x300')
mycanva = Canvas(window, width=955, height=300, bg='#0086cb')
mycanva.place(x=-3, y=-3)
# Images source
img_bb8 = 'images/tkinter/bb8/bb8.gif'
img_bb8_object = PhotoImage(file=img_bb8)
img_dune = 'images/tkinter/bb8/dune.png'
img_dune_object = PhotoImage(file=img_dune)
# Images resized with ratio
small_img_bb8 = img_bb8_object.subsample(4,4)
small_img_dune = img_dune_object.subsample(2,2)
# Images linked with canvas
bb8_canva = mycanva.create_image(5,100, anchor=NW, image=small_img_bb8)
dune_canva = mycanva.create_image(0,0, anchor=NW, image=small_img_dune)
# Motion function
def moving_image():
    sens_x = 5
    img_coords = mycanva.coords(bb8_canva)
    img_width = small_img_bb8.width()
    print(img_coords, img_width)
    if (img_coords[0] + img_width) <= 955:
        # Moving Image Canvas Object (x, y)
        mycanva.move(bb8_canva, sens_x, 0)
    elif img_coords[0] >= 530:
        sens_x = -sens_x
        print(sens_x)
        mycanva.move(bb8_canva, sens_x, 0)
    # frequency of launched function
    window.after(40, moving_image)
    # destination
# launch moving_image
moving_image()
# Window launch
window.mainloop()