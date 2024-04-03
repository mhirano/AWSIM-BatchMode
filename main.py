# 環境設定
# 自分の環境に合わせて変更してください
template_path="ChangeCameraParameters.cs"
script_path="ChangeCameraParameters_fill.cs"
# script_path="/home/mhirano/Documents/Projects/AWSIM/Assets/AWSIM/Scripts/ChangeCameraParameters.cs"


# 新しいパラメータたち
camera1_pos_x = 225.2
camera1_pos_y = 2
camera1_pos_z = -255
camera1_angle_x = 0
camera1_angle_y = -60
camera1_angle_z = 0
camera1_focalLength = 25

camera2_pos_x = 170
camera2_pos_y = 2
camera2_pos_z = -235
camera2_angle_x = 0
camera2_angle_y = -240
camera2_angle_z = 0
camera2_focalLength = 25

camera3_pos_x = 200
camera3_pos_y = 2
camera3_pos_z = -260
camera3_angle_x = 0
camera3_angle_y = 0
camera3_angle_z = 0
camera3_focalLength = 25

fr = open(template_path, 'r')
fw = open(script_path, 'w')
while True:
    line = fr.readline()

    # Break if EOF
    if line == '':
        break

    if line.find("CAMERA1_POSITION_X") != -1:
        line = line.replace("old_pos.x", str(camera1_pos_x))
        print(line, file=fw, end='')
        continue

    if line.find("CAMERA1_POSITION_Y") != -1:
        line = line.replace("old_pos.y", str(camera1_pos_y))
        print(line, file=fw, end='')
        continue

    if line.find("CAMERA1_POSITION_Z") != -1:
        line = line.replace("old_pos.z", str(camera1_pos_z))
        print(line, file=fw, end='')
        continue

    if line.find("CAMERA1_ANGLE_X") != -1:
        line = line.replace("old_angle.x", str(camera1_angle_x))
        print(line, file=fw, end='')
        continue

    if line.find("CAMERA1_ANGLE_Y") != -1:
        line = line.replace("old_angle.y", str(camera1_angle_y))
        print(line, file=fw, end='')
        continue

    if line.find("CAMERA1_ANGLE_Z") != -1:
        line = line.replace("old_angle.z", str(camera1_angle_z))
        print(line, file=fw, end='')
        continue

    if line.find("CAMERA1_FOCALLENGTH") != -1:
        line = line.replace("old_focalLength", str(camera1_focalLength))
        print(line, file=fw, end='')
        continue



    if line.find("CAMERA2_POSITION_X") != -1:
        line = line.replace("old_pos.x", str(camera2_pos_x))
        print(line, file=fw, end='')
        continue

    if line.find("CAMERA2_POSITION_Y") != -1:
        line = line.replace("old_pos.y", str(camera2_pos_y))
        print(line, file=fw, end='')
        continue

    if line.find("CAMERA2_POSITION_Z") != -1:
        line = line.replace("old_pos.z", str(camera2_pos_z))
        print(line, file=fw, end='')
        continue

    if line.find("CAMERA2_ANGLE_X") != -1:
        line = line.replace("old_angle.x", str(camera2_angle_x))
        print(line, file=fw, end='')
        continue

    if line.find("CAMERA2_ANGLE_Y") != -1:
        line = line.replace("old_angle.y", str(camera2_angle_y))
        print(line, file=fw, end='')
        continue

    if line.find("CAMERA2_ANGLE_Z") != -1:
        line = line.replace("old_angle.z", str(camera2_angle_z))
        print(line, file=fw, end='')
        continue

    if line.find("CAMERA2_FOCALLENGTH") != -1:
        line = line.replace("old_focalLength", str(camera2_focalLength))
        print(line, file=fw, end='')
        continue



    if line.find("CAMERA3_POSITION_X") != -1:
        line = line.replace("old_pos.x", str(camera3_pos_x))
        print(line, file=fw, end='')
        continue

    if line.find("CAMERA3_POSITION_Y") != -1:
        line = line.replace("old_pos.y", str(camera3_pos_y))
        print(line, file=fw, end='')
        continue

    if line.find("CAMERA3_POSITION_Z") != -1:
        line = line.replace("old_pos.z", str(camera3_pos_z))
        print(line, file=fw, end='')
        continue

    if line.find("CAMERA3_ANGLE_X") != -1:
        line = line.replace("old_angle.x", str(camera3_angle_x))
        print(line, file=fw, end='')
        continue

    if line.find("CAMERA3_ANGLE_Y") != -1:
        line = line.replace("old_angle.y", str(camera3_angle_y))
        print(line, file=fw, end='')
        continue

    if line.find("CAMERA3_ANGLE_Z") != -1:
        line = line.replace("old_angle.z", str(camera3_angle_z))
        print(line, file=fw, end='')
        continue

    if line.find("CAMERA3_FOCALLENGTH") != -1:
        line = line.replace("old_focalLength", str(camera3_focalLength))
        print(line, file=fw, end='')
        continue

    print(line, file=fw, end='')


fr.close()
fw.close()
