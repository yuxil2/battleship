from src.config import ShipConfig, valid_choices, MIN_BOARD_SIZE, MAX_BOARD_SIZE

class UserInterface:
    
    @staticmethod
    def ask_board_size():
        while True:
            try:
                m = int(input(f"Enter board height ({MIN_BOARD_SIZE}-{MAX_BOARD_SIZE}): "))
                n = int(input(f"Enter board width ({MIN_BOARD_SIZE}-{MAX_BOARD_SIZE}): "))
                if MIN_BOARD_SIZE <= m <= MAX_BOARD_SIZE and MIN_BOARD_SIZE <= n <= MAX_BOARD_SIZE:
                    return m, n
            except ValueError:
                pass
            print("Invalid input. Please enter a number within the specified range.")

    @staticmethod
    def ask_ship_placement(ship: ShipConfig):
        print(f"Placing {ship}. Please specify starting coordinate and orientation.")
        x = int(input("Enter starting X coordinate: "))
        y = int(input("Enter starting Y coordinate: "))
        orientation = UserInterface.get_valid_string("Enter orientation (horizontal/vertical): ", "orientation")
        return x, y, orientation
    
    @staticmethod
    def ask_ship_counts():
        ship_counts = {}
        for ship_config in ShipConfig:
            while True:
                try:
                    count = int(input(f"How many {ship_config} do you want? "))
                    if count > 0:
                        ship_counts[ship_config] = count
                        return ship_counts
                except ValueError:
                    pass
                print("Invalid input. Please enter a positive integer.")

    @staticmethod
    def get_valid_string(prompt: str, choice_key: str) -> str:
        while True:
            response = input(prompt).lower().strip()
            if response in valid_choices[choice_key]:
                return response
            print(f"Invalid choice. Please choose from: {', '.join(valid_choices[choice_key])}")

    @staticmethod
    def inform_invalid_placement():
        print("Invalid placement. Please try again.")
