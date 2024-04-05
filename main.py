import subprocess
import util

#### 自分の環境に合わせて変更 ↓ここから
awsimProjectRootPath = "/home/mhirano/Documents/Projects/AWSIM" # AWSIMのディレクトリ
unityBinaryPath = "/home/mhirano/Unity/Hub/Editor/2021.1.7f1/Editor/Unity"
#### 自分の環境に合わせて変更 ↑ここまで

for i in range(5):
    # In this example, camera height is the only variable changed during the loop.
    height = i

    # Create a unity script that changes camera parameters (position/angle/focalLength)
    # You need to specify all the parameters.
    print("Generating camera parameter script...")
    util.GenerateScriptToChangeParameter(
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
    print("Done.")

    # Build a player with the specified camera paraemters
    # ref: https://docs.unity3d.com/ja/2018.4/Manual/CommandLineArguments.html
    print("Building player...")
    commandToBuildPlayer = [ 
        unityBinaryPath,
        "-quit",
        # "-batchmode",
        "-buildTarget", 
        "Linux64",
        "-executeMethod",
        "BuildPlayer.MyBuild",
        "-projectPath",
        awsimProjectRootPath
        ]
    subprocess.call(commandToBuildPlayer)
    print("Done.")

    # Run the built player
    print("Running player...")
    commandToRunPlayer =[
        awsimProjectRootPath+"/Linux/Player"
    ]
    subprocess.call(commandToRunPlayer)
    print("Done.")

    # Reset script to its original contents
    print("Resetting camera parameter script...")
    util.ResetScriptToOriginalParameters(awsimProjectRootPath)
    print("Done.")




