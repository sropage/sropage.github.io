import os
import re

def remove_string_from_files(root_dir, target_string):
    # 编译正则表达式以提高性能
    pattern = re.compile(re.escape(target_string))
    
    # 遍历所有目录和子目录
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            # 跳过.py后缀的文件
            if filename.endswith('.py'):
                continue
                
            file_path = os.path.join(dirpath, filename)
            
            try:
                # 读取文件内容
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                
                # 检查是否需要替换
                if pattern.search(content):
                    # 执行替换
                    new_content = pattern.sub('', content)
                    
                    # 只有内容确实改变了才写入文件
                    if new_content != content:
                        with open(file_path, 'w', encoding='utf-8') as file:
                            file.write(new_content)
                        print(f'已处理文件: {file_path}')
            except (UnicodeDecodeError, PermissionError, IOError) as e:
                # 跳过二进制文件或无权限文件等
                print(f'跳过文件 {file_path}，原因: {str(e)}')
                continue

if __name__ == '__main__':
    # 获取脚本所在目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 要删除的目标字符串
    target_string = '<a href="../callus.html">联系我们</a>'
    
    print(f'开始在目录 {script_dir} 及其子目录中处理文件...')
    print('注意：将跳过所有.py后缀的文件')
    remove_string_from_files(script_dir, target_string)
    print('处理完成！')