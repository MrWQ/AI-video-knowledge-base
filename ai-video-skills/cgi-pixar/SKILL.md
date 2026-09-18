---
name: cgi-pixar
description: Use when the user wants Pixar-like or stylized 3D CGI AI video prompts, cute character animation, or polished 3D commercial animation.
---

# 3D卡通视频

皮克斯式 3D 角色与商业动画模板。

## 何时使用
- 用户要做 **3D卡通视频** 风格的 AI 视频提示词/分镜/成片文案时使用。
- 需要锁定该风格的镜头模板、取值词与避坑清单时使用。

## 风格锁定词（放 prompt 最前，多镜头逐字复用）

Stylized 3D CGI animation, Pixar-like character design, soft subsurface skin, glossy materials, cinematic lighting.

## 核心关键字取值

`stylized 3D CGI`, `Pixar-like`, `subsurface scattering`, `polished render`

## 避坑

- 避免 gritty realistic dirt 过量
- 不要真人皮肤纹理词
- 角色保持圆润可爱比例

## 提示词模板（含演示图）

演示图：`assets/style-3d.png`（项目根目录）

### 3D 角色出场

- 画面类型：角色 · 中景 · 弧线推进
- 演示图：`assets/style-3d.png`

```text
Stylized 3D CGI Pixar-like animation. A cute round character in a red coat steps into a rain-wet neon street at night. Camera arcs in, medium shot, glossy reflections, soft cinematic lighting, appealing design. 16:9, 5 seconds.
```

### 产品 3D 演示

- 画面类型：产品 · 特写 · 环绕
- 演示图：`assets/style-3d.png`

```text
High-quality 3D CGI product animation, matte black headphones floating on dark reflective floor, camera orbits slowly, studio softboxes, clean commercial look. 1:1, 4 seconds.
```

### 欢乐群像

- 画面类型：群体 · 全景 · 摇镜
- 演示图：`assets/style-3d.png`

```text
Pixar-like 3D ensemble of colorful characters waving in a bright stylized town square, pan left to right, sunny cheerful lighting, polished render. 16:9, 5 seconds.
```

## 推荐工作流

1. 复制风格锁定词 + 一条模板 prompt
2. 只改本镜头的「主体动作 / 运镜 / 景别」
3. 人物与场景卡保持逐字一致
4. 负面提示：`blurry, deformed hands, watermark, text, flickering, morphing`

## 相关

- 项目模板库页面：`index.html` → 「提示词模板库」
- 关键字字典：`index.html` → 「提示词关键字字典」
- 本 skill 包：`ai-video-skills/cgi-pixar/`
