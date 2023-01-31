import sys
import pygame # импортируем игровую библиотеку

# Функция определения победителя
def check_win(mas, sign):
    zeroes = 0
    for row in mas:
        zeroes+= row.count(0)
        if row.count(sign) == 3:
            return sign
    for col in range(3):
        if mas[0][col] == sign and mas[1][col] == sign and mas[2][col] == sign:
            return sign
    if mas[0][0] == sign and mas[1][1] == sign and mas[2][2] == sign:
        return sign
    if mas[0][2] == sign and mas[1][1] == sign and mas[2][0] == sign:
        return sign
    if zeroes==0:
        return "Ничья!"
    return False

#Создаем каркас для игры
pygame.init()
size_block = 100
margin = 15 # Отступ между квадратиками
width = heiqth = size_block*3 + margin*4 # Длина и высота квадратика

size = (width, heiqth) # создаем переменную с длинной и шириной экрана
screen = pygame.display.set_mode(size) # делаем игровое поле с нашей переменной
pygame.display.set_caption("Игра крестики-нолики") # Название игры
img = pygame.image.load("tic-tac-toe.png") # загружаем логотип картинки в игровом экране
pygame.display.set_icon(img)

#Цветовая гамма
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
mas = [[0]*3 for i in range(3)] # массив для хранение данных
query = 0 # Множество для определенния чей ход
game_over = False

while True: #Цикл обработки событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit ()
            sys.exit (0)
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over: # Обработка нажатий на игровом поле
            x_mouse, y_mouse = pygame.mouse.get_pos()
            print(f'x={x_mouse} y={y_mouse}')
            col = x_mouse//(margin+size_block)
            row = y_mouse//(margin+size_block)
            if mas [row][col] == 0: # Избавляемся от ошибки, когда можно было дважды нажать на одну клетку
                if query%2==0: # Понимание чей ход
                    mas [row][col] = 'x'
                else:
                    mas [row][col] = 'o'
                query+=1
        elif event.type ==pygame.KEYDOWN and event.key == pygame.K_SPACE: #Рестарт игры на пробел
            game_over =False
            mas = [[0]*3 for i in range(3)]
            query=0
            screen.fill(black)
    if not  game_over:
        for row in range(3):
            for col in range(3):
                if mas[row][col] =='x':
                    color = red
                elif  mas [row][col] == 'o':
                    color = green
                else:
                    color = white
                x =col * size_block +(col+1) * margin # показывает нахождение одного угла
                y = row * size_block + (row+1) * margin
                pygame.draw.rect(screen, color, (x, y, size_block, size_block)) # показывает нахождение другого угла
                if color==red:
                    pygame.draw.line(screen, white, (x,y) , (x+size_block, y+size_block), 3) # Отрисовка крестиков
                    pygame.draw.line(screen, white, (x + size_block, y), (x, y + size_block), 3)
                elif color == green:
                    pygame.draw.circle(screen, white, (x+size_block//2, y+size_block//2),size_block//2, 3)
    if(query-1)%2==0:
        game_over = check_win(mas, 'x')
    else:
        game_over = check_win(mas, 'o')

    if game_over: # Показывает кто победитель
        screen.fill(black)
        font = pygame.font.SysFont('arial', 32)
        text1 = font.render(game_over, True, white)
        text_rect = text1.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_width() / 2 - text_rect.height / 2
        screen.blit(text1 , [text_x , text_y])
    pygame.display.update()