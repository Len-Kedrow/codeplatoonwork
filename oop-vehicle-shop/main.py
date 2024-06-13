from car_management import CarManager

def main():
    
    car1 = CarManager( "Honda", "Odyssy", 2006, 257755)
    car2 = CarManager( "Audi", "Q5", 2018, 55000)
    
    doing_car_stuff = 1
    choice = None
    while doing_car_stuff == 1:
        
        print("""----WELCOME----  \n
            1. Add a car  
            2. View all cars 
            3. View total number of cars 
            4. See a car's details 
            5. Service a car 
            6. Update milage  
            7. Quit \n """ )
        
        choice = int(input("What would you like to do? "))
        
        match choice:
           
            case 1: 
                print("Need to be done ")
            case 2: 
                CarManager.print_allcars()
            case 3: 
                print(f"The total number of cars  {CarManager.total_cars}")
            case 4: 
                input("What is the car ID? ")
            case 5: 
                print("Do Service a car stuff")
            case 6: 
                print("Do Update milage stuff")
            case 7:
                doing_car_stuff = 0 
                "\n"
            case _:
                print(f"{choice} has no function")

    return print("Thank you for doing car stuff.")
   
main()  




    


