---
name: oil-painting
description: Use when the user wants oil painting, impasto, impressionist, or fine-art painterly AI video prompts.
---

# 油画艺术视频

厚涂油画与印象派光影镜头模板。

## 何时使用
- 用户要做 **油画艺术视频** 风格的 AI 视频提示词/分镜/成片文案时使用。
- 需要锁定该风格的镜头模板、取值词与避坑清单时使用。

## 风格锁定词（放 prompt 最前，多镜头逐字复用）

Oil painting style, thick impasto brushwork, visible palette knife texture, rich pigment mixing, impressionist light.

## 核心关键字取值

`oil painting`, `impasto`, `impressionist`, `palette knife`, `brushwork`

## 避坑

- 避免光滑 3D 塑料感
- 不要锐利数码噪点
- 保持笔触可见

## 提示词模板（含演示图）

演示图：`assets/style-oil.png`（项目根目录）

### 油画人物夜巷

- 画面类型：人物 · 中景 · 缓推
- 演示图：`assets/style-oil.png`

```text
Oil painting style, thick impasto brushwork. A woman in a red coat in a rain-lit alley at night, neon colors melted into painterly strokes. Slow push in, medium shot, impressionist night atmosphere. 16:9, 5 seconds.
```

### 印象派风景

- 画面类型：空镜 · 远景 · 摇镜
- 演示图：`assets/style-oil.png`

```text
Impressionist oil painting landscape at dusk, loose brush strokes of sky and water, slow pan left, rich color mixing, canvas texture visible. 16:9, 5 seconds.
```

### 静物油画

- 画面类型：产品 · 特写 · 固定
- 演示图：`assets/style-oil.png`

```text
Oil painting still life, fruit and ceramic on a table, dramatic side light, impasto highlights, classical composition, static shot. 4:3, 4 seconds.
```

## 推荐工作流

1. 复制风格锁定词 + 一条模板 prompt
2. 只改本镜头的「主体动作 / 运镜 / 景别」
3. 人物与场景卡保持逐字一致
4. 负面提示：`blurry, deformed hands, watermark, text, flickering, morphing`

## 相关

- 项目模板库页面：`index.html` → 「提示词模板库」
- 关键字字典：`index.html` → 「提示词关键字字典」
- 本 skill 包：`ai-video-skills/oil-painting/`
