import cv2
import os

DIR=''

def glue(prefix='0001',project='GANINVERSION',out_dir='/home/ubuntu/workspace/results/gan-inversion'):

    images = []
    if project =='GANINVERSION':
        dir = '/home/ubuntu/workspace/gan-inversion/bear13/logs/images/test/faces'
        files = [os.path.join(dir,f) for f in sorted(os.listdir(dir)) if f.startswith(prefix)]
        files = files[::2]
        img_init = cv2.imread(files[0])
        images.append(img_init[:,:300,:])
        crop_size = 550
        for pth in files:
            img = cv2.imread(pth)
            # crop first
            img = img[:,crop_size:,:]
            images.append(img)

        res = cv2.hconcat(images)
        cv2.imwrite(os.path.join(out_dir,'%s.png'%prefix),res)


if __name__ == "__main__":
    for i in range(220):
        prefix = str(i).zfill(4)
        glue(prefix=prefix)