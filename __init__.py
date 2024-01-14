from datetime import date
import matplotlib.pyplot as plt
import os

def get_value() -> float:
    while True:
        try:
            get_spent = float(input("Introduce lo que te has gastado hoy: "))
            if get_spent < 0:
                print("Por favor, introduce un número positivo.")
                continue
            return get_spent
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número.")

def get_desktop() -> str:
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
    return desktop

def get_current_date() -> str:
    currently = str(date.today())
    currently=currently.replace(" ", "-")
    return currently

def get_lines_document() -> str:
    with open(get_desktop()+"/daily.txt", "r") as file:
        lines = len(file.readlines())
    return str(lines)

def add_to_file(spent,current_day) -> None:
    with open(get_desktop()+"/daily.txt", "a+") as file:
        lines = get_lines_document()
        file.write(str(spent)+" "+str(current_day)[2:]+"/"+lines+"\n")

def create_graph(x,y) -> None:
    plt.axes().set_facecolor("#1CC4AF")
    plt.xlabel('x - Day')
    plt.ylabel('y - Money')
    plt.title("Money spent this month")
    plt.scatter(x, y,s=30,color= "red") 
    plt.plot(x,y,color="red")
  
    plt.legend()
    plt.show()

def get_alltime_money() -> list[float]:
    with open(get_desktop()+"/daily.txt", "r") as file:
        separate_spaces = file.read().split()
    money = []
    for word in range(0, len(separate_spaces), 2):  # Skip every other word starting from index 0
        money.append(separate_spaces[word])
    return money

def get_alltime_days() -> list[str]:
    with open(get_desktop()+"/daily.txt", "r") as file:
        separate_spaces = file.read().split()
    days = []
    for i in range(1, len(separate_spaces), 2):  # Skip every other word starting from index 1
        days.append(str(separate_spaces[i]))
    return days
    
def main() -> None:
    spent = get_value()
    current_day = get_current_date()
    add_to_file(spent,current_day)
    
    x_graph = get_alltime_days() #x = days
    y_graph = get_alltime_money() #y = money
    create_graph(x_graph,y_graph)

if __name__ == "__main__":
    main()