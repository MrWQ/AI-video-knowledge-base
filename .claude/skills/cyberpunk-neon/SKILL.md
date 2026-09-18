---
name: cyberpunk-neon
description: Use when the user wants cyberpunk AI video prompts, neon city night shots, rainy futuristic alleys, or high-tech noir atmosphere.
---

# 赛博朋克视频

霓虹未来都市与赛博角色镜头模板。

## 何时使用
- 用户要做 **赛博朋克视频** 风格的 AI 视频提示词/分镜/成片文案时使用。
- 需要锁定该风格的镜头模板、取值词与避坑清单时使用。

## 风格锁定词（放 prompt 最前，多镜头逐字复用）

Cyberpunk concept art photoreal hybrid, dense neon signage, wet reflective streets, magenta cyan palette, futuristic clutter.

## 核心关键字取值

`cyberpunk`, `neon signs`, `wet streets`, `cyan magenta`, `holographic`

## 避坑

- 避免过亮白昼
- 不要田园/吉卜力词
- 文字招牌写 no legible text

## 提示词模板（含演示图）

演示图：`assets/style-cyberpunk.png`（项目根目录）

### 霓虹巷推进

- 画面类型：人物 · 中近景 · 推进
- 演示图：`assets/style-cyberpunk.png`

```text
Cyberpunk photorealistic night, young woman in a red coat walking through a dense neon alley in the rain. Slow dolly in, medium close-up. Magenta and cyan neon, wet reflective asphalt, steam vents, holographic ads without readable text. 16:9, 5 seconds.
```

### 未来天际线

- 画面类型：空镜 · 大远景 · 航拍
- 演示图：`assets/style-cyberpunk.png`

```text
Cyberpunk city skyline at night in rain, flying vehicles leaving light trails, extreme wide aerial establishing shot, slow drift forward, neon grid below. 21:9, 5 seconds.
```

### FPV 穿街

- 画面类型：动作 · FPV · 高速
- 演示图：`assets/style-cyberpunk.png`

```text
FPV drone flying at high speed through a cyberpunk neon alley at night, tilted horizon, light streaks, rain, immersive first-person flight. 16:9, 4 seconds.
```

## 推荐工作流

1. 复制风格锁定词 + 一条模板 prompt
2. 只改本镜头的「主体动作 / 运镜 / 景别」
3. 人物与场景卡保持逐字一致
4. 负面提示：`blurry, deformed hands, watermark, text, flickering, morphing`

## 相关

- 项目模板库页面：`index.html` → 「提示词模板库」
- 关键字字典：`index.html` → 「提示词关键字字典」
- 本 skill 包：`ai-video-skills/cyberpunk-neon/`
