import random

def guess_number():
    while True:
        while True:
            try:
                difficulty = int(input("Chọn mức độ khó (1: từ 1 đến 10, 2: từ 1 đến 100, 3: từ 1 đến 1000): "))
                if difficulty in [1, 2, 3]:
                    break
                else:
                    print("Chọn mức độ không hợp lệ. Vui lòng chọn lại.")
            except ValueError:
                print("Vui lòng nhập một số nguyên.")

        if difficulty == 1:
            min_num, max_num = 1, 10
        elif difficulty == 2:
            min_num, max_num = 1, 100
        else:
            min_num, max_num = 1, 1000

        secret_number = random.randint(min_num, max_num)

        # Biến số lần đoán
        num_guesses = 0
        max_guesses = 5  # Giới hạn 

        # Vòng lặp chính
        while num_guesses < max_guesses:
            num_guesses += 1

            # Biến cờ để kiểm tra xem số đã được nhập có hợp lệ không
            valid_guess = False

            # Bắt ngoại lệ khi người dùng nhập chuỗi trống hoặc không hợp lệ
            while not valid_guess:
                try:
                    user_guess = input(f"Nhập một số từ {min_num} đến {max_num}: ")
                    if not user_guess.strip():  # Kiểm tra chuỗi trống
                        raise ValueError("Bạn chưa nhập số.")
                    user_guess = int(user_guess)
                    if not min_num <= user_guess <= max_num:  # Kiểm tra giá trị hợp lệ
                        raise ValueError("Số không nằm trong khoảng đã cho.")
                    valid_guess = True  # Đánh dấu số đã nhập là hợp lệ
                except ValueError as ve:
                    if isinstance(user_guess, str) and user_guess.isalpha():  # Kiểm tra xem người dùng đã nhập chữ hay không
                        print("Yêu cầu người dùng nhập số.")
                    else:
                        print(f"Lỗi: {ve}")

            if user_guess < secret_number:
                print("Số bạn đoán nhỏ hơn. Đoán lại đi.")
            elif user_guess > secret_number:
                print("Số bạn đoán lớn hơn. Đoán lại đi.")
            else:
                print(f"Chúc mừng! Bạn đã đoán đúng sau {num_guesses} lần.")
                save_result(num_guesses)
                break

        else:
            print("Bạn đã hết số lần đoán. Số bí mật là:", secret_number)

        
        play_again = input("Bạn có muốn chơi lại không? (Y/N): ")
        if play_again.lower() != "Y":
            break

def save_result(num_guesses):
  # Xử lý tên người chơi để loại bỏ các ký tự không hỗ trợ
    player_name = input("Nhập tên người chơi: ")
    player_name_cleaned = ''.join(filter(lambda x: x.isprintable(), player_name))

    # Ghi thông tin người chơi vào tệp
    with open("D:/CuoiKiMonHoc/Python/user_guesses.txt", "a", encoding="utf-8") as file:
        file.write(f"Tên: {player_name_cleaned}, Số lần đoán: {num_guesses}\n")

    print("Bạn có thể xem lại kết quả trong tệp 'guesses.txt'.")

guess_number()