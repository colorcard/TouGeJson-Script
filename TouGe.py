import json

# 打开JSON文件
with open("T.txt", "r", encoding="utf-8") as file:
    data = json.load(file)

# 提取编程题的题目内容
questions = data["exercise_question_types"][0]["items"]

# 保存到 Markdown 文件
with open("questions.md", "w", encoding="utf-8") as output_file:
    # 添加文件的总体标题
    output_file.write("# 题目列表\n\n")

    for question in questions:
        # 添加题目编号和标题作为二级标题
        output_file.write(f"## 题目 {question['question_num']}: {question['question_title']}\n\n")

        # 将题目描述处理为 Markdown 换行格式
        description = question["description"].replace("\n", "  \n")
        output_file.write(f"**题目描述：**\n\n{description}\n\n")

        # 添加分隔线
        output_file.write("---\n\n")

print("解析完成！题目信息已保存到 questions.md 文件中。")