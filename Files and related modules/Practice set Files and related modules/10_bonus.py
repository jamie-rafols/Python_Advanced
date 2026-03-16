with open(r".\Files and related modules\Practice set Files and related modules\tasks.txt", "r") as f:
    content = (f.read())
    
with open(r".\Files and related modules\Practice set Files and related modules\output.txt", "w") as f:
    f.write(content.upper())
