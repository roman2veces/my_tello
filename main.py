from my_tello import MyTello
import cv2, math, time

my_dron = MyTello()
my_dron.connect()

my_dron.streamon()
frame_reader = my_dron.get_frame_read()

my_dron.takeoff()
is_flying = True

while is_flying:
    img = frame_reader.frame
    cv2.imshow("drone", img)

    key = cv2.waitKey(1) & 0xff
    if key == 27:  # ESC
        break
    elif key == ord('w'):
        my_dron.move_forward(30)
    elif key == ord('s'):
        my_dron.move_back(30)
    elif key == ord('a'):
        my_dron.move_left(30)
    elif key == ord('d'):
        my_dron.move_right(30)
    elif key == ord('e'):
        my_dron.rotate_clockwise(30)
    elif key == ord('q'):
        my_dron.rotate_counter_clockwise(30)
    elif key == ord('r'):
        my_dron.move_up(30)
    elif key == ord('f'):
        my_dron.move_down(30)
    elif key == ord('l'):
        is_flying = False

my_dron.land()

