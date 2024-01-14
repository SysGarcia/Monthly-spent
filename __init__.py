from collections import defaultdict
from datetime import date, datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import date2num
import os

def get_value() -> float:
    """
    Asks the user to input the amount of money spent and returns it.
    Continues to prompt the user until a valid positive float is entered.
    """
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
    """
    Returns the path to the user's desktop directory.
    """
    return os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

def get_current_date() -> str:
    """
    Returns the current date as a string in YYYY-MM-DD format.
    """
    return str(date.today())

def get_lines_document() -> str:
    """
    Returns the number of lines in the 'daily.txt' file as a string.
    """
    with open(get_desktop() + "/daily.txt", "r") as file:
        lines = len(file.readlines())
    return str(lines)

def add_to_file(current_day, spent) -> None:
    """
    Appends the given day and spent amount as a new line in 'daily.txt'.
    """
    with open(get_desktop() + "/daily.txt", "a+") as file:
        file.write(str(current_day) + " " + str(spent) + "\n")

def create_graph(x, y) -> None:
    """
    Creates and displays a scatter plot and line graph of expenses.
    x: List of dates (strings).
    y: Corresponding list of amounts spent.
    """
    # Convert string dates to datetime objects and then to matplotlib date format
    x = [date2num(datetime.strptime(date_str, "%Y-%m-%d")) for date_str in x]

    plt.axes().set_facecolor("#1CC4AF")
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator())
    plt.xlabel('Day')
    plt.ylabel('Money Spent')
    plt.title("Money Spent This Month")
    plt.scatter(x, y, s=30, color="red")
    plt.plot(x, y, color="red")
    plt.gcf().autofmt_xdate()  # Rotate date labels
    plt.legend(['Expenses'])
    plt.show()

def read_document() -> dict:
    """
    Reads the 'daily.txt' file and returns a dictionary with dates as keys and
    the sum of expenses for each date as values.
    """
    daily_sum = defaultdict(float)
    with open(os.path.join(get_desktop(), "daily.txt"), "r") as file:
        for line in file:
            parts = line.split()
            if len(parts) == 2:
                try:
                    current_date, value = parts[0], float(parts[1])
                    daily_sum[current_date] += value
                except ValueError:
                    print(f"Invalid line in file: {line.strip()}")
    return daily_sum

def get_alltime_money() -> list[float]:
    """
    Reads the 'daily.txt' file and extracts all the money values.
    
    Returns:
        list[float]: A list of all the money values (as floats) from the file.
                     The values are assumed to be in every alternate position
                     starting from the first position in each line.
    """
    with open(get_desktop() + "/daily.txt", "r") as file:
        separate_spaces = file.read().split()
    money = []
    for word in range(0, len(separate_spaces), 2):
        # Assuming every alternate entry starting from index 0 is a money value
        money.append(float(separate_spaces[word]))
    return money

def get_alltime_days() -> list[str]:
    """
    Reads the 'daily.txt' file and extracts all the dates.

    Returns:
        list[str]: A list of all the dates (as strings) from the file.
                   The dates are assumed to be in every alternate position
                   starting from the second position in each line.
    """
    with open(get_desktop() + "/daily.txt", "r") as file:
        separate_spaces = file.read().split()
    days = []
    for i in range(1, len(separate_spaces), 2):
        # Assuming every alternate entry starting from index 1 is a date
        days.append(str(separate_spaces[i]))
    return days
    
def main() -> None:
    """
    Main function to execute the program.
    
    Steps:
    1. Get the amount spent and current date.
    2. Add them to the 'daily.txt' file.
    3. Read the file to aggregate data by date.
    4. Extract dates and summed money for graphing.
    5. Create and display the graph with this data.
    """
    spent = get_value()
    current_day = get_current_date()
    add_to_file(current_day, spent)
    
    daily_data = read_document()
    x_graph = list(daily_data.keys())  # Extracted days for the x-axis
    y_graph = list(daily_data.values())  # Extracted total money spent for each day for the y-axis

    create_graph(x_graph, y_graph)

if __name__ == "__main__":
    main()
