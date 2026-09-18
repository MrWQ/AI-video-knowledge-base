---
name: flat-motion-graphics
description: Use when the user wants flat illustration, motion graphics, explainer video, infographic animation, or clean vector AI video prompts.
---

# 扁平动态图形

扁平插画信息动画与说明类视频模板。

## 何时使用
- 用户要做 **扁平动态图形** 风格的 AI 视频提示词/分镜/成片文案时使用。
- 需要锁定该风格的镜头模板、取值词与避坑清单时使用。

## 风格锁定词（放 prompt 最前，多镜头逐字复用）

Flat vector motion graphics, bold geometric shapes, limited palette, clean edges, modern explainer video style, no legible text baked in.

## 核心关键字取值

`flat vector`, `motion graphics`, `explainer`, `geometric`, `limited palette`

## 避坑

- 避免写实景深/胶片颗粒
- 不要复杂笔触
- 画面文字后期叠加

## 提示词模板（含演示图）

演示图：`assets/tpl-flat-graphic.png`（项目根目录）

### 扁平城市说明

- 画面类型：图形 · 中景 · 元素入场
- 演示图：`assets/tpl-flat-graphic.png`

```text
Flat vector motion graphics, clean geometric city skyline, simple character icons sliding into frame, bold teal orange cream palette, smooth UI-like motion, no readable text. 16:9, 5 seconds.
```

### 图标流程动画

- 画面类型：信息 · 固定 · 元素弹入
- 演示图：`assets/tpl-flat-graphic.png`

```text
Flat motion graphics sequence, abstract nodes and arrows connecting with bouncy spring motion, minimal background, modern tech explainer style, no text. 1:1, 4 seconds.
```

### 扁平人物行走

- 画面类型：角色 · 侧面 · 循环
- 演示图：`assets/tpl-flat-graphic.png`

```text
Flat 2D vector character walking loop in side view, simple shapes, consistent stroke weight, soft color blocks, seamless loop. 16:9, 4 seconds.
```

## 推荐工作流

1. 复制风格锁定词 + 一条模板 prompt
2. 只改本镜头的「主体动作 / 运镜 / 景别」
3. 人物与场景卡保持逐字一致
4. 负面提示：`blurry, deformed hands, watermark, text, flickering, morphing`

## 相关

- 项目模板库页面：`index.html` → 「提示词模板库」
- 关键字字典：`index.html` → 「提示词关键字字典」
- 本 skill 包：`ai-video-skills/flat-motion-graphics/`
