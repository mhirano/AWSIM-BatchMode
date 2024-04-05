import subprocess
import bayes_util

#### 自分の環境に合わせて変更 ↓ここから
awsimProjectRootPath = "/home/mhirano/Documents/Projects/AWSIM" # AWSIMのディレクトリ
unityBinaryPath = "/home/mhirano/Unity/Hub/Editor/2021.1.7f1/Editor/Unity"
#### 自分の環境に合わせて変更 ↑ここまで

for i in range(5):
    height = i

    # Create a unity script that changes camera parameters (position/angle/focalLength)
    bayes_util.GenerateScriptToChangeParameter(
        awsimProjectRootPath,
        camera1_pos_x=225,
        camera1_pos_y=height,
        camera1_pos_z=-255,
        camera1_angle_x=0,
        camera1_angle_y=-60,
        camera1_angle_z=0,
        camera1_focalLength=25,
        camera2_pos_x=170,
        camera2_pos_y=height,
        camera2_pos_z=-235,
        camera2_angle_x=0,
        camera2_angle_y=-240,
        camera2_angle_z=0,
        camera2_focalLength=25,
        camera3_pos_x=200,
        camera3_pos_y=height,
        camera3_pos_z=-260,
        camera3_angle_x=30,
        camera3_angle_y=5,
        camera3_angle_z=0,
        camera3_focalLength=25
        )

    # Build a unity player with the specified camera paraemters
    commandToBuildPlayer = [ 
        unityBinaryPath,
        "-quit",
        "-batchmode",
        "-buildTarget", 
        "Linux64",
        "-executeMethod",
        "BuildPlayer.MyBuild",
        "-projectPath",
        "/home/mhirano/Documents/Projects/AWSIM"
        ]
    subprocess.call(commandToBuildPlayer)

    # Run the built player
    commandToRunPlayer =[
        awsimProjectRootPath+"/Linux/Player"
    ]
    subprocess.call(commandToRunPlayer)

    # Reset script to its original 
    bayes_util.ResetScriptToOriginalParameters(awsimProjectRootPath)
