import json
from openai import OpenAI

# 实例化 OpenAI 客户端
client = OpenAI(
    api_key="请自行替换。",  # 替换为你的实际 API 密钥
    base_url="请自行替换。"  # 如果有自定义 URL
)

# 加载 JSON 文件
with open("T.txt", "r", encoding="utf-8") as file:
    data = json.load(file)

# 提取编程题目
questions = data["exercise_question_types"][0]["items"]

# 保存结果到 Markdown 文件
with open("solutions.md", "w", encoding="utf-8") as output_file:
    # 添加文件标题
    output_file.write("# 编程题目解答\n\n")

    for question in questions:
        # 提取题目信息
        question_num = question["question_num"]
        question_title = question["question_title"]
        question_description = question["description"]

        # 打印当前处理的题目
        print(f"正在处理题目编号: {question_num} - {question_title}")

        # 调用 ChatGPT 生成答案
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "你是一个专业的编程助手，帮助解决编程问题。"},
                    {"role": "user", "content": f"题目描述：{question_description}\n\n请使用 C 语言解决这个问题，并提供完整的代码实现。"}
                ]
            )
            # 获取 ChatGPT 的回复
            answer = response.choices[0].message.content
        except Exception as e:
            answer = f"ChatGPT 请求失败: {str(e)}"

        # 将题目和答案写入 Markdown 文件
        output_file.write(f"## 题目 {question_num}: {question_title}\n\n")
        output_file.write(f"**题目描述：**\n\n{question_description.replace('\n', '  \n')}\n\n")
        output_file.write(f"**ChatGPT 解答：**\n\n```c\n{answer}\n```\n\n")
        output_file.write("---\n\n")  # 添加分隔线

        # 打印完成信息
        print(f"题目编号 {question_num} 已处理完成！\n")

print("所有题目已处理完成，结果保存在 solutions.md 文件中。")