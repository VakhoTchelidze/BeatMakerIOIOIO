
#მუსიკის შექმნის პროგრამა

#უნდა შეიქმნას პროგრამა რომელიც მომხმარებელს საშუალებას მიცემს შექმნას მარტივი მელოდიები პროგრამაშია რსებული წინასწარ განსაზღვრული მელოდიებისა და ხმების შესახებ
#პროგრამას ექნება დრამმაშინის დიზაინი
#მომხმარებელმა უნდა შეძლოს თავისი სურვილისამებრ ანალაგოს ხმები ლუპზე
# ასევე შესაძლებელი იქნება მუსიკის სიჩქარის ცვლილება, აწყობილი მუსიკის დამახსოვრება და სურვილისამებრ უკვე დასეივებული მელოდიის თავიდან გახსნა პროგრამაში.

import time
import pygame
from pygame import mixer
pygame.init()

#ferebi
black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)
dark_gray = (50, 50, 50)
light_gray = (170, 170, 170)
blue = (0, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
gold = (212, 175, 55)

#fanjris parametrebi
WIDTH = 1400
HEIGHT = 800

#tamashis shida parametrebi
fps = 60
timer = pygame.time.Clock()
beats = 8
beatsadd = 1
instruments = 6
boxes = []
clicked = [[-1 for _ in range(beats)] for _ in range(instruments)]
active_list = [1 for _ in range(instruments)]
bpm = 205 #240
playing = True
active_length = 0
active_beat = 1
beat_changed = True

#save da load meniuebis variablebi
save_menu = False
load_menu = False
saved_beats = []
file = open('saved_beats.txt','r')
for line in file:
    saved_beats.append(line)
beat_name = ''
typing = False
index = 100

#mode gilakis parametrebi
georgian = True
hiphop = False
soul = False
mode_menu = False

#screen da fonti
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('MusikMaker')
label_font = pygame.font.Font('fast99.ttf', 30)
medium_font = pygame.font.Font('fast99.ttf', 24)

#soundebi
sound1 = mixer.Sound('sounds\georgian\sound1.wav')
sound2 = mixer.Sound('sounds\georgian\sound2.wav')
sound3 = mixer.Sound('sounds\georgian\sound3.wav')
sound4 = mixer.Sound('sounds\georgian\sound4.wav')
sound5 = mixer.Sound('sounds\georgian\sound5.wav')
sound6 = mixer.Sound('sounds\georgian\sound6.wav')

#soundebis saxelebi
sound1_name = 'Doli'
sound2_name = 'Doli2'
sound3_name = 'Doli3'
sound4_name = 'Duduki'
sound5_name = 'Acharuli'
sound6_name = 'Fanduri'

pygame.mixer.set_num_channels(instruments * 3)

def play_notes():
    for i in range(len(clicked)):
        if clicked[i][active_beat] == 1 and active_list[i] == 1:
            if i == 0:
                sound1.stop()
                sound1.play()
            if i == 1:
                sound2.stop()
                sound2.play()
            if i == 2:
                sound3.stop()
                sound3.play()
            if i == 3:
                sound4.stop()
                sound4.play()
            if i == 4:
                sound5.stop()
                sound5.play()
            if i == 5:
                sound6.stop()
                sound6.play()

def set_mode_opt(georgian_mode,hiphop_mode,soul_mode):
    if georgian_mode:
        sound1_name = 'Doli'
        sound2_name = 'Doli2'
        sound3_name = 'Doli3'
        sound4_name = 'Duduki'
        sound5_name = 'Acharuli'
        sound6_name = 'Fanduri'

        sound1 = mixer.Sound('sounds\georgian\sound1.wav')
        sound2 = mixer.Sound('sounds\georgian\sound2.wav')
        sound3 = mixer.Sound('sounds\georgian\sound3.wav')
        sound4 = mixer.Sound('sounds\georgian\sound4.wav')
        sound5 = mixer.Sound('sounds\georgian\sound5.wav')
        sound6 = mixer.Sound('sounds\georgian\sound6.wav')



    elif hiphop_mode:
        sound1_name = 'Kick'
        sound2_name = 'Hihat'
        sound3_name = 'Snare'
        sound4_name = 'Bass'
        sound5_name = 'Impact'
        sound6_name = 'Vocal'

        sound1 = mixer.Sound('sounds\hiphop\sound1.wav')
        sound2 = mixer.Sound('sounds\hiphop\sound2.wav')
        sound3 = mixer.Sound('sounds\hiphop\sound3.wav')
        sound4 = mixer.Sound('sounds\hiphop\sound4.wav')
        sound5 = mixer.Sound('sounds\hiphop\sound5.wav')
        sound6 = mixer.Sound('sounds\hiphop\sound6.wav')



    elif soul_mode:
        sound1_name = 'Loop'
        sound2_name = 'Kick'
        sound3_name = 'Snare'
        sound4_name = 'HiHat'
        sound5_name = 'String'
        sound6_name = 'Bells'

        sound1 = mixer.Sound('sounds\soul\sound1.wav')
        sound2 = mixer.Sound('sounds\soul\sound2.wav')
        sound3 = mixer.Sound('sounds\soul\sound3.wav')
        sound4 = mixer.Sound('sounds\soul\sound4.wav')
        sound5 = mixer.Sound('sounds\soul\sound5.wav')
        sound6 = mixer.Sound('sounds\soul\sound6.wav')


    return sound1, sound2, sound3, sound4, sound5, sound6, sound1_name, sound2_name, sound3_name, sound4_name, sound5_name, sound6_name
def draw_grid(clicks, beat, activelst):
    boxes = []
    left_box = pygame.draw.rect(screen, gray, [0, 0, 200, HEIGHT - 200], 5)
    bottom_box = pygame.draw.rect(screen, gray, [0, HEIGHT - 200, WIDTH, 200], 5)
    colors = [gray, white, gray]

    #instrumentebis dasaxelebebi
    sound1_text = label_font.render(sound1_name, True, colors[activelst[0]])
    screen.blit(sound1_text, (30, 30))
    sound2_text = label_font.render(sound2_name, True, colors[activelst[1]])
    screen.blit(sound2_text, (30, 130))
    sound3_text = label_font.render(sound3_name, True, colors[activelst[2]])
    screen.blit(sound3_text, (30, 230))
    sound4_text = label_font.render(sound4_name, True, colors[activelst[3]])
    screen.blit(sound4_text, (30, 330))
    sound5_text = label_font.render(sound5_name, True, colors[activelst[4]])
    screen.blit(sound5_text, (30, 430))
    sound6_text = label_font.render(sound6_name, True, colors[activelst[5]])
    screen.blit(sound6_text, (30, 530))

    #xazebi insturmentebs shoris
    for i in range(6):
        pygame.draw.line(screen, gray, (0,(i*100) + 100), (200, (i*100) + 100), 3)

    #instrumentebis beatebis chasasmeli sivrceebi
    for i in range(beats):
        for j in range(instruments):
            #gavamwvanot monishnuli figurebi
            if clicks[j][i] == -1:
                color = gray
            else:
                if activelst[j] == 1:
                    color = green
                else:
                    color = dark_gray

            rect = pygame.draw.rect(screen, color,[i * ((WIDTH - 200) // beats) + 205, (j * 100) + 5, ((WIDTH - 200) // beats) - 10, 90], 0, 3)

            pygame.draw.rect(screen, gold, [i * ((WIDTH - 200) // beats) + 200, j * 100, ((WIDTH - 200) // beats), 100], 5, 5)

            pygame.draw.rect(screen, black, [i * ((WIDTH - 200) // beats) + 200, j * 100, ((WIDTH - 200) // beats), 100],2, 5)

            boxes.append((rect,(i,j)))

        active = pygame.draw.rect(screen, blue, [beat * ((WIDTH-200) // beats) + 200, 0, ((WIDTH - 200)//beats), instruments * 100], 5, 3)

    return boxes

#save menius daxatva
def draw_save_menu(beat_name, typing):

    pygame.draw.rect(screen, red, (0, 0, WIDTH, HEIGHT))
    menu_text = label_font.render('SAVE MENU: Enter a Name for Current Beat', True, white)
    screen.blit(menu_text,(400, 25))

    saving_btn = pygame.draw.rect(screen, gray, [WIDTH // 2 - 200, HEIGHT * 0.75,400,100],0,5)
    saving_text = label_font.render('SAVE', True, white)
    screen.blit(saving_text,(WIDTH // 2 - 40, HEIGHT * 0.75 + 30))

    exit_btn = pygame.draw.rect(screen, gray, [WIDTH-200, HEIGHT-100, 180, 90], 0,5)
    exit_text = label_font.render('Close', True, white)
    screen.blit(exit_text, (WIDTH - 160, HEIGHT - 70))

    if typing:
        pygame.draw.rect(screen, dark_gray, [400, 200, 600, 200], 0, 5)
    entry_rect = pygame.draw.rect(screen, gray, [400, 200, 600, 200], 5, 5)
    entry_text = label_font.render(f'{beat_name}', True, white)
    screen.blit(entry_text,(430, 250))

    return exit_btn, saving_btn, beat_name, entry_rect

#load menius daxatva
def draw_load_menu(index):
    loaded_clicked = []
    loaded_beats = 0
    loaded_bpm = 0

    pygame.draw.rect(screen, red, (0, 0, WIDTH, HEIGHT))
    menu_text = label_font.render('LOAD MENU: Select a Beat', True, white)
    screen.blit(menu_text, (500, 25))

    loading_btn = pygame.draw.rect(screen, gray, [WIDTH // 2 - 200, HEIGHT * .87, 400, 100], 0, 5)
    loading_text = label_font.render('LOAD', True, white)
    screen.blit(loading_text, (WIDTH // 2 - 40, HEIGHT * .87 + 30))

    delete_btn = pygame.draw.rect(screen, gray, [WIDTH//2 - 500, HEIGHT * .87, 200, 100], 0, 5)
    delete_text = label_font.render('DELETE', True, white)
    screen.blit(delete_text, (WIDTH//2 - 455, HEIGHT * 0.87 + 30))

    exit_btn = pygame.draw.rect(screen, gray, [WIDTH-200, HEIGHT-100,180, 90], 0,5)
    exit_text = label_font.render('Close', True, white)
    screen.blit(exit_text, (WIDTH - 160, HEIGHT - 70))



    if 0 <= index < len(saved_beats):
        pygame.draw.rect(screen, light_gray, [190, 100 + index*50, 1000, 50])

    for beat in range(len(saved_beats)):
        if beat < 10:
            beat_clicked = []
            row_text = medium_font.render(f'{beat + 1}',True,white)
            screen.blit(row_text, (200, 100 + beat * 50))
            name_index_start = saved_beats[beat].index('name: ') + 6
            name_index_end = saved_beats[beat].index(', beats:')
            name_text = medium_font.render(saved_beats[beat][name_index_start:name_index_end], True, white)
            screen.blit(name_text, (240, 100 + beat * 50))

        if 0 <= index < len(saved_beats) and beat == index:
            beat_index_end = saved_beats[beat].index(', bpm:')
            loaded_beats = int(saved_beats[beat][name_index_end + 8: beat_index_end])
            bpm_index_end = saved_beats[beat].index(', selected:')
            loaded_bpm = int(saved_beats[beat][beat_index_end + 6 : bpm_index_end])
            loaded_clicks_string = saved_beats[beat][bpm_index_end + 14 : -3]
            loaded_clicks_rows = list(loaded_clicks_string.split('], ['))
            for row in range(len(loaded_clicks_rows)):
                loaded_clicks_row = (loaded_clicks_rows[row].split(', '))
                for item in range(len(loaded_clicks_row)):
                    if loaded_clicks_row[item] == '1' or loaded_clicks_row[item] == '-1':
                        loaded_clicks_row[item] = int(loaded_clicks_row[item])
                beat_clicked.append(loaded_clicks_row)
                loaded_clicked = beat_clicked
    loaded_info = [loaded_beats, loaded_bpm, loaded_clicked]
    loaded_rectangle = pygame.draw.rect(screen, gray, [190, 90, 1000, 600], 5, 5)
    return exit_btn, loading_btn, delete_btn, loaded_rectangle, loaded_info


def draw_mode_menu():

    pygame.draw.rect(screen, red, (0, 0, WIDTH, HEIGHT))
    menu_text = label_font.render('CHOOSE MODE', True, white)
    screen.blit(menu_text, (550, 25))

    exit_btn = pygame.draw.rect(screen, gray, [WIDTH - 200, HEIGHT - 100, 180, 90], 0, 5)
    exit_text = label_font.render('Close', True, white)
    screen.blit(exit_text, (WIDTH - 160, HEIGHT - 70))

    georgian_mode_btn = pygame.draw.rect(screen, gray, [520, 150, 300, 100], 0, 5)
    georgian_mode_text = label_font.render('GEORGIAN',True,white)
    screen.blit(georgian_mode_text, (590, 185))

    hiphop_mode_btn = pygame.draw.rect(screen, gray, [520, 275, 300, 100], 0, 5)
    hiphop_mode_text = label_font.render('HIP-HOP', True, white)
    screen.blit(hiphop_mode_text, (610, 310))

    soul_mode_btn = pygame.draw.rect(screen, gray, [520, 400, 300, 100], 0, 5)
    soul_mode_text = label_font.render('TALE', True, white)
    screen.blit(soul_mode_text, (640, 435))

    return exit_btn , georgian_mode_btn, hiphop_mode_btn, soul_mode_btn


def bpm_button():

    bpm_rect = pygame.draw.rect(screen, gray, [300, HEIGHT - 150, 200, 100], 5, 5)
    bpm_text = medium_font.render('BPM', True, white)
    screen.blit(bpm_text, (370, HEIGHT - 130))
    bpm_text2 = label_font.render(f'{bpm}', True, white)
    screen.blit(bpm_text2, (370, HEIGHT - 100))
    bpm_add_rect = pygame.draw.rect(screen, gray, [510, HEIGHT - 150, 48, 48], 0, 5)
    bpm_sub_rect = pygame.draw.rect(screen, gray, [510, HEIGHT - 100, 48, 48], 0, 5)
    add_text = medium_font.render('+5', True, white)
    sub_text = medium_font.render('-5', True, white)
    screen.blit(add_text, (520, HEIGHT - 140))
    screen.blit(sub_text, (520, HEIGHT - 90))
    return bpm_rect,bpm_sub_rect,bpm_add_rect



#mtavari loopi
run = True
while run:
    timer.tick(fps)
    screen.fill(red)
    boxes = draw_grid(clicked, active_beat, active_list)

    #qveda meniud gilakebi
    play_pause = pygame.draw.rect(screen,gray, [50, HEIGHT-150, 200, 100], 0, 5)
    play_text = label_font.render('Play/Pause', True, white)
    screen.blit(play_text,(70,HEIGHT-130))
    if playing:
        play_text2 = medium_font.render('Playing', True, dark_gray)
    else:
        play_text2 = medium_font.render('Paused', True, dark_gray)
    screen.blit(play_text2, (70, HEIGHT - 100))



    #Beatsis gilaki
    beats_rect = pygame.draw.rect(screen, gray, [600, HEIGHT - 150, 200, 100], 5, 5)
    beats_text = medium_font.render('Beats', True, white)
    screen.blit(beats_text, (670, HEIGHT - 130))
    beats_text2 = label_font.render(f'{beats}', True, white)
    screen.blit(beats_text2, (690, HEIGHT - 100))
    beats_add_rect = pygame.draw.rect(screen, gray, [810, HEIGHT - 150, 48, 48], 0, 5)
    beats_sub_rect = pygame.draw.rect(screen, gray, [810, HEIGHT - 100, 48, 48], 0, 5)
    beats_add_text = medium_font.render(f'+{beatsadd}', True, white)
    beats_sub_text = medium_font.render(f'-{beatsadd}', True, white)
    screen.blit(beats_add_text, (820, HEIGHT - 140))
    screen.blit(beats_sub_text, (820, HEIGHT - 90))

    #instrumentebis chartva gamortva
    instrument_rects = []
    for i in range(instruments):
        rect = pygame.rect.Rect((0, i * 100), (200, 100))
        instrument_rects.append(rect)

    #save da load meiuebis recti
    #save
    save_button = pygame.draw.rect(screen,gray, [900, HEIGHT - 150, 200,48],0,5 )
    save_text = medium_font.render('Save Beat', True, white)
    screen.blit(save_text, (940, HEIGHT - 140))
    #load
    load_button = pygame.draw.rect(screen, gray, [900, HEIGHT - 100, 200, 48], 0, 5)
    load_text = medium_font.render('Load Beat', True, white)
    screen.blit(load_text, (940, HEIGHT - 90))

    #boardis gasuftaveba
    clear_button = pygame.draw.rect(screen, gray, [1150, HEIGHT-150, 200, 48],5,5)
    clear_text = label_font.render('Clear', True, white)
    screen.blit(clear_text, (1210, HEIGHT - 140))

    #mode gilaki
    mode_btn = pygame.draw.rect(screen, gray, [1150, HEIGHT - 100, 200, 48], 5, 5)
    mode_text = label_font.render('Mode', True, white)
    screen.blit(mode_text, (1210, HEIGHT - 90))

    # bpms gilaki
    if hiphop:
        bpm_rect, bpm_sub_rect, bpm_add_rect = bpm_button()


    # save da load meniuebis daxatva
    if save_menu:
        exit_button, saving_button, beat_name ,entry_rectangle = draw_save_menu(beat_name, typing)

    if load_menu:
        exit_button, loading_button, delete_button, loaded_rectangle, loaded_info = draw_load_menu(index)

    #mode menius daxatva
    if mode_menu:
        exit_button, georgian_mode_button, hiphop_mode_button, soul_mode_button = draw_mode_menu()

    if beat_changed:
        play_notes()
        beat_changed = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        #boxis monishvna
        if event.type == pygame.MOUSEBUTTONDOWN and not save_menu and not load_menu and not mode_menu: #ამით ვაზღვევთ იმას რომ ჩაწერის და გახსნის მენიუები ცალკე იყოს
            for i in range(len(boxes)):
                #amit veubnebit tu mausi aris im poziciaze sadac boxia for loopidan
                if boxes[i][0].collidepoint(event.pos):
                    coords = boxes[i][1]
                    clicked[coords[1]][coords[0]] *= -1

        #play/pause gilaki
        if event.type == pygame.MOUSEBUTTONUP and not save_menu and not load_menu and not mode_menu: #ამით ვაზღვევთ იმას რომ ჩაწერის და გახსნის მენიუები ცალკე იყოს
            if play_pause.collidepoint(event.pos):
                if playing:
                    playing = False
                    sound3.stop()
                    sound1.stop()
                    sound6.stop()
                    sound4.stop()
                    sound5.stop()
                    sound2.stop()

                elif not playing:
                    playing = True



            elif beats_add_rect.collidepoint(event.pos):
                beats += beatsadd
                for i in range(len(clicked)):
                    for x in range(beatsadd):
                        clicked[i].append(-1)

            elif beats_sub_rect.collidepoint(event.pos):
                beats -= beatsadd
                for i in range(len(clicked)):
                    clicked[i].pop(-1*beatsadd)

            elif clear_button.collidepoint(event.pos):
                clicked = [[-1 for _ in range(beats)] for _ in range(instruments)]
                sound3.stop()
                sound1.stop()
                sound6.stop()
                sound4.stop()
                sound5.stop()
                sound2.stop()

            elif save_button.collidepoint(event.pos):
                save_menu = True

            elif load_button.collidepoint(event.pos):
                load_menu = True

            elif mode_btn.collidepoint(event.pos):
                mode_menu = True

            elif hiphop:

                if bpm_add_rect.collidepoint(event.pos):
                    bpm += 5

                elif bpm_sub_rect.collidepoint(event.pos):
                    bpm -= 5


            for i in range(len(instrument_rects)):
                if instrument_rects[i].collidepoint(event.pos):
                    active_list[i] *= -1

        elif event.type == pygame.MOUSEBUTTONUP:
            if exit_button.collidepoint(event.pos):
                save_menu = False
                load_menu = False
                mode_menu = False
                playing = True
                beat_name = ''
                typing = False

            if load_menu:
                if loaded_rectangle.collidepoint(event.pos):
                    index = (event.pos[1] - 100) // 50
                    # print(event.pos, index)

                if delete_button.collidepoint(event.pos):
                    if 0 <= index <= len(saved_beats):
                        saved_beats.pop(index)

                if loading_button.collidepoint(event.pos):
                    if 0 <= index <= len(saved_beats):
                        beats = loaded_info[0]
                        bpm = loaded_info[1]
                        clicked = loaded_info[2]
                        index = 100
                        load_menu = False
                        # print(loaded_info)

            if save_menu:
                if entry_rectangle.collidepoint(event.pos):
                    if typing:
                        typing = False
                    elif not typing:
                        typing = True

                if saving_button.collidepoint(event.pos):
                    file = open('saved_beats.txt', 'w')
                    saved_beats.append(f'\nname: {beat_name}, beats: {beats}, bpm: {bpm}, selected: {clicked}')
                    for i in range(len(saved_beats)):
                        file.write(str(saved_beats[i]))
                    file.close()
                    save_menu = False
                    typing = False
                    beat_name = ''

            if mode_menu:
                if georgian_mode_button.collidepoint(event.pos):
                    sound3.stop()
                    sound1.stop()
                    sound6.stop()
                    sound4.stop()
                    sound5.stop()
                    sound2.stop()
                    clicked = [[-1 for _ in range(beats)] for _ in range(instruments)]
                    georgian = True
                    soul = False
                    hiphop = False
                    mode_menu = False
                    bpm = 205
                    beats = 8
                    beatsadd = 1
                    sound1, sound2, sound3, sound4, sound5, sound6, sound1_name, sound2_name, sound3_name, sound4_name, sound5_name, sound6_name = set_mode_opt(
                        georgian, hiphop, soul)


                elif hiphop_mode_button.collidepoint(event.pos):
                    sound3.stop()
                    sound1.stop()
                    sound6.stop()
                    sound4.stop()
                    sound5.stop()
                    sound2.stop()
                    clicked = [[-1 for _ in range(beats)] for _ in range(instruments)]
                    georgian = False
                    soul = False
                    hiphop = True
                    mode_menu = False
                    bpm = 160
                    beats = 8
                    beatsadd = 1
                    sound1, sound2, sound3, sound4, sound5, sound6, sound1_name, sound2_name, sound3_name, sound4_name, sound5_name, sound6_name = set_mode_opt(
                        georgian, hiphop, soul)

                elif soul_mode_button.collidepoint(event.pos):
                    sound3.stop()
                    sound1.stop()
                    sound6.stop()
                    sound4.stop()
                    sound5.stop()
                    sound2.stop()
                    clicked = [[-1 for _ in range(beats)] for _ in range(instruments)]
                    georgian = False
                    soul = True
                    hiphop = False
                    mode_menu = False
                    bpm = 212
                    beats = 6
                    beatsadd = 3
                    sound1, sound2, sound3, sound4, sound5, sound6, sound1_name, sound2_name, sound3_name, sound4_name, sound5_name, sound6_name = set_mode_opt(
                        georgian, hiphop, soul)



        if event.type == pygame.TEXTINPUT and typing:
            beat_name += event.text

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE and len(beat_name) > 0:
                beat_name = beat_name[:-1]


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if playing:
                    playing = False
                    sound3.stop()
                    sound1.stop()
                    sound6.stop()
                    sound4.stop()
                    sound5.stop()
                    sound2.stop()

                elif not playing:
                    playing = True



    beat_length = 3600 // bpm

    if playing:
        if active_length < beat_length:
            active_length += 1
        else:
            active_length = 0
            if active_beat < beats - 1:
                active_beat += 1
                beat_changed = True
            else:
                active_beat = 0
                beat_changed = True

    pygame.display.flip()

pygame.quit()

















