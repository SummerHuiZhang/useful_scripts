
#-*- coding: UTF-8 -*-  
 
import imageio
 
def create_gif(image_list, gif_name):
 
    frames = []
    for image_name in image_list:
        frames.append(imageio.imread(image_name))
    # Save them as frames into a gif 
    imageio.mimsave(gif_name, frames, 'GIF', duration = 0.5)
 
    return
 
def main():
    image_list = ['1.png', '2.png', '3.png', 
                  '4.png', '5.png', '6.png',
                  '7.png','8.png', '9.png', '10.png', 
                  '11.png', '12.png', '13.png', ]
    gif_name = 'created_gif.gif'
    create_gif(image_list, gif_name)
 
if __name__ == "__main__":
    main()
