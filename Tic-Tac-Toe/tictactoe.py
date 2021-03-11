user_input = "_" * 9
user_input = [character for character in user_input]

playing_field = [[user_input[0], user_input[1], user_input[2]],
                 [user_input[3], user_input[4], user_input[5]],
                 [user_input[6], user_input[7], user_input[8]]]

line1 = playing_field[0][0] + " " + playing_field[0][1] + " " + playing_field[0][2]
line2 = playing_field[1][0] + " " + playing_field[1][1] + " " + playing_field[1][2]
line3 = playing_field[2][0] + " " + playing_field[2][1] + " " + playing_field[2][2]
print(f"---------\n| {line1} |\n| {line2} |\n| {line3} |\n---------")


def check_win(field):
    return field[0][0] == field[0][1] == field[0][2] == "X" \
           or field[1][0] == field[1][1] == field[1][2] == "X" \
           or field[2][0] == field[2][1] == field[2][2] == "X" \
           or field[0][0] == field[1][0] == field[2][0] == "X" \
           or field[0][1] == field[1][1] == field[2][1] == "X" \
           or field[0][2] == field[1][2] == field[2][2] == "X" \
           or field[0][0] == field[1][1] == field[2][2] == "X" \
           or field[2][0] == field[1][1] == field[0][2] == "X" \
           or field[0][0] == field[0][1] == field[0][2] == "O" \
           or field[1][0] == field[1][1] == field[1][2] == "O" \
           or field[2][0] == field[2][1] == field[2][2] == "O" \
           or field[0][0] == field[1][0] == field[2][0] == "O" \
           or field[0][1] == field[1][1] == field[2][1] == "O" \
           or field[0][2] == field[1][2] == field[2][2] == "O" \
           or field[0][0] == field[1][1] == field[2][2] == "O" \
           or field[2][0] == field[1][1] == field[0][2] == "O"


while True:
    coordinates = input("Enter the coordinates: ")
    coordinates = coordinates.split(" ")
    correct_options_text = ["1", "2", "3"]
    last_entry = ""
    if coordinates[0] not in correct_options_text or coordinates[1] not in correct_options_text:
        print("You should enter numbers!")
        pass
    correct_options = [1, 2, 3]
    coordinates[0] = int(coordinates[0])
    coordinates[1] = int(coordinates[1])
    if coordinates[0] not in correct_options or coordinates[1] not in correct_options:
        print("Coordinates should be from 1 to 3!")
        pass
    elif playing_field[3 - coordinates[1]][coordinates[0] - 1] == "X" \
            or playing_field[3 - coordinates[1]][coordinates[0] - 1] == "O":
        print("This cell is occupied! Choose another one!")
        pass
    else:
        if last_entry == "X":
            last_entry = "O"
        else:
            last_entry = "X"
        playing_field[3 - coordinates[1]][coordinates[0] - 1] = last_entry
    line1 = playing_field[0][0] + " " + playing_field[0][1] + " " + playing_field[0][2]
    line2 = playing_field[1][0] + " " + playing_field[1][1] + " " + playing_field[1][2]
    line3 = playing_field[2][0] + " " + playing_field[2][1] + " " + playing_field[2][2]
    print(f"---------\n| {line1} |\n| {line2} |\n| {line3} |\n---------")
    if check_win(playing_field):
        print(last_entry + " wins")
        break
