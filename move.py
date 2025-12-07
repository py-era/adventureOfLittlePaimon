import os

def create_folders():
    # 指定目录路径
    base_dir = "./img"
    
    # 如果img目录不存在，则创建它
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
        print(f"创建目录: {base_dir}")
    
    # 循环创建0-161的文件夹
    for i in range(162):  # 0到161，共162个
        folder_name = str(i)
        folder_path = os.path.join(base_dir, folder_name)
        
        # 检查文件夹是否已存在
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"创建文件夹: {folder_path}")
        else:
            print(f"文件夹已存在，跳过: {folder_path}")

if __name__ == "__main__":
    create_folders()
    print("完成！")