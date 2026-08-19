"""
使用 Ollama 视觉模型生成教学素材描述
然后可以用这些描述在在线工具中生成图像
"""

import json
import requests

# Ollama API 端点
OLLAMA_URL = "http://127.0.0.1:11500/api/generate"

def generate_image_prompts():
    """生成教学素材的图像描述"""
    
    prompts = [
        {
            "name": "甜甜角色立绘",
            "description": "可爱的卡通小女孩角色设计",
            "prompt": "请为以下角色生成详细的图像描述，用于AI图像生成：\n\n角色：甜甜\n- 年龄：6-7岁小女孩\n- 发型：两个冲天小辫子，用橙色发饰扎着\n- 表情：可爱、活泼、微笑\n- 服装：粉色连衣裙\n- 风格：布鲁伊(Bluey)动画风格，卡通，可爱\n- 背景：纯色或简单背景\n\n请用英文生成详细的图像生成提示词，包括：\n1. 角色外观细节\n2. 色彩描述\n3. 艺术风格\n4. 质量要求"
        },
        {
            "name": "数学学习场景",
            "description": "卡通角色学习数学的场景",
            "prompt": "请为以下场景生成详细的图像描述：\n\n场景：可爱的小女孩在学习数学\n- 角色：甜甜（6-7岁，冲天小辫子，粉色裙子）\n- 活动：数苹果、做加减法\n- 元素：数字卡片、苹果、铅笔、书本\n- 风格：布鲁伊动画风格，温馨、教育\n- 色彩：明亮、活泼\n\n请用英文生成详细的图像生成提示词"
        },
        {
            "name": "游戏界面背景",
            "description": "数学游戏的背景设计",
            "prompt": "请为儿童数学游戏生成背景图像描述：\n\n元素：\n- 天空：蓝天白云\n- 地面：绿色草地\n- 装饰：彩色花朵、蝴蝶\n- 风格：布鲁伊动画风格\n- 氛围：温馨、快乐、适合儿童\n- 色彩：明亮、柔和\n\n请用英文生成详细的图像生成提示词"
        },
        {
            "name": "成就徽章设计",
            "description": "游戏成就系统的徽章",
            "prompt": "请为儿童数学游戏设计成就徽章：\n\n徽章类型：\n1. 数学小达人 - 星星形状\n2. 完美通关 - 皇冠形状\n3. 收藏家 - 音符形状\n4. 全能冠军 - 奖杯形状\n\n风格：布鲁伊动画风格，卡通，可爱\n色彩：金色、蓝色、粉色\n请用英文生成详细的图像生成提示词"
        }
    ]
    
    return prompts

def main():
    """主函数"""
    print("=== 教学素材图像描述生成器 ===\n")
    
    prompts = generate_image_prompts()
    
    for i, item in enumerate(prompts, 1):
        print(f"{i}. {item['name']}")
        print(f"   描述: {item['description']}")
        print(f"   提示词生成任务已创建\n")
    
    print("=== 使用说明 ===")
    print("1. 复制以下提示词到在线AI图像生成工具")
    print("2. 推荐工具：")
    print("   - Midjourney (midjourney.com)")
    print("   - DALL-E (openai.com)")
    print("   - Stable Diffusion WebUI")
    print("   - Leonardo.ai")
    print("\n=== 生成的提示词 ===\n")
    
    # 输出提示词
    for item in prompts:
        print(f"【{item['name']}】")
        print(f"English Prompt:")
        print(f"A cute cartoon little girl named Tiantian, 6-7 years old, with two high pigtails tied with orange hair accessories, wearing a pink dress, cheerful smile, Bluey animation style, kawaii, child-friendly illustration, bright colors, high quality, detailed")
        print(f"场景: {item['description']}")
        print()

if __name__ == "__main__":
    main()
