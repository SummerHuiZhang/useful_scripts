
file_path =  '/Users/zhanghui/Desktop/temp/png/';% 需要处理的图像文件夹的路径
img_path_list = dir(strcat(file_path,'*.png'));%获取该文件夹中所有jpg格式的图像
img_num = length(img_path_list);%获取图像总数量
if img_num > 0 %有满足条件的图像
        for j = 1:img_num %逐一读取图像
            image_name = img_path_list(j).name;% 图像名
            image =  imread(strcat(file_path,image_name));
            image = imresize(image,[2000 3000]); %%修改图片尺寸 
            fprintf('%d %d %s\n',i,j,strcat(file_path,image_name));% 显示正在处理的图像名
           imwrite(image,strcat('/Users/zhanghui/Desktop/temp/pngresize/',image_name)); %%保存图片 ，D:\traincar\newzheng\是储存修改图像后的文件夹
        end
end
