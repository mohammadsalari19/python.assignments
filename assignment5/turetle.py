import turtle
list_rang = ['','red', 'black', 'yellow', 'purple', 'orange', 'blue', 'light blue', 'dark blue', 'borwn','pink', 'green']

zele = int(input('tedad azlae ra vared konid : '))

rang = int(input('''ahomare yki az rang oa ra vared konid :\n1.red  2.black  3.yellow  4.purple  5.orange  6.blue 
7.light blue  8.dark blue  9.brown  10.pink  11.green\n'''))

zaviye =180- ((zele-2)*180)/(zele)

turtle.dot()


for i in range(zele):
    turtle.color(list_rang[rang])
    turtle.right(zaviye)
    turtle.forward(30)
    
    
turtle.done()

