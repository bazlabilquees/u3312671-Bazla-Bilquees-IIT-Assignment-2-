#Name: Bazla Bilquees
#Student ID: u3312671 
#Case Study 2: Smart Classroom Monitor (robust implementation)
import sys
import traceback
from datetime import datetime
# -Room state and data structures -
ROOM = {
    "projector_on": False,   # bool
    "capacity": 30,          # int
    "topic": ""              # str
}

attendance = set()       # set of student names (strings)
temperatures = []        # list of float temperature readings (°C)


# ---------- Input helpers ----------
def safe_input(prompt):
    """
    Wrapper for input() which handles Ctrl+C / Ctrl+D gracefully.
    Returns a stripped string, or None if the user cancelled.
    """
    try:
        s = input(prompt)
    except (EOFError, KeyboardInterrupt):
        print("\nInput cancelled by user. Exiting program.")
        return None
    return s.strip()
def get_nonempty_string(prompt):
    while True:
        s = safe_input(prompt)
        if s is None:
            return None
        if s != "":
            return s
        print("Please enter a non-empty value.")
# - Classroom operations -
def toggle_projector():
    ROOM["projector_on"] = not ROOM["projector_on"]
    state = "ON" if ROOM["projector_on"] else "OFF"
    print(f"Projector switched {state}.")


def set_topic():
    topic = get_nonempty_string("Enter lecture topic (or blank to cancel): ")
    if topic is None:
        return
    ROOM["topic"] = topic
    print(f"Topic set to: {ROOM['topic']}")
def add_student():
    name = get_nonempty_string("Enter student name to add: ")
    if name is None:
        return
    if len(attendance) >= ROOM["capacity"]:
        print("⚠ ROOM FULL — cannot add more students.")
        return
    if name in attendance:
        print(f"{name} is already marked present (no duplicate entries).")
    else:
        attendance.add(name)
        print(f"Added {name}. Attendance count: {len(attendance)}/{ROOM['capacity']}")
def remove_student():
    name = get_nonempty_string("Enter student name to remove: ")
    if name is None:
        return
    if name in attendance:
        attendance.remove(name)
        print(f"Removed {name}. Attendance count: {len(attendance)}/{ROOM['capacity']}")
    else:
        print(f"{name} not found in attendance.")
def add_temperature():
    s = safe_input("Enter temperature reading in °C (e.g. 22.5): ")
    if s is None:
        return
    try:
        t = float(s)
    except ValueError:
        print("Invalid number. Please enter a numeric temperature (e.g. 21.3).")
        return
    temperatures.append(t)
    print(f"Temperature {t:.1f}°C added. Total readings: {len(temperatures)}")
    if t < 16 or t > 28:
        print("⚠ Temperature out of recommended range (<16°C or >28°C).")
def temp_stats():
    if not temperatures:
        return None, None, None
    tmin = min(temperatures)
    tmax = max(temperatures)
    tavg = sum(temperatures) / len(temperatures)
    return tmin, tmax, tavg
def show_temperature_stats():
    tmin, tmax, tavg = temp_stats()
    if tmin is None:
        print("No temperature readings available.")
        return
    print(f"Temperature stats — Min: {tmin:.2f}°C, Max: {tmax:.2f}°C, Avg: {tavg:.2f}°C")
    if tmin < 16 or tmax > 28:
        print("⚠ ALERT: Temperature readings out of recommended range.")
def report():
    print("\n" + "=" * 36)
    print("CLASSROOM REPORT")
    print(f"Projector: {'ON' if ROOM['projector_on'] else 'OFF'}")
    print(f"Topic: {ROOM['topic'] or '<none>'}")
    print(f"Capacity: {ROOM['capacity']}")
    print(f"Attendance ({len(attendance)}): {', '.join(sorted(attendance)) or '<none>'}")
    tmin, tmax, tavg = temp_stats()
    if tmin is None:
        print("Temperature readings: <none>")
    else:
        print(f"Temperature: min={tmin:.2f}°C, max={tmax:.2f}°C, avg={tavg:.2f}°C")
        if tmin < 16 or tmax > 28:
            print("⚠ Temperature ALERT: values out of range (<16°C or >28°C).")
    # Alerts
    if len(attendance) > ROOM["capacity"]:
        print("⚠ ROOM OVER CAPACITY!")
    if ROOM["topic"] and not ROOM["projector_on"]:
        print("⚠ Reminder: Topic is set but projector is OFF.")
    print("=" * 36 + "\n")


# -Utility: change capacity (optional) -
def set_capacity():
    s = safe_input(f"Enter new capacity (current {ROOM['capacity']}) or blank to cancel: ")
    if s is None or s == "":
        return
    try:
        val = int(s)
        if val < 0:
            print("Capacity must be a non-negative integer.")
            return
    except ValueError:
        print("Please enter an integer value.")
        return
    ROOM['capacity'] = val
    print(f"Capacity set to {ROOM['capacity']}")
# - Main program loop -
def main():
    MENU_TEXT = """\nSMART CLASSROOM MONITOR
1) Toggle projector
2) Set topic
3) Add student
4) Remove student
5) Add temperature reading
6) Show temperature stats
7) Show full report
8) Set capacity (optional)
9) Exit
"""
    while True:
        print(MENU_TEXT)
        choice = safe_input("Choose option (1-9): ")
        if choice is None:
            # user cancelled input (Ctrl+C / Ctrl+D)
            break
        choice = choice.strip()
        if choice == "1":
            toggle_projector()
        elif choice == "2":
            set_topic()
        elif choice == "3":
            add_student()
        elif choice == "4":
            remove_student()
        elif choice == "5":
            add_temperature()
        elif choice == "6":
            show_temperature_stats()
        elif choice == "7":
            report()
        elif choice == "8":
            set_capacity()
        elif choice == "9":
            print("Exiting Smart Classroom Monitor. Goodbye!")
            break
        else:
            # allow text commands too
            cmd = choice.lower()
            if cmd in ("toggle", "projector"):
                toggle_projector()
            elif cmd == "exit":
                break
            else:
                print("Invalid choice — enter 1-9 or a command (toggle/exit).")
# -Program entry with top-level exception handling -
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        # print friendly error message and record full traceback to a log file
        print("An unexpected error occurred. A log file 'classroom_error.log' was created.")
        with open("classroom_error.log", "a", encoding="utf-8") as f:
            f.write(f"\n[{datetime.now().isoformat()}] Unhandled exception:\n")
            traceback.print_exc(file=f)
        # also print the traceback snippet to console for quick debugging
        traceback.print_exc()
        sys.exit(1)
