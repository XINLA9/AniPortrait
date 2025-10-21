import torch, sys, platform, pkg_resources
print(f"🐍 Python: {sys.version.split()[0]}")
print(f"🧱 Platform: {platform.system()} {platform.release()} ({platform.machine()})")
try:
    print(f"🔥 PyTorch: {torch.__version__}")
    print(f"⚡ CUDA (torch): {torch.version.cuda}")
    print(f"🧠 CUDA available: {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        print(f"🎯 GPU: {torch.cuda.get_device_name(0)}")
except Exception as e:
    print("❌ Torch info not available:", e)
# 常见库版本
for lib in ["numpy", "scipy", "opencv-python", "transformers"]:
    try:
        print(f"📦 {lib}: {pkg_resources.get_distribution(lib).version}")
    except pkg_resources.DistributionNotFound:
        print(f"⚠️ {lib} not installed")
