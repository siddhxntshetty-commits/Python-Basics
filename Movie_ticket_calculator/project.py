print("""Welcome to cinemax
      1.The Odyssey
      2.Michael
      3.The Godfather""")

movie = input("Select a movie: ")
operator = input("select[Adult,Child]: ")

if movie == "1" and operator == "Adult":
    print("the price is $40")

elif movie == "1" and operator == "child":
    print("The price is $20")
elif movie == "2" and operator == "Adult":
    print("The price is $30")
elif movie == "2" and operator == "child":
    print("The price is $10")
elif movie == "3" and operator == "Adult":
    print("The price is $50")
elif movie == "3" and operator == "child":
    print("The price is $25")
else : 
    print("Invalid input")