import cv2
import numpy as np

def resize(img_dir, out_dir='out.png', x = 1000, y = 600):
    try:
        img = cv2.imread(img_dir)
        h, w, c = img.shape
        ratio = h/w

        if h/w < y/x:
            #height is less than the ratio
            res = cv2.resize(img, (x, int(h*(x/w))), interpolation = cv2.INTER_CUBIC)
            res = cv2.copyMakeBorder(res, (y-int(h*(x/w)))//2, (y-int(h*(x/w)))//2, 0, 0, borderType=cv2.BORDER_CONSTANT, value=None)

        else:
            #width is less than the ratio
            res = cv2.resize(img, (int(w*(y/h)), y), interpolation = cv2.INTER_CUBIC)
            res = cv2.copyMakeBorder(res, 0, 0, (x-int(w*(y/h)))//2, (x-int(w*(y/h)))//2, borderType=cv2.BORDER_CONSTANT, value=None)

        h, w, c = res.shape

        cv2.imwrite(out_dir, res)
    except:
        print('error resizing')
        return None

def main(args):
    out_dir = 'out.png'
    x = 1000
    y = 600

    args, opts = getargs(args)
    directory = args[1]
    if len(args) > 2:
        pics = args[1:]
    else:
        print('bad args')
        return None

    if opts.get('-x'):
        x = int(opts.get('-x'))
    
    if opts.get('-y'):
        y = int(opts.get('-y'))

    if pics:
        import os
        if not os.path.exists(pics[0][:pics[0].rfind('/')]+'/out'):
            os.mkdir(pics[0][:pics[0].rfind('/')]+'/out')
        for i in pics:
            if i[-3:] in set(['png', 'jpg', 'peg']):
                resize(i, x=x, y=y, out_dir=i[:i.rfind('/')]+'/out/'+i[i.rfind('/')+1:])

    else:
        resize(directory, x=x, y=y, out_dir='out.png')


    print('done!')

    
def getargs(argv):
    opts = {}
    args = []
    while argv: 
        if argv[0][0] == '-':
            opts[argv[0]] = argv[1]
            argv = argv[2:]

        else:
            args.append(argv[0])
            argv = argv[1:]

    return args, opts

if __name__ == '__main__':
    import sys
    main(sys.argv)


