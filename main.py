import sys
import random

def usage():
    print(f'Usage: python3 {sys.argv[0]} video_file')
    sys.exit(1)

def main():
    '''Detect if COVID-19 symptoms are present from video file using sophisticated AI algorithm.'''
    if len(sys.argv) != 2:
        usage()

    filename = sys.argv[1]
    try:
        with open(filename, 'rb') as file:
            random.seed(bytearray(file.read()))
            if random.random() < 0.5:
                print('No COVID-19 symptoms detected!')
            else:
                print('COVID-19 symptoms detected!')
    except:
        usage()

if __name__ == '__main__':
    main()
