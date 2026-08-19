"""
使用 SDXL 模型生成教学素材图像
无需启动完整的 ComfyUI 服务器
"""
import torch
from diffusers import StableDiffusionXLPipeline, AutoencoderKL
import os

# 设置输出目录
output_dir = "C:/hermesAgent/tiantian-math-game/images"
os.makedirs(output_dir, exist_ok=True)

# 模型路径
model_path = "D:/ComfyUI/models/checkpoints/sd_xl_base_1.0.safetensors"
vae_path = "D:/ComfyUI/models/vae/sdxl_vae.safetensors"

print("正在加载 SDXL 模型...")
print("这可能需要几分钟时间...")

try:
    # 加载 VAE
    vae = AutoencoderKL.from_single_file(
        vae_path,
        torch_dtype=torch.float16
    )
    
    # 加载 SDXL Pipeline
    pipe = StableDiffusionXLPipeline.from_single_file(
        model_path,
        vae=vae,
        torch_dtype=torch.float16,
        use_safetensors=True
    )
    
    # 移动到 GPU
    pipe = pipe.to("cuda")
    
    # 启用内存优化
    pipe.enable_attention_slicing()
    
    print("模型加载完成！")
    
    # 生成教学素材图像
    prompts = [
        {
            "prompt": "cute cartoon little girl with pigtails, bluey style, kawaii, learning math, educational material, bright colors, cheerful, child-friendly, high quality",
            "negative": "ugly, blurry, low quality, distorted, deformed, scary, dark",
            "filename": "tiantian_character.png"
        },
        {
            "prompt": "cute cartoon little girl counting apples, bluey style, kawaii, educational, numbers 1 to 10, colorful, child-friendly illustration",
            "negative": "ugly, blurry, low quality, distorted, deformed, scary, dark, realistic photo",
            "filename": "counting_apples.png"
        },
        {
            "prompt": "cute cartoon animals playing with numbers, bluey style, kawaii, educational math game, bright cheerful colors, child-friendly",
            "negative": "ugly, blurry, low quality, distorted, deformed, scary, dark, realistic",
            "filename": "math_animals.png"
        },
        {
            "prompt": "cartoon classroom with cute characters learning addition, bluey style, kawaii, educational, colorful, happy atmosphere",
            "negative": "ugly, blurry, low quality, distorted, deformed, scary, dark, realistic photo",
            "filename": "classroom.png"
        }
    ]
    
    for i, item in enumerate(prompts):
        print(f"\n生成图像 {i+1}/4: {item['filename']}")
        
        image = pipe(
            prompt=item["prompt"],
            negative_prompt=item["negative"],
            num_inference_steps=30,
            guidance_scale=7.5,
            width=1024,
            height=1024
        ).images[0]
        
        # 保存图像
        output_path = os.path.join(output_dir, item["filename"])
        image.save(output_path)
        print(f"✅ 已保存: {output_path}")
    
    print(f"\n🎉 所有图像生成完成！")
    print(f"输出目录: {output_dir}")
    
except Exception as e:
    print(f"❌ 错误: {str(e)}")
    import traceback
    traceback.print_exc()
