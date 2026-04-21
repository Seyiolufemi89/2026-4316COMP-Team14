import pandas as pd
import matplotlib

while True:
    print ("1. Load dataset")
    print ("2. Visualisations")

    choice = input("\nEnter your choice 1-2: ")

    if choice == "1":
        df = pd.read_csv('imdb_top_1000.csv')
        print("Dataset loaded successfully!")
    
    elif choice == "2":
        if 'df' not in locals():
            print("\nPlease load the dataset first!\n")
            continue

        while True:
            print("1. Thomas Ellerton" )
            print("2. Ellie Harris")
            print("3. Mackenzie Scrivener")
            print("4. Oluwaseyi Olufemi")
            print("5. Paddy Monaghan")
            print("6. Kodi Dean")
            print("7. Tom McAdam")
            print("8. Back to main menu")

            choice = input("\nEnter your choice 1-8: ")

            if choice == "1":
                # Thomas Ellerton code
                print("Code \n")
            elif choice == "2":
                # Ellie Harris code
                print("Code \n")
            elif choice == "3":
                # Mackenzie Scrivener code
                print("Code \n")
            elif choice == "4":
                # Oluwaseyi Olufemi code
                print("Code \n")
            elif choice == "5":
                # Paddy Monaghan code
                print("Code \n")
            elif choice == "6":
                # Kodi Dean code
                print("Code \n")
            elif choice == "7":
                # Tom McAdam code
                print("Code \n")
            elif choice == "8":
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 8.\n")