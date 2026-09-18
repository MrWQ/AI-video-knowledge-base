---
name: aerial-travel
description: Use when the user wants aerial travel AI video prompts, drone landscape shots, coastline, or epic establishing footage.
---

# 航拍风光视频

旅行航拍、海岸与城市建立镜头模板。

## 何时使用
- 用户要做 **航拍风光视频** 风格的 AI 视频提示词/分镜/成片文案时使用。
- 需要锁定该风格的镜头模板、取值词与避坑清单时使用。

## 风格锁定词（放 prompt 最前，多镜头逐字复用）

Cinematic aerial travel photography, photorealistic drone footage, golden hour or clean daylight, epic scale.

## 核心关键字取值

`aerial drone shot`, `establishing`, `golden hour`, `epic landscape`, `bird's-eye`

## 避坑

- 避免镜头内过多小人脸
- 不要文本标注
- 比例感要靠地标

## 提示词模板（含演示图）

演示图：`assets/tpl-aerial-coast.png`（项目根目录）

### 海岸线航拍

- 画面类型：风光 · 大远景 · 前推
- 演示图：`assets/tpl-aerial-coast.png`

```text
Cinematic aerial drone shot of turquoise coastline, waves meeting golden cliffs, golden hour light, slow forward flight, epic travel establishing shot, photorealistic. 16:9, 6 seconds.
```

### 城市鸟瞰夜

- 画面类型：城市 · 鸟瞰 · 缓降
- 演示图：`assets/tpl-aerial-coast.png`

```text
Aerial night drone footage over a dense city, glowing street grid, slow descending move, light haze, cinematic travel film look. 16:9, 5 seconds.
```

### 山脊掠过

- 画面类型：风光 · FPV/掠过
- 演示图：`assets/tpl-aerial-coast.png`

```text
Drone flying fast along a mountain ridge at sunrise, light breaking over peaks, dynamic speed, photorealistic aerial adventure. 16:9, 5 seconds.
```

## 推荐工作流

1. 复制风格锁定词 + 一条模板 prompt
2. 只改本镜头的「主体动作 / 运镜 / 景别」
3. 人物与场景卡保持逐字一致
4. 负面提示：`blurry, deformed hands, watermark, text, flickering, morphing`

## 相关

- 项目模板库页面：`index.html` → 「提示词模板库」
- 关键字字典：`index.html` → 「提示词关键字字典」
- 本 skill 包：`ai-video-skills/aerial-travel/`
