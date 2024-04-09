from pathlib import Path
import shutil

def GenerateScriptToSetExportDirectory(projectRootPath, new_name: str):
    template_path=Path('ScreenshotHandler_template.cs')
    script_path=projectRootPath / Path('Assets/AWSIM/Scripts/ScreenshotHandler.cs')

    # テンプレートを1行ずつ読み込み、編集後のスクリプトを保存
    fr = open(str(template_path),'r')
    fw = open(str(script_path), 'w')
    while True:
        line = fr.readline()

        # テンプレートを全て読み終えたら終了
        if line == '':
            break

        # Export directoryを設定
        if line.find("RENDERING_EXPORT_DIRECTORY") != -1:
            line = line.replace("DEFAULT_DIRECTORY", new_name)
            print(line, file=fw, end='')
            continue

        print(line, file=fw, end='')


    fr.close()
    fw.close()




# テンプレートからカメラパラメータ変更スクリプト(ChangeCameraParameters.cs)を生成
def GenerateScriptToChangeParameter(projectRootPath, **kwargs):

    # 関数に渡される引数を解析し、変更後のパラメータを変数として保存
    # カメラを追加したり、他のパラメータを変更したい場合はここに追加
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
    
    # C#スクリプトのテンプレートを指定
    # position, angle, focalLengthあたりを編集可能にしていますが、
    # 他のパラメータも変更したい場合は、適宜追加してください。
    template_path=Path('ChangeCameraParameters_template.cs') 
    
    # GameObjectにアタッチされるC#スクリプトのパス
    script_path=projectRootPath / Path('Assets/AWSIM/Scripts/ChangeCameraParameters.cs')

    # テンプレートを1行ずつ読み込み、編集後のスクリプトを保存
    fr = open(str(template_path),'r')
    fw = open(str(script_path), 'w')
    while True:
        line = fr.readline()

        # テンプレートを全て読み終えたら終了
        if line == '':
            break

        # 以下でテンプレートを1行ずつチェックして/** KEYWORD **/を探しだし、
        # 文字列をreplaceしてスクリプトに出力していく
        # 上部の引数解析と同様に、カメラを追加したり他のカメラパラメータを変更したい場合は、ここに追記してください。
        
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


# カメラパラメータ変更スクリプト(ChangeCameraParameters.cs)をデフォルトに復元
def ResetScripts(projectRootPath):

    template_path=Path('ChangeCameraParameters_template.cs')
    script_path=projectRootPath / Path('Assets/AWSIM/Scripts/ChangeCameraParameters.cs')

    shutil.copy(template_path, script_path);

    template_path=Path('ScreenshotHandler_template.cs')
    script_path=projectRootPath / Path('Assets/AWSIM/Scripts/ScreenshotHandler.cs')

    shutil.copy(template_path, script_path);

