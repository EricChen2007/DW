import time
import sys


def show_progress(duration=3):
    # 进度条动画参数 
    total_steps = 20
    step_interval = duration / total_steps

    for i in range(total_steps):
        # 构建动态进度条 
        bar = '[' + '#' * (i + 1) + ' ' * (total_steps - i - 1) + ']'
        percent = (i + 1) * 5
        # 生成动态旋转指针 
        spin = ['-', '\\', '|', '/'][i % 4]
        # 输出组合效果 
        sys.stdout.write(f"\r 处理中 {spin} {bar} {percent}% ")
        sys.stdout.flush()
        time.sleep(step_interval)


while True:
    try:
        user_input = input("\n用户输入：")
        show_progress(2)  # 设置2秒延时 
        print("\n系统回复：服务器繁忙，请稍后再试。")

    except KeyboardInterrupt:
        print("\n\n服务已安全终止")
        break 