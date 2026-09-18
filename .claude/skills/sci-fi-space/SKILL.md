---
name: sci-fi-space
description: Use when the user wants sci-fi AI video prompts, spaceship interiors, space vistas, holograms, or futuristic technology videos.
---

# 科幻太空视频

飞船舱内、星球舷窗与未来科技模板。

## 何时使用
- 用户要做 **科幻太空视频** 风格的 AI 视频提示词/分镜/成片文案时使用。
- 需要锁定该风格的镜头模板、取值词与避坑清单时使用。

## 风格锁定词（放 prompt 最前，多镜头逐字复用）

Photorealistic sci-fi cinema, sleek spacecraft interiors, cool teal lighting, holographic UI without readable text, vast space vistas.

## 核心关键字取值

`sci-fi`, `spaceship interior`, `holographic`, `planet vista`, `teal lighting`

## 避坑

- 避免中世纪奇幻词
- 不要可读乱码 UI 文字
- 保持科技材质干净

## 提示词模板（含演示图）

演示图：`assets/tpl-sci-fi.png`（项目根目录）

### 舷窗星球

- 画面类型：场景 · 中景 · 缓推
- 演示图：`assets/tpl-sci-fi.png`

```text
Photorealistic sci-fi spaceship interior looking out a large viewport at a glowing planet, cool teal lighting, holographic panels with abstract UI no readable text, slow push toward the glass. 21:9, 6 seconds.
```

### 走廊警报

- 画面类型：场景 · 前移 · 红光
- 演示图：`assets/tpl-sci-fi.png`

```text
Sci-fi corridor with red alert lighting, steam vents, slow camera move forward, cinematic tension, photorealistic hard-surface design. 16:9, 5 seconds.
```

### 太空建立

- 画面类型：空镜 · 大远景 · 漂移
- 演示图：`assets/tpl-sci-fi.png`

```text
Epic space establishing shot, starship drifting above a ringed planet, slow lateral drift, volumetric sun flare, photorealistic sci-fi. 21:9, 6 seconds.
```

## 推荐工作流

1. 复制风格锁定词 + 一条模板 prompt
2. 只改本镜头的「主体动作 / 运镜 / 景别」
3. 人物与场景卡保持逐字一致
4. 负面提示：`blurry, deformed hands, watermark, text, flickering, morphing`

## 相关

- 项目模板库页面：`index.html` → 「提示词模板库」
- 关键字字典：`index.html` → 「提示词关键字字典」
- 本 skill 包：`ai-video-skills/sci-fi-space/`
