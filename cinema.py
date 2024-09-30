##Email - falam3399@gmail.com
##Name - Farhana Alam

class Star_Cinema:
    __hall_list=[]
    def entry_hall(self,hall):
        self.__hall_list.append(hall)
        
        
        
class Hall(Star_Cinema):
    def __init__(self,rows,cols,hall_no):
        super().__init__()
        self.__seats={}
        self.__show_list=[]
        self.__rows=rows
        self.__cols=cols
        self.__hall_no=hall_no
        
    def entry_show(self,id,movie_name,time):
        info=(id,movie_name,time)
        self.__show_list.append(info)
        self.__seats[id]=[[0 for i in range(self.__cols)] for j in range(self.__rows)]
        
        
    def book_seats(self,show_id,seat_list):
        if show_id not in self.__seats:
            print("Show not found. Try again")
            return
        
        for row, col in seat_list:
            if row < 0 or row >= self.__rows or col < 0 or col >= self.__cols:
                print(f"Error: Seat ({row},{col}) is invalid.")
                continue
            if self.__seats[show_id][row][col] == 0:
                self.__seats[show_id][row][col] = 1  
                print(f"Seat no. ({row}, {col}) booked successfully.")
            else:
                print(f"Sorry!!! Seat ({row}, {col}) is already booked.")

            
    def view_show_list(self):
        print("Now premiering:")
        print("\tID\tName\t\tTime")
        for movie in self.__show_list:
            print(f"\t{movie[0]}\t{movie[1]}\t{movie[2]}")
            
    def view_available_seats(self, show_id):
        if show_id not in self.__seats:  
            print("Show not found. Try again")  
            return
        
        print("Available seats are:")
        ok= True
        for row in range(self.__rows):
            for col in range(self.__cols):
                if self.__seats[show_id][row][col] == 0:
                    ok= False  
                    print(f"({row},{col})")
        if ok:
            print("No seats available")

       
cinema = Star_Cinema()
hall1 = Hall(rows=5, cols=10, hall_no=1)   
    
hall1.entry_show('001', 'Inception', '18:00')
hall1.entry_show('002', 'The Matrix', '20:00')
            


print("Welcome to Star Cinemas")
print("Choose your option")
while True:
    n=int(input("1. View show list\n2. View available seats\n3. Book seats\n4. Exit\n"))
    if(n==1):
        hall1.view_show_list()
    elif(n==2):
        showID=input("Enter show ID\n")
        hall1.view_available_seats(showID)
    elif(n==3):
        showID=input("Enter show ID\n")
        seats_input=input("Enter seat list (row,col)\n")
        seat_list = [tuple(map(int, seat.split(','))) for seat in seats_input.split()]
        
        hall1.book_seats(showID, seat_list)
    elif(n==4):
        print("Thank you for using Star Cinemas")
        exit()
 
