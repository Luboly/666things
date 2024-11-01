import json

# 假设您的文档路径是 '666件可写的事.txt'
document_path = '666件可写的事.txt'
output_path = 'output.json'

# 读取文档内容
with open(document_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 转换为 JSON 格式
json_prompts = []
for i, line in enumerate(lines, start=1):
    # 去除每行的首尾空白字符（包括换行符）
    prompt = line.strip()
    # 创建 JSON 对象
    json_prompt = {"id": i, "prompt": prompt}
    json_prompts.append(json_prompt)

# 将 JSON 对象写入文件
with open(output_path, 'w', encoding='utf-8') as output_file:
    json.dump(json_prompts, output_file, ensure_ascii=False, indent=4)

print(f'JSON 文件已保存至：{output_path}')