import os

def add_paragraph_tags():
    # 获取脚本所在目录的路径
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 构建输入和输出文件的完整路径
    input_file = os.path.join(script_dir, 'input.txt')
    output_file = os.path.join(script_dir, 'output.txt')
    
    try:
        # 读取输入文件
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # 为每行非空文本添加<p>标签
        tagged_lines = []
        for line in lines:
            stripped_line = line.strip()
            if stripped_line:  # 只处理非空行
                tagged_line = f"<p>{stripped_line}</p>"
                tagged_lines.append(tagged_line)
        
        # 将处理后的行连接起来
        result = '\n'.join(tagged_lines)
        
        # 写入输出文件
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(result)
        
        print("处理完成！结果已保存到 output.txt")
        print(f"共处理了 {len(tagged_lines)} 行文本")
        
    except FileNotFoundError:
        print("错误：找不到 input.txt 文件")
    except Exception as e:
        print(f"处理过程中发生错误：{str(e)}")

if __name__ == "__main__":
    add_paragraph_tags()