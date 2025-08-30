import os
import re

def replace_email_in_html_files():
    # 获取脚本所在目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 要查找和替换的邮箱地址
    old_email = "sroclaude@outlook.com"
    new_email = "sroniko@outlook.com"
    
    # 计数器
    files_processed = 0
    replacements_made = 0
    
    # 遍历所有目录和子目录
    for root, dirs, files in os.walk(script_dir):
        for file in files:
            # 检查文件是否为HTML文件
            if file.lower().endswith(('.html', '.htm')):
                file_path = os.path.join(root, file)
                
                try:
                    # 读取文件内容
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # 检查是否包含旧邮箱地址
                    if old_email in content:
                        # 替换邮箱地址
                        new_content = content.replace(old_email, new_email)
                        
                        # 写回文件
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        
                        # 统计替换次数
                        count = content.count(old_email)
                        replacements_made += count
                        print(f"在文件 {file_path} 中进行了 {count} 次替换")
                    
                    files_processed += 1
                    
                except Exception as e:
                    print(f"处理文件 {file_path} 时出错: {str(e)}")
    
    # 输出结果摘要
    print(f"\n处理完成!")
    print(f"已扫描 {files_processed} 个HTML文件")
    print(f"共进行了 {replacements_made} 次替换")

if __name__ == "__main__":
    replace_email_in_html_files()