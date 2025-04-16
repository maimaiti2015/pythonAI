
from openai import OpenAI
import requests

client = OpenAI(api_key="sk-2315051b87af4eef8a20d948c0ba874d", base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "你是一个乐于助人的助手"},
        {"role": "user", "content": "一般腋下手术伤口的愈合周期是多少时间？"},
    ],
    stream=True
)

full_response = []
for chunk in response:  # 遍历流式响应的每个块
    if chunk.choices:  # 检查块中是否有有效数据
        content = chunk.choices[0].delta.content  # 获取增量内容
        if content is not None:
            full_response.append(content)
            print(content, end="", flush=True)  # 实时逐字输出

# 合并完整结果
final_answer = "".join(full_response)
print("\n最终结果:", final_answer)


