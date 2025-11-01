#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ChatPromptTemplate 使用演示
展示各种 ChatPromptTemplate 的使用方式
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import (
    ChatPromptTemplate, 
    SystemMessagePromptTemplate, 
    HumanMessagePromptTemplate
)
from langchain_core.messages import SystemMessage, HumanMessage

class ChatPromptTemplateDemo:
    """ChatPromptTemplate 使用演示类"""
    
    def __init__(self):
        """初始化演示类"""
        # 加载环境变量
        load_dotenv()
        
        # 获取API配置
        api_key = os.getenv("DOUBAO_API_KEY")
        base_url = os.getenv("DOUBAO_BASE_URL")
        
        if not api_key or not base_url:
            raise ValueError("请在 .env 文件中设置 DOUBAO_API_KEY 和 DOUBAO_BASE_URL")
        
        # 初始化模型
        self.llm = ChatOpenAI(
            model="ep-20241230140623-qvqzm",
            api_key=api_key,
            base_url=base_url,
            temperature=0.7
        )
        
        print("✅ ChatPromptTemplate 演示初始化成功")
    
    def basic_template_demo(self):
        """1. 基础模板演示"""
        print("\n" + "="*50)
        print("1. 基础模板演示")
        print("="*50)
        
        # 创建基础模板
        template = ChatPromptTemplate.from_messages([
            ("system", "你是一个有用的AI助手。"),
            ("human", "请回答这个问题：{question}")
        ])
        
        # 格式化模板
        messages = template.format_messages(question="什么是人工智能？")
        print("📝 格式化后的消息:")
        for msg in messages:
            print(f"  {msg.type}: {msg.content}")
        
        # 调用模型
        print("\n🤖 模型回答:")
        response = self.llm.invoke(messages)
        print(response.content)
    
    def advanced_template_demo(self):
        """2. 高级模板演示 - 多变量"""
        print("\n" + "="*50)
        print("2. 高级模板演示 - 多变量")
        print("="*50)
        
        # 创建多变量模板
        template = ChatPromptTemplate.from_messages([
            ("system", "你是一个{role}，专门帮助用户{task}。"),
            ("human", "关于{topic}，请用{style}的方式来{action}。")
        ])
        
        # 格式化模板
        messages = template.format_messages(
            role="编程导师",
            task="学习编程",
            topic="Python函数",
            style="简单易懂",
            action="解释"
        )
        
        print("📝 格式化后的消息:")
        for msg in messages:
            print(f"  {msg.type}: {msg.content}")
        
        # 调用模型
        print("\n🤖 模型回答:")
        response = self.llm.invoke(messages)
        print(response.content)
    
    def message_template_demo(self):
        """3. 消息模板演示"""
        print("\n" + "="*50)
        print("3. 消息模板演示")
        print("="*50)
        
        # 使用 SystemMessagePromptTemplate 和 HumanMessagePromptTemplate
        system_template = SystemMessagePromptTemplate.from_template(
            "你是一个{expertise}专家，请用{tone}的语气回答问题。"
        )
        
        human_template = HumanMessagePromptTemplate.from_template(
            "请解释一下{concept}的概念，并给出一个{example_type}的例子。"
        )
        
        # 组合模板
        chat_template = ChatPromptTemplate.from_messages([
            system_template,
            human_template
        ])
        
        # 格式化模板
        messages = chat_template.format_messages(
            expertise="机器学习",
            tone="专业但友好",
            concept="神经网络",
            example_type="实际应用"
        )
        
        print("📝 格式化后的消息:")
        for msg in messages:
            print(f"  {msg.type}: {msg.content}")
        
        # 调用模型
        print("\n🤖 模型回答:")
        response = self.llm.invoke(messages)
        print(response.content)
    
    def streaming_template_demo(self):
        """4. 流式模板演示"""
        print("\n" + "="*50)
        print("4. 流式模板演示")
        print("="*50)
        
        # 创建模板
        template = ChatPromptTemplate.from_messages([
            ("system", "你是一个创意写作助手。"),
            ("human", "请写一个关于{theme}的{length}故事。")
        ])
        
        # 格式化模板
        messages = template.format_messages(
            theme="未来科技",
            length="短篇"
        )
        
        print("📝 使用流式处理获取回答:")
        print("🤖 模型回答:")
        
        # 流式调用
        for chunk in self.llm.stream(messages):
            print(chunk.content, end="", flush=True)
        print("\n")
    
    def conversation_template_demo(self):
        """5. 对话模板演示"""
        print("\n" + "="*50)
        print("5. 对话模板演示")
        print("="*50)
        
        # 创建包含上下文的对话模板
        template = ChatPromptTemplate.from_messages([
            ("system", "你是一个{character}，请保持角色一致性。"),
            ("human", "{previous_context}"),
            ("assistant", "{previous_response}"),
            ("human", "{current_question}")
        ])
        
        # 格式化模板
        messages = template.format_messages(
            character="友善的图书管理员",
            previous_context="我想找一些关于历史的书籍。",
            previous_response="我推荐您看看《人类简史》，这是一本很好的历史入门书籍。",
            current_question="除了这本书，还有其他类似的推荐吗？"
        )
        
        print("📝 格式化后的对话:")
        for msg in messages:
            print(f"  {msg.type}: {msg.content}")
        
        # 调用模型
        print("\n🤖 模型回答:")
        response = self.llm.invoke(messages)
        print(response.content)
    
    def partial_template_demo(self):
        """6. 部分模板演示"""
        print("\n" + "="*50)
        print("6. 部分模板演示")
        print("="*50)
        
        # 创建模板
        template = ChatPromptTemplate.from_messages([
            ("system", "你是一个{role}，专门处理{domain}相关的问题。"),
            ("human", "请帮我{task}：{content}")
        ])
        
        # 使用 partial 预填充一些变量
        partial_template = template.partial(
            role="技术顾问",
            domain="软件开发"
        )
        
        print("📝 使用部分模板，预填充了 role 和 domain")
        
        # 只需要提供剩余的变量
        messages = partial_template.format_messages(
            task="代码审查",
            content="这段Python代码的性能如何优化？"
        )
        
        print("📝 格式化后的消息:")
        for msg in messages:
            print(f"  {msg.type}: {msg.content}")
        
        # 调用模型
        print("\n🤖 模型回答:")
        response = self.llm.invoke(messages)
        print(response.content)

def main():
    """主函数"""
    try:
        # 创建演示实例
        demo = ChatPromptTemplateDemo()
        
        print("🚀 开始 ChatPromptTemplate 演示")
        print("本演示将展示 6 种不同的 ChatPromptTemplate 使用方式")
        
        # 运行所有演示
        demo.basic_template_demo()
        demo.advanced_template_demo()
        demo.message_template_demo()
        demo.streaming_template_demo()
        demo.conversation_template_demo()
        demo.partial_template_demo()
        
        print("\n" + "="*50)
        print("✅ 所有演示完成！")
        print("="*50)
        
    except Exception as e:
        print(f"❌ 演示过程中出现错误: {e}")

if __name__ == "__main__":
    main()