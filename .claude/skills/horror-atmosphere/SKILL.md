---
name: horror-atmosphere
description: Use when the user wants horror AI video prompts, abandoned places, suspense atmosphere, dark corridors, or thriller mood videos.
---

# 恐怖氛围视频

废弃空间、底光与悬疑惊悚镜头模板。

## 何时使用
- 用户要做 **恐怖氛围视频** 风格的 AI 视频提示词/分镜/成片文案时使用。
- 需要锁定该风格的镜头模板、取值词与避坑清单时使用。

## 风格锁定词（放 prompt 最前，多镜头逐字复用）

Cinematic horror atmosphere, photorealistic dark spaces, flickering practical lights, fog, dread mood, desaturated grade.

## 核心关键字取值

`horror atmosphere`, `flickering light`, `abandoned`, `fog`, `low-key`

## 避坑

- 避免明亮高调广告光
- 不要卡通可爱角色
- 血腥写实要谨慎/可关闭

## 提示词模板（含演示图）

演示图：`assets/tpl-horror.png`（项目根目录）

### 废弃医院走廊

- 画面类型：场景 · 中景 · 缓慢前移
- 演示图：`assets/tpl-horror.png`

```text
Cinematic horror atmosphere, abandoned hospital corridor at night, flickering fluorescent lights, fog, slow steadicam push forward, desaturated grade, dread mood, photorealistic. 16:9, 6 seconds.
```

### 门缝底光

- 画面类型：特写 · 固定
- 演示图：`assets/tpl-horror.png`

```text
Horror still-frame motion, light leaking under a closed door in darkness, dust in beam, subtle camera creep in, tense silence mood. 21:9, 5 seconds.
```

### 回头惊悚

- 画面类型：人物 · 中近景 · 手持
- 演示图：`assets/tpl-horror.png`

```text
Handheld horror shot, person in dark hallway slowly looking over shoulder, underlight flicker, grain, shallow DOF, suspenseful. 16:9, 4 seconds.
```

## 推荐工作流

1. 复制风格锁定词 + 一条模板 prompt
2. 只改本镜头的「主体动作 / 运镜 / 景别」
3. 人物与场景卡保持逐字一致
4. 负面提示：`blurry, deformed hands, watermark, text, flickering, morphing`

## 相关

- 项目模板库页面：`index.html` → 「提示词模板库」
- 关键字字典：`index.html` → 「提示词关键字字典」
- 本 skill 包：`ai-video-skills/horror-atmosphere/`
