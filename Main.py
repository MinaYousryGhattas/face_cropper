import sys
import os
import face_croper
# run example python Main.py 'inputpath' 'outputpath'
def main():
    print(sys.argv)
    assert len(sys.argv) == 3, 'input path and outpath must be defined'
    files = os.listdir(sys.argv[1])
    counter = 1
    for file in files:
        counter += 1
        face_croper.face_cropper(sys.argv[1]+'\\'+file,sys.argv[2],counter)

if __name__ == '__main__':
    main()



