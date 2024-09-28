##Email - falam3399@gmail.com
##Name - Farhana Alam

class Star_Cinema:
    _hall_list=[]
    def entry_hall(self,hall):
        self._hall_list.append(hall)
        
        
        
class Hall(Star_Cinema):
    def __init__(self,rows,cols,hall_no):
        super().__init__()
        self._seats={}
        self._show_list=[]
        self._rows=rows
        self._cols=cols
        self._hall_no=hall_no
        
    def entry_show(self,id,movie_name,time):
        info=(id,movie_name,time)
        self._show_list.append(info)
        self._seats[id]=[[0 for i in range(self._cols)] for j in range(self._rows)]
        
        
    def book_seats(self,show_id,seat_list):
        if show_id not in self._seats:
            print("Show not found. Try again")
            return
        
        for row, col in seat_list:
            if row < 0 or row >= self._rows or col < 0 or col >= self._cols:
                print(f"Error: Seat ({row},{col}) is invalid.")
                continue
            if self._seats[show_id][row][col] == 0:
                self._seats[show_id][row][col] = 1  
                print(f"Seat no. ({row}, {col}) booked successfully.")
            else:
                print(f"Sorry!!! Seat ({row}, {col}) is already booked.")

            
    def view_show_list(self):
        print("Now premiering:")
        print("\tID\tName\t\tTime")
        for movie in self._show_list:
            print(f"\t{movie[0]}\t{movie[1]}\t{movie[2]}")
            
    def view_available_seats(self, show_id):
        if show_id not in self._seats:  
            print("Show not found. Try again")  
            return
        
        print("Available seats are:")
        ok= True
        for row in range(self._rows):
            for col in range(self._cols):
                if self._seats[show_id][row][col] == 0:
                    ok= False  
                    print(f"({row},{col})")
        if ok:
            print("No seats available")

       

cinema = Star_Cinema()
hall1 = Hall(rows=5, cols=10, hall_no=1)   
    
hall1.entry_show('001', 'Inception', '18:00')
hall1.entry_show('002', 'The Matrix', '20:00')
            
hall1.view_show_list()
hall1.view_available_seats('001')            
hall1.book_seats('001', [(0, 0), (0, 1), (1, 0)])
hall1.view_available_seats('001')
hall1.book_seats('001', [(0, 0)])