"""
豆包 Seed-1.6-flash 模型调用示例
使用 langchain_openai 库调用豆包大模型
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatMessagePromptTemplate, ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage

# 加载环境变量
load_dotenv()


class DoubaoDemo:
    """豆包模型调用演示类"""
    
    def __init__(self):
        """初始化豆包模型客户端"""
        self.api_key = os.getenv("DOUBAO_API_KEY")
        self.base_url = os.getenv("DOUBAO_BASE_URL")
        
        if not self.api_key:
            raise ValueError("请在.env文件中设置DOUBAO_API_KEY")
        
        # 初始化豆包模型客户端
        self.llm = ChatOpenAI(
            model="ep-20251101172752-8ctss",
            api_key=self.api_key,
            base_url=self.base_url,
            temperature=0.7,
            max_tokens=1000
        )
    
    def simple_chat(self, user_message: str) -> str:
        """简单对话示例"""
        try:
            messages = [
                SystemMessage(content="你是一个友好的AI助手，请用中文回答问题。"),
                HumanMessage(content=user_message)
            ]
            
            response = self.llm.invoke(messages)
            return response.content
        
        except Exception as e:
            return f"调用失败: {str(e)}"
    
    def creative_writing(self, topic: str) -> str:
        """创意写作示例"""
        try:
            messages = [
                SystemMessage(content="你是一个专业的创意写作助手，擅长写故事、诗歌和创意文案。"),
                HumanMessage(content=f"请以'{topic}'为主题，写一个简短的创意故事（200字左右）。")
            ]
            
            response = self.llm.invoke(messages)
            return response.content
        
        except Exception as e:
            return f"创意写作失败: {str(e)}"
            
    def code_assistant(self, question: str, role: str, domain: str) -> str:
        """生成指定角色和领域的回答"""
        try:
            # 构建提示词模板
            chat_prompt = ChatPromptTemplate.from_messages(
                [
                    SystemMessagePromptTemplate.from_template("你是一位{role}专家，擅长回答{domain}领域的问题。请用简洁准确的语言回答。"),
                    HumanMessagePromptTemplate.from_template("用户问题：{question}")
                ]
            )
            
            # 格式化提示词（填充变量）
            formatted_prompt = chat_prompt.format_messages(
                role=role,
                domain=domain,
                question=question
            )
            
            # 流式获取响应并拼接结果
            response_chunks = []
            for chunk in self.llm.stream(formatted_prompt):
                response_chunks.append(chunk.content)
            
            return "".join(response_chunks)
        
        except Exception as e:
            return f"处理失败：{str(e)}"
    
    def batch_questions(self, questions: list) -> dict:
        """批量问题处理示例"""
        results = {}
        
        for i, question in enumerate(questions, 1):
            try:
                messages = [
                    SystemMessage(content="你是一个知识渊博的AI助手，请简洁准确地回答问题。"),
                    HumanMessage(content=question)
                ]
                
                response = self.llm.invoke(messages)
                results[f"问题{i}"] = {
                    "question": question,
                    "answer": response.content
                }
            
            except Exception as e:
                results[f"问题{i}"] = {
                    "question": question,
                    "answer": f"回答失败: {str(e)}"
                }
        
        return results


def main():
    """主函数 - 演示各种功能"""
    print("=== 豆包 Seed-1.6-flash 模型调用演示 ===\n")
    
    try:
        # 初始化豆包客户端
        doubao = DoubaoDemo()
        
        # 1. 简单对话
        # print("1. 简单对话测试:")
        # response = doubao.simple_chat("你好，请介绍一下你自己。")
        # print(f"回答: {response}\n")
        
        # 2. 创意写作
        # print("2. 创意写作测试:")
        # story = doubao.creative_writing("未来城市")
        # print(f"创意故事: {story}\n")
        
        # 3. 编程助手
        print("3. 编程助手测试:")
        code_help = doubao.code_assistant("你吃饭了吗？","技术","Python")
        print(f"编程建议: {code_help}\n")
        
        # 4. 批量问题处理
        # print("4. 批量问题处理测试:")
        # questions = [
        #     "什么是人工智能？",
        #     "Python有哪些优势？",
        #     "如何学习机器学习？"
        # ]
        
        # batch_results = doubao.batch_questions(questions)
        # for key, result in batch_results.items():
        #     print(f"{key}: {result['question']}")
        #     print(f"回答: {result['answer']}\n")
    
    except Exception as e:
        print(f"演示过程中出现错误: {str(e)}")
        print("请检查:")
        print("1. 是否正确设置了.env文件中的API密钥")
        print("2. 网络连接是否正常")
        print("3. API配置是否正确")


if __name__ == "__main__":
    main()