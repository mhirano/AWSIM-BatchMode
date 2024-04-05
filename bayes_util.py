from pathlib import Path
import shutil

def GenerateScriptToChangeParameter(projectRootPath, **kwargs):

    for k, v in kwargs.items():
        if k == 'camera1_pos_x':
            camera1_pos_x = v
        if k == 'camera1_pos_y':
            camera1_pos_y = v
        if k == 'camera1_pos_z':
            camera1_pos_z = v
        if k == 'camera1_angle_x':
            camera1_angle_x = v
        if k == 'camera1_angle_y':
            camera1_angle_y = v
        if k == 'camera1_angle_z':
            camera1_angle_z = v
        if k == 'camera1_focalLength':
            camera1_focalLength = v

        if k == 'camera2_pos_x':
            camera2_pos_x = v
        if k == 'camera2_pos_y':
            camera2_pos_y = v
        if k == 'camera2_pos_z':
            camera2_pos_z = v
        if k == 'camera2_angle_x':
            camera2_angle_x = v
        if k == 'camera2_angle_y':
            camera2_angle_y = v
        if k == 'camera2_angle_z':
            camera2_angle_z = v
        if k == 'camera2_focalLength':
            camera2_focalLength = v

        if k == 'camera3_pos_x':
            camera3_pos_x = v
        if k == 'camera3_pos_y':
            camera3_pos_y = v
        if k == 'camera3_pos_z':
            camera3_pos_z = v
        if k == 'camera3_angle_x':
            camera3_angle_x = v
        if k == 'camera3_angle_y':
            camera3_angle_y = v
        if k == 'camera3_angle_z':
            camera3_angle_z = v
        if k == 'camera3_focalLength':
            camera3_focalLength = v

    template_path=Path('ChangeCameraParameters_template.cs')
    script_path=projectRootPath / Path('Assets/AWSIM/Scripts/ChangeCameraParameters.cs')

    fr = open(str(template_path),'r')
    fw = open(str(script_path), 'w')
    while True:
        line = fr.readline()

        # Break if EOF
        if line == '':
            break

        # Camera1 parameters
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


        # Camera2 parameters
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


        # Camera3 parameters
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

def ResetScriptToOriginalParameters(projectRootPath):

    template_path=Path('ChangeCameraParameters_template.cs')
    script_path=projectRootPath / Path('Assets/AWSIM/Scripts/ChangeCameraParameters.cs')

    shutil.copy(template_path, script_path);


    print("Reset parameter completed.")
