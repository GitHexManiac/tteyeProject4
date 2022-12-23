import arcade

my_file = open("nationsPop.txt", 'r')
lines = my_file.readlines()
pop_data = []
for line in lines:
    linesplit = line.split(",")
    country_pop_data = {
        "name": linesplit[0],
        "pop": int(linesplit[1]),
        "change": float(linesplit[2])
    }

my_window = arcade.open_window(1200, 800, "Bar Graph")
arcade.set_background_color(arcade.color.HONEYDEW) #BG
arcade.start_render()

arcade.draw_line(100, 75, 100, 750, arcade.color.BLACK, 2) #Lines
arcade.draw_line(100, 75, 1100, 75, arcade.color.BLACK, 2)

arcade.draw_text("Populations of largest nations on earth", 450, 760, arcade.color.PINE_GREEN, 16) #Text
for increment in range(1,15):
    arcade.draw_text(f"{increment}00M", 20, increment*50+25, arcade.color_from_hex_string("#AD9AD0"), 14)
x_value = 120
for country in country_pop_data:
    arcade.draw_text(country_pop_data["name"], x_value, 50, arcade.color_from_hex_string("#D0C89A"), 14)
    x_value+=80
arcade.finish_render()
arcade.run()
