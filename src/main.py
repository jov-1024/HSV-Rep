#main script, sets up and starts the application
import color
import window

def main():
    white = color.hsv(0.0, 0.0, 1.0)
    win = window.window(white)

if __name__ == "__main__":
    main()