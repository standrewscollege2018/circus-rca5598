from tkinter import *
class Show:

    def __init__(self, time, capacity, available_tickets, ticket_cost):
        self._time = time
        self._capacity = capacity
        self._available_tickets = available_tickets
        self._ticket_cost = ticket_cost
        shows.append(self)
        show_times.append(self._time)
        
        

shows = []
show_times = []

Show("10am", 150, 150, 10)


root = Tk()
root.title("Ticketing")
root.geometry("300x300")


root.mainloop()
