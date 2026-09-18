---
name: ghibli-painterly
description: Use when the user asks for Ghibli-inspired painterly anime video prompts, whimsical nature scenes, rolling hills, or soft magical backgrounds.
---

# 吉卜力手绘视频

吉卜力式手绘自然风光与童话场景模板。

## 何时使用
- 用户要做 **吉卜力手绘视频** 风格的 AI 视频提示词/分镜/成片文案时使用。
- 需要锁定该风格的镜头模板、取值词与避坑清单时使用。

## 风格锁定词（放 prompt 最前，多镜头逐字复用）

Studio Ghibli inspired painterly anime, lush hand-painted nature, soft magical light, whimsical atmosphere, detailed clouds.

## 核心关键字取值

`Ghibli inspired`, `painterly`, `whimsical`, `hand-painted background`

## 避坑

- 避免硬科幻机械词
- 不要高反差硬光
- 保持色彩柔和

## 提示词模板（含演示图）

演示图：`assets/tpl-ghibli-hill.png`（项目根目录）

### 风吹山丘

- 画面类型：空镜 · 远景 · 横摇
- 演示图：`assets/tpl-ghibli-hill.png`

```text
Ghibli inspired painterly anime. Vast green rolling hills under towering clouds, wind blowing through grass and wildflowers. Slow pan right, wide shot, soft volumetric light, whimsical nature, hand-painted background. 16:9, 6 seconds.
```

### 山丘上的红衣

- 画面类型：人物 · 全景 · 拉远
- 演示图：`assets/tpl-ghibli-hill.png`

```text
Ghibli inspired painterly anime, a small girl in a red dress standing on a green hill, camera slowly pulls back to reveal endless sky and clouds, soft golden light, magical calm mood. 16:9, 5 seconds.
```

### 林间光束

- 画面类型：场景 · 中景 · 缓推
- 演示图：`assets/tpl-ghibli-hill.png`

```text
Ghibli inspired forest with god rays through leaves, fireflies drifting, painterly details, slow push in through ferns, peaceful magical atmosphere. 16:9, 5 seconds.
```

## 推荐工作流

1. 复制风格锁定词 + 一条模板 prompt
2. 只改本镜头的「主体动作 / 运镜 / 景别」
3. 人物与场景卡保持逐字一致
4. 负面提示：`blurry, deformed hands, watermark, text, flickering, morphing`

## 相关

- 项目模板库页面：`index.html` → 「提示词模板库」
- 关键字字典：`index.html` → 「提示词关键字字典」
- 本 skill 包：`ai-video-skills/ghibli-painterly/`
