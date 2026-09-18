---
name: cinematic-realism
description: Use when the user asks for photorealistic cinematic AI video prompts, film-look shots, dramatic character scenes, or 35mm movie-style video generation.
---

# 电影写实视频

写实电影感人物与剧情镜头的提示词模板。

## 何时使用
- 用户要做 **电影写实视频** 风格的 AI 视频提示词/分镜/成片文案时使用。
- 需要锁定该风格的镜头模板、取值词与避坑清单时使用。

## 风格锁定词（放 prompt 最前，多镜头逐字复用）

Cinematic photorealistic, 35mm film look, shallow depth of field, subtle film grain, natural skin tones.

## 核心关键字取值

`cinematic photorealistic`, `35mm film`, `teal and orange`, `shallow DOF`, `rim light`

## 避坑

- 不要同时写 cartoon 与 photorealistic
- 避免一镜头堆多个运镜
- 文字/logo 交给后期

## 提示词模板（含演示图）

演示图：`assets/style-photoreal.png`（项目根目录）

### 雨夜人物推进

- 画面类型：人物 · 中近景 · 推进
- 演示图：`assets/style-photoreal.png`

```text
Cinematic photorealistic, 35mm film look. A 25-year-old woman in a red wool coat walks slowly through a rainy neon alley in Tokyo at night. Slow dolly in, medium close-up, eye level. Wet asphalt reflects cyan and orange neon. Rim light from behind, soft fill on face. Teal and orange grade, shallow DOF. 16:9, 5 seconds.
```

### 城市建立镜头

- 画面类型：空镜 · 大远景 · 航拍缓推
- 演示图：`assets/style-photoreal.png`

```text
Cinematic photorealistic establishing shot of a rainy neon city at night, extreme wide aerial view, slow push in toward a glowing alley, volumetric haze, teal and orange grade, 35mm film grain. 16:9, 5 seconds.
```

### 对话过肩

- 画面类型：双人 · 过肩 · 固定
- 演示图：`assets/style-photoreal.png`

```text
Cinematic photorealistic film still, over-the-shoulder shot in a dim cafe at night, rain on windows, woman in red coat listening, warm practical lamps, shallow DOF, natural skin tones. Locked-off camera, medium close-up. 16:9, 4 seconds.
```

## 推荐工作流

1. 复制风格锁定词 + 一条模板 prompt
2. 只改本镜头的「主体动作 / 运镜 / 景别」
3. 人物与场景卡保持逐字一致
4. 负面提示：`blurry, deformed hands, watermark, text, flickering, morphing`

## 相关

- 项目模板库页面：`index.html` → 「提示词模板库」
- 关键字字典：`index.html` → 「提示词关键字字典」
- 本 skill 包：`ai-video-skills/cinematic-realism/`
