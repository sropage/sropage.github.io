input_file = '' #补充文件名  
output_file = 'output.txt' 
with open(input_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()
paragraphs = []
current_paragraph = []
for line in lines:
    if line.strip():  
        current_paragraph.append(line.strip())
    elif current_paragraph:  
        paragraphs.append(' '.join(current_paragraph))
        current_paragraph = []
if current_paragraph:  
    paragraphs.append(' '.join(current_paragraph))

html_content = '<p>' + '</p><p>'.join(paragraphs) + '</p>'

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(html_content)
print(f"已将内容保存到 {output_file}")