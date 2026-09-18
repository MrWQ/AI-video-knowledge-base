---
name: product-commercial
description: Use when the user wants product commercial AI video prompts, packshots, luxury watches, headphones, or studio product films.
---

# 产品广告视频

高端产品商业广告与棚拍镜头模板。

## 何时使用
- 用户要做 **产品广告视频** 风格的 AI 视频提示词/分镜/成片文案时使用。
- 需要锁定该风格的镜头模板、取值词与避坑清单时使用。

## 风格锁定词（放 prompt 最前，多镜头逐字复用）

Premium product commercial, photorealistic CGI or studio photography, controlled highlights, deep blacks, luxury grade.

## 核心关键字取值

`product commercial`, `studio lighting`, `packshot`, `reflective surface`, `luxury`

## 避坑

- 避免杂乱背景杂物
- 不要人脸抢主体
- logo/文字默认关闭

## 提示词模板（含演示图）

演示图：`assets/tpl-product-watch.png`（项目根目录）

### 腕表环绕

- 画面类型：产品 · 特写 · 环绕
- 演示图：`assets/tpl-product-watch.png`

```text
Premium product commercial, photorealistic. An elegant wristwatch on dark reflective stone. Camera slowly orbits, close-up, low angle. Soft key light with cool rim highlight, black and gold grade, macro details. No text on dial. 1:1, 4 seconds.
```

### 耳机开箱氛围

- 画面类型：产品 · 中近景 · 推进
- 演示图：`assets/tpl-product-watch.png`

```text
Luxury headphone product film, matte black headphones on wet black surface with subtle neon reflections, slow dolly in, shallow DOF, cinematic commercial lighting. 16:9, 4 seconds.
```

### 悬浮产品

- 画面类型：产品 · 固定 · 微动
- 演示图：`assets/tpl-product-watch.png`

```text
Product floating in dark studio, soft gradient background, gentle rotation of object only, specular highlights sweeping, premium CGI packshot. 9:16, 4 seconds.
```

## 推荐工作流

1. 复制风格锁定词 + 一条模板 prompt
2. 只改本镜头的「主体动作 / 运镜 / 景别」
3. 人物与场景卡保持逐字一致
4. 负面提示：`blurry, deformed hands, watermark, text, flickering, morphing`

## 相关

- 项目模板库页面：`index.html` → 「提示词模板库」
- 关键字字典：`index.html` → 「提示词关键字字典」
- 本 skill 包：`ai-video-skills/product-commercial/`
