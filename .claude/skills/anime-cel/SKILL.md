---
name: anime-cel
description: Use when the user wants Japanese anime cel-style AI video prompts, school rooftop scenes, anime city night, or clean line-art animation videos.
---

# 日式动画视频

赛璐璐日式动画角色与校园/都市场景模板。

## 何时使用
- 用户要做 **日式动画视频** 风格的 AI 视频提示词/分镜/成片文案时使用。
- 需要锁定该风格的镜头模板、取值词与避坑清单时使用。

## 风格锁定词（放 prompt 最前，多镜头逐字复用）

Japanese anime cel animation, clean line art, painted background, soft glow highlights, vibrant but controlled colors.

## 核心关键字取值

`anime cel style`, `painted background`, `Makoto Shinkai inspired`, `clean line art`

## 避坑

- 避免 photorealistic 皮肤词
- 不要过度写实景深
- 口型台词慎用

## 提示词模板（含演示图）

演示图：`assets/tpl-anime-school.png`（项目根目录）

### 天台少女 · 夕阳

- 画面类型：人物 · 中景 · 缓慢环绕
- 演示图：`assets/tpl-anime-school.png`

```text
Japanese anime cel style. A high school girl in uniform stands on the rooftop at sunset, cherry blossoms drifting, wind in her hair. Slow orbit shot, medium shot, warm golden sky with dramatic clouds, clean line art, painterly background. 16:9, 5 seconds.
```

### 雨夜动画街

- 画面类型：场景 · 中景 · 跟随
- 演示图：`assets/tpl-anime-school.png`

```text
Anime cel style city street at night in rain, neon signs reflecting on wet ground, a girl with umbrella walking away. Camera follows from behind, medium shot, soft light blooms, painted background. 16:9, 5 seconds.
```

### 大特写眼神

- 画面类型：特写 · 固定
- 演示图：`assets/tpl-anime-school.png`

```text
Anime cel style extreme close-up of a girl's eyes reflecting city lights, subtle emotional blink, clean lines, soft shading, shallow glow. Static shot. 16:9, 3 seconds.
```

## 推荐工作流

1. 复制风格锁定词 + 一条模板 prompt
2. 只改本镜头的「主体动作 / 运镜 / 景别」
3. 人物与场景卡保持逐字一致
4. 负面提示：`blurry, deformed hands, watermark, text, flickering, morphing`

## 相关

- 项目模板库页面：`index.html` → 「提示词模板库」
- 关键字字典：`index.html` → 「提示词关键字字典」
- 本 skill 包：`ai-video-skills/anime-cel/`
