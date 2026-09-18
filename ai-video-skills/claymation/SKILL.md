---
name: claymation
description: Use when the user wants claymation, stop-motion, miniature diorama, or handmade toy-style AI video prompts.
---

# 黏土定格视频

黏土玩偶微缩布景与定格动画模板。

## 何时使用
- 用户要做 **黏土定格视频** 风格的 AI 视频提示词/分镜/成片文案时使用。
- 需要锁定该风格的镜头模板、取值词与避坑清单时使用。

## 风格锁定词（放 prompt 最前，多镜头逐字复用）

Stop-motion claymation, handmade clay textures, practical miniature set, soft toy-like lighting, shallow macro focus.

## 核心关键字取值

`claymation`, `stop motion`, `miniature`, `handmade`, `macro shallow focus`

## 避坑

- 避免光滑工业 CGI
- 不要超写实人类皮肤
- 保持玩偶比例

## 提示词模板（含演示图）

演示图：`assets/style-clay.png`（项目根目录）

### 雨巷黏土人物

- 画面类型：角色 · 中景 · 缓推
- 演示图：`assets/style-clay.png`

```text
Stop-motion claymation, handmade clay character in a red coat on a miniature rainy neon alley set, slow push in, soft practical lights, shallow macro focus, tactile textures. 16:9, 5 seconds.
```

### 微缩小镇建立

- 画面类型：空镜 · 全景 · 横摇
- 演示图：`assets/style-clay.png`

```text
Miniature claymation town diorama, tiny houses and street lamps, slow pan across the set, warm tabletop lighting, handmade charm. 16:9, 5 seconds.
```

### 黏土手部动作

- 画面类型：特写 · 固定
- 演示图：`assets/style-clay.png`

```text
Close-up claymation shot, clay hands carefully placing a tiny object on a miniature table, macro depth of field, stop-motion warmth. 1:1, 4 seconds.
```

## 推荐工作流

1. 复制风格锁定词 + 一条模板 prompt
2. 只改本镜头的「主体动作 / 运镜 / 景别」
3. 人物与场景卡保持逐字一致
4. 负面提示：`blurry, deformed hands, watermark, text, flickering, morphing`

## 相关

- 项目模板库页面：`index.html` → 「提示词模板库」
- 关键字字典：`index.html` → 「提示词关键字字典」
- 本 skill 包：`ai-video-skills/claymation/`
