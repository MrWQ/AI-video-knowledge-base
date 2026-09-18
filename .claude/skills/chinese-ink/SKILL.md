---
name: chinese-ink
description: Use when the user wants Chinese ink wash, sumi-e, traditional guofeng, or minimalist ink animation AI video prompts.
---

# 中国水墨视频

水墨山水、留白与朱砂点缀动画模板。

## 何时使用
- 用户要做 **中国水墨视频** 风格的 AI 视频提示词/分镜/成片文案时使用。
- 需要锁定该风格的镜头模板、取值词与避坑清单时使用。

## 风格锁定词（放 prompt 最前，多镜头逐字复用）

Traditional Chinese ink wash painting, sumi-e brush strokes, misty mountains, sparse negative space, subtle vermilion accent.

## 核心关键字取值

`Chinese ink wash`, `sumi-e`, `misty mountains`, `negative space`, `vermilion accent`

## 避坑

- 避免赛博霓虹
- 不要厚涂油画笔触
- 色彩克制，仅朱砂点缀

## 提示词模板（含演示图）

演示图：`assets/tpl-ink-mountain.png`（项目根目录）

### 水墨行旅

- 画面类型：人物 · 远景 · 横移
- 演示图：`assets/tpl-ink-mountain.png`

```text
Traditional Chinese ink wash animation. A lone traveler walks on a mountain path in mist. Slow lateral tracking, wide shot, sumi-e brushwork, vast negative space, single vermilion accent on the figure. 16:9, 6 seconds.
```

### 山水显形

- 画面类型：空镜 · 缓显 · 固定+雾动
- 演示图：`assets/tpl-ink-mountain.png`

```text
Chinese ink wash painting comes alive, mist drifting across layered mountain silhouettes, ink gradients blooming on paper texture, static camera, meditative pace. 16:9, 6 seconds.
```

### 水墨飞鸟

- 画面类型：特写元素 · 固定
- 演示图：`assets/tpl-ink-mountain.png`

```text
Sumi-e style, a single ink-brush bird flies across white space, wet ink trails, minimal composition, elegant traditional aesthetic. 1:1, 4 seconds.
```

## 推荐工作流

1. 复制风格锁定词 + 一条模板 prompt
2. 只改本镜头的「主体动作 / 运镜 / 景别」
3. 人物与场景卡保持逐字一致
4. 负面提示：`blurry, deformed hands, watermark, text, flickering, morphing`

## 相关

- 项目模板库页面：`index.html` → 「提示词模板库」
- 关键字字典：`index.html` → 「提示词关键字字典」
- 本 skill 包：`ai-video-skills/chinese-ink/`
