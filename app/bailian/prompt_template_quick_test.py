#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ChatPromptTemplate 快速测试
用于验证 ChatPromptTemplate 基本功能
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

def main():
    """主函数 - ChatPromptTemplate 快速测试"""
    print("🧪 ChatPromptTemplate 快速测试")
    print("="*40)
    
    try:
        # 1. 加载环境变量
        print("1️⃣ 加载环境变量...")
        load_dotenv()
        
        # 2. 检查环境变量
        api_key = os.getenv("DOUBAO_API_KEY")
        base_url = os.getenv("DOUBAO_BASE_URL")
        
        if not api_key:
            print("❌ 错误: 未找到 DOUBAO_API_KEY 环境变量")
            print("请在 .env 文件中设置 DOUBAO_API_KEY")
            return
        
        if not base_url:
            print("❌ 错误: 未找到 DOUBAO_BASE_URL 环境变量")
            print("请在 .env 文件中设置 DOUBAO_BASE_URL")
            return
        
        print("✅ 环境变量检查通过")
        
        # 3. 初始化模型
        print("2️⃣ 初始化豆包模型...")
        llm = ChatOpenAI(
            model="ep-20241230140623-qvqzm",
            api_key=api_key,
            base_url=base_url,
            temperature=0.7,
            max_tokens=500
        )
        print("✅ 模型初始化成功")
        
        # 4. 创建 ChatPromptTemplate
        print("3️⃣ 创建 ChatPromptTemplate...")
        template = ChatPromptTemplate.from_messages([
            ("system", "你是一个有用的AI助手，请简洁地回答问题。"),
            ("human", "请用一句话解释：{topic}")
        ])
        print("✅ 模板创建成功")
        
        # 5. 格式化模板
        print("4️⃣ 格式化模板...")
        messages = template.format_messages(topic="ChatPromptTemplate的作用")
        
        print("📝 格式化后的消息:")
        for i, msg in enumerate(messages, 1):
            print(f"   消息{i} ({msg.type}): {msg.content}")
        
        # 6. 调用模型
        print("5️⃣ 调用模型...")
        response = llm.invoke(messages)
        
        print("🤖 模型回答:")
        print(f"   {response.content}")
        
        print("\n" + "="*40)
        print("✅ ChatPromptTemplate 快速测试完成！")
        print("所有功能正常工作")
        
    except Exception as e:
        print(f"❌ 测试失败: {e}")
        print("请检查:")
        print("1. 网络连接是否正常")
        print("2. API密钥是否正确")
        print("3. 模型访问权限是否有效")

if __name__ == "__main__":
    main()