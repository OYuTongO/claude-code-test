# Terminal Infiltrator - 完整攻略

本攻略包含所有关卡的完整解答。如果你想自己解谜，请不要提前查看！

## 第一关：入侵开始 - 废弃的服务器

### 目标
访问主数据库

### 完整流程

1. **开始探索**
   ```
   scan
   ```
   查看所有可用文件和目标

2. **阅读 welcome.txt**
   ```
   read welcome.txt
   ```
   了解系统基本信息

3. **解密 note.txt**
   ```
   decrypt note.txt
   ```
   - 问题：100 + 200 - 50 = ?
   - 答案：`250`

4. **阅读解密后的内容**
   文件中提示：密码是"2024年的前4位数字"

5. **访问数据库**
   ```
   execute access database 2024
   ```

6. **完成关卡**
   查看数据库内容，进入第二关

---

## 第二关：深入 - NEXUS-7 服务器

### 目标
访问 AI 核心系统

### 完整流程

1. **扫描系统**
   ```
   scan
   ```

2. **查看系统日志**
   ```
   read system.log
   ```
   注意：日志中提到 "KEY-ALPHA-7"

3. **解密防火墙配置**
   ```
   decrypt firewall_config.enc
   ```
   - 问题：逻辑推理题（三个开关）
   - 分析：
     - A说自己是错的（矛盾）
     - B说C是对的
     - C说A是对的
     - 如果A对，则"A是错的"为真，矛盾
     - 如果C对，则A对，导致矛盾
     - 因此B对
   - 答案：`B`

4. **查看防火墙配置**
   文件显示 ai_core 的密码是 ALPHA-7

5. **（可选）解密秘密备忘录**
   ```
   decrypt secret_memo.enc
   ```
   - 问题：凯撒密码，KHOOR 偏移量3
   - 答案：`HELLO`
   - 了解更多背景故事

6. **访问 AI 核心**
   ```
   execute access ai_core ALPHA-7
   ```

7. **完成关卡**
   进入第三关

---

## 第三关：真相 - OMEGA 区域

### 目标
做出最终选择

### 完整流程

1. **阅读 README**
   ```
   read README.txt
   ```

2. **解密举报人日志**
   ```
   decrypt whistleblower.enc
   ```
   - 问题：数列 2, 4, 8, 16, 32, ?
   - 规律：每次乘以2
   - 答案：`64`

3. **查看后门信息**
   获得访问码：FREEDOM

4. **解密项目真相**
   ```
   decrypt project_truth.enc
   ```
   - 问题：哲学问题（监控 vs 隐私）
   - 提示：举报人的选择
   - 答案：`NO`

5. **访问主控制台**
   ```
   execute access main_console FREEDOM
   ```

6. **做出选择**

   **选项1：关闭系统（沉默结局）**
   ```
   execute shutdown_system
   ```
   - 结果：永久删除所有数据
   - 特点：没人知道真相
   - 主题：保护世界，代价是隐瞒

   **选项2：公开证据（真相结局）**
   ```
   execute leak_evidence
   ```
   - 结果：向全世界公开
   - 特点：真相大白
   - 主题：揭露真相，无论代价

7. **游戏结束**

---

## 所有谜题答案速查

| 关卡 | 文件 | 问题 | 答案 |
|------|------|------|------|
| 1 | note.txt | 100+200-50=? | 250 |
| 2 | firewall_config.enc | 逻辑推理（三个开关） | B |
| 2 | secret_memo.enc | 凯撒密码 KHOOR | HELLO |
| 3 | whistleblower.enc | 数列 2,4,8,16,32,? | 64 |
| 3 | project_truth.enc | 监控系统应该存在吗 | NO |

---

## 关键命令序列

### 第一关最快通关
```
scan
decrypt note.txt
250
execute access database 2024
```

### 第二关最快通关
```
read system.log
decrypt firewall_config.enc
B
execute access ai_core ALPHA-7
```

### 第三关（真相结局）
```
decrypt whistleblower.enc
64
decrypt project_truth.enc
NO
execute access main_console FREEDOM
execute leak_evidence
```

---

## 游戏彩蛋和隐藏内容

1. **多次使用错误答案**
   在解密时多次输入错误答案，虽然会失败但可以重试

2. **尝试 hack 所有目标**
   某些目标无法直接 hack，需要先获取密码

3. **阅读所有文件**
   即使不是必需的文件也包含有趣的背景故事

4. **两种结局**
   尝试两种不同的最终选择，体验不同的结局

---

## 进阶技巧

1. **使用 status 跟踪进度**
   随时查看当前关卡和完成状态

2. **善用 hint 命令**
   每个关卡都有提示，卡关时别忘了用

3. **使用 save 保存进度**
   在关键节点保存，可以尝试不同选择

4. **clear 保持界面整洁**
   信息太多时清屏让思路更清晰

---

## 开发者笔记

### 游戏设计理念

1. **渐进式难度**
   - 第一关：教学，简单数学
   - 第二关：中级，逻辑和密码学
   - 第三关：高级，道德选择

2. **剧情主题**
   - 隐私 vs 安全
   - 个人自由 vs 集体安全
   - 真相的代价

3. **游戏机制**
   - 探索：scan, read
   - 解谜：decrypt
   - 行动：hack, execute
   - 进度：save, status

### 扩展可能

如果你想基于此游戏创作：

1. 添加更多关卡到 `game/levels.py`
2. 创建新的命令在 `game/commands.py`
3. 设计新的谜题类型
4. 添加计时挑战
5. 实现成就系统

---

**祝你游戏愉快！**
