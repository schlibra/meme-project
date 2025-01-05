import os
import platform
import shutil
import zipfile


def remake_dir(path, mkdir=True):
    if os.path.exists(path):
        if platform.system() == "Windows":
            os.system(f"rd /s /q {path}")
        else:
            os.system(f"rm -rf {path}")
    if mkdir:
        os.mkdir(path)


def run(command, title):
    print(f"-- {title} --")
    if os.system(command):
        print(f"{title}失败")
        exit(1)
    print(f"{title}成功")


def cd(path):
    os.chdir(path)


def copy(src, tgt):
    shutil.copytree(src, tgt)
    print(f"已复制目录 {src} => {tgt}")


def zip_get_file(input_path, result):
    for file in os.listdir(input_path):
        if os.path.isdir(f"{input_path}/{file}"):
            zip_get_file(f"{input_path}/{file}", result)
        else:
            result.append(f"{input_path}/{file}")


def make_zip(path, zip_name):
    print("开始创建压缩包")
    if os.path.exists(zip_name):
        os.unlink(zip_name)
    file_list = []
    zip_get_file(path, file_list)
    f = zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED)
    for file in file_list:
        f.write(file)
        print(f"添加文件 {file}")
    f.close()
    print("压缩包创建完成")


if __name__ == '__main__':
    backend_targets = [
        "app", "config", "public", "route", "runtime", "vendor"
    ]
    print("--- 开始编译 ---")

    if os.path.isfile("package.zip"):
        os.unlink("package.zip")
    remake_dir("build")
    cd("../frontend")
    run("npm install", "安装前端依赖")
    run("npm run build", "打包前端资源")
    cd("../backend")
    run("composer install", "安装后端依赖")
    run("php think clear", "清理后端运行时文件")
    cd("../deployer")
    for item in backend_targets:
        copy(f"../backend/{item}", f"build/{item}")
    shutil.copy(f"../backend/.env", f"build/.env")
    os.mkdir(f"build/view")
    copy(f"../frontend/dist", f"build/view/dist")
    cd("build")
    make_zip(".", "package.zip")
    os.rename("package.zip", "../package.zip")
    cd("..")
    remake_dir("build", False)
    print("全部执行完成")
