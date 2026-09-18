---
name: sports-fpv
description: Use when the user wants sports AI video prompts, FPV drone racing, extreme sports, high-speed chase, or dynamic action camera footage.
---

# 运动FPV视频

极限运动、穿越机与高速跟拍模板。

## 何时使用
- 用户要做 **运动FPV视频** 风格的 AI 视频提示词/分镜/成片文案时使用。
- 需要锁定该风格的镜头模板、取值词与避坑清单时使用。

## 风格锁定词（放 prompt 最前，多镜头逐字复用）

Cinematic action sports, high-energy FPV or gimbal follow, motion blur streaks, vivid but clean grade.

## 核心关键字取值

`FPV drone`, `high speed`, `action sports`, `motion blur`, `first person`

## 避坑

- 避免静止锁死机位
- 不要过多慢动作堆叠
- 路径写清空间

## 提示词模板（含演示图）

演示图：`assets/tpl-sports-fpv.png`（项目根目录）

### 城市峡谷俯冲

- 画面类型：FPV · 高速 · 俯冲
- 演示图：`assets/tpl-sports-fpv.png`

```text
FPV drone diving through a neon city canyon at night at high speed, tilted horizon, light streaks, rain mist, cinematic action sports energy. 16:9, 4 seconds.
```

### 滑板跟拍

- 画面类型：运动 · 侧跟 · 低角度
- 演示图：`assets/tpl-sports-fpv.png`

```text
Low-angle tracking shot following a skateboarder through a sunlit skatepark, smooth gimbal motion, dust particles, energetic sports film look. 16:9, 5 seconds.
```

### 跑酷飞跃

- 画面类型：动作 · 升格 · 弧线
- 演示图：`assets/tpl-sports-fpv.png`

```text
Slow-motion action shot, athlete parkour leap between rooftops, camera arcs around mid-air pose, golden hour rim light, epic sports commercial. 16:9, 4 seconds.
```

## 推荐工作流

1. 复制风格锁定词 + 一条模板 prompt
2. 只改本镜头的「主体动作 / 运镜 / 景别」
3. 人物与场景卡保持逐字一致
4. 负面提示：`blurry, deformed hands, watermark, text, flickering, morphing`

## 相关

- 项目模板库页面：`index.html` → 「提示词模板库」
- 关键字字典：`index.html` → 「提示词关键字字典」
- 本 skill 包：`ai-video-skills/sports-fpv/`
