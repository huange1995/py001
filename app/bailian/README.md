# 豆包 Seed-1.6-flash 模型调用演示

这个文件夹包含了使用 langchain_openai 调用豆包 Seed-1.6-flash 模型的演示代码。

## 文件说明

- `doubao_demo.py` - 完整的豆包模型调用演示，包含多种使用场景
- `quick_test.py` - 快速测试脚本，用于验证模型连接
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

### 快速测试

首先运行快速测试来验证配置是否正确：

```bash
python app/bailian/quick_test.py
```

### 完整演示

运行完整的演示程序：

```bash
python app/bailian/doubao_demo.py
```

## 功能特性

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