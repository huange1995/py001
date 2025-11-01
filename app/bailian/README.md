# 豆包 Seed-1.6-flash 模型调用演示

这个文件夹包含了使用 langchain_openai 调用豆包 Seed-1.6-flash 模型的演示代码。

## 文件说明

- `doubao_demo.py` - 完整的豆包模型调用演示，包含多种使用场景
- `chat_prompt_template_demo.py` - ChatPromptTemplate 详细使用演示，展示6种不同的模板使用方式
- `prompt_template_quick_test.py` - ChatPromptTemplate 快速测试脚本
- `README.md` - 本说明文件

## 使用前准备

### 1. 安装依赖

确保已安装所需的Python包：

```bash
# 如果使用uv（推荐）
uv sync

# 或者使用pip
pip install langchain-openai python-dotenv
```

### 2. 配置环境变量

在项目根目录创建 `.env` 文件，添加以下配置：

```env
# 豆包API配置
DOUBAO_API_KEY=your_doubao_api_key_here
DOUBAO_BASE_URL=https://ark.cn-beijing.volces.com/api/v3
```

**注意**: 
- 请将 `your_doubao_api_key_here` 替换为你的实际API密钥
- 确保你有豆包 Seed-1.6-flash 模型的访问权限

### 3. 获取API密钥

1. 访问豆包开放平台
2. 创建应用并获取API密钥
3. 确保有 Seed-1.6-flash 模型的使用权限

## 运行演示

### ChatPromptTemplate 快速测试

首先运行 ChatPromptTemplate 快速测试来验证配置：

```bash
python app/bailian/prompt_template_quick_test.py
```

### ChatPromptTemplate 详细演示

运行完整的 ChatPromptTemplate 使用演示：

```bash
python app/bailian/chat_prompt_template_demo.py
```

### 完整功能演示

运行完整的豆包模型演示程序：

```bash
python app/bailian/doubao_demo.py
```

## 功能特性

### ChatPromptTemplateDemo 类提供以下演示：

1. **基础模板** (`basic_template_demo`)
   - 使用 `from_messages` 创建简单模板
   - 单变量替换演示

2. **高级模板** (`advanced_template_demo`)
   - 多变量模板使用
   - 复杂场景参数传递

3. **消息模板** (`message_template_demo`)
   - SystemMessagePromptTemplate 使用
   - HumanMessagePromptTemplate 使用
   - 模板组合演示

4. **流式模板** (`streaming_template_demo`)
   - 模板与流式处理结合
   - 实时响应获取

5. **对话模板** (`conversation_template_demo`)
   - 包含上下文的对话模板
   - 多轮对话支持

6. **部分模板** (`partial_template_demo`)
   - 使用 `partial` 预填充变量
   - 模板复用优化

### DoubaoDemo 类提供以下功能：

1. **简单对话** (`simple_chat`)
   - 基础的问答功能
   - 支持中文对话

2. **创意写作** (`creative_writing`)
   - 根据主题生成创意故事
   - 适合内容创作场景

3. **编程助手** (`code_assistant`)
   - 编程问题解答
   - 代码示例生成

4. **批量处理** (`batch_questions`)
   - 批量处理多个问题
   - 适合批量任务场景

## 自定义使用

你可以根据需要修改以下参数：

```python
llm = ChatOpenAI(
    model="ep-20241230140623-qvqzm",  # 模型endpoint ID
    api_key=api_key,
    base_url=base_url,
    temperature=0.7,  # 控制回答的随机性 (0-1)
    max_tokens=1000   # 最大回复长度
)
```

## 常见问题

### Q: 出现认证错误怎么办？
A: 检查 `.env` 文件中的 API 密钥是否正确设置。

### Q: 模型调用失败？
A: 确认网络连接正常，且有模型访问权限。

### Q: 如何修改模型参数？
A: 在初始化 `ChatOpenAI` 时调整 `temperature`、`max_tokens` 等参数。

## 注意事项

- 请妥善保管API密钥，不要提交到版本控制系统
- 注意API调用的费用和限制
- 建议在生产环境中添加适当的错误处理和重试机制