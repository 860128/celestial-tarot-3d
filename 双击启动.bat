@echo off
title 3D 虚幻塔罗牌 (Ethereal 3D Tarot)
chcp 65001 >nul
cd /d "%~dp0"

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [提示] 未检测到 Python 环境，正在尝试直接用默认浏览器打开网页...
    start "" "index.html"
    pause
    exit /b 0
)

echo 正在启动 3D 塔罗牌本地服务...
python server.py
pause
