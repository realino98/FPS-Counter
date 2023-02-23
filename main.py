import os

def countPercent(source_fps, target_fps):
    percentage = target_fps * 100 / source_fps
    percentage = int(percentage)
    print("Source FPS", source_fps, "\tTarget FPS", target_fps, "\tis", percentage, "%")
    return percentage

os.system("cls")
source = [24, 30, 60, 120]
target = [24, 30]

for trgt in target:
    for src in source:
        countPercent(src, trgt)
    print()