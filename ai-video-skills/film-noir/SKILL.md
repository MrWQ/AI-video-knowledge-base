---
name: film-noir
description: Use when the user wants film noir AI video prompts, black-and-white detective scenes, hard chiaroscuro lighting, or classic mystery mood.
---

# 黑色电影视频

黑白高反差侦探与雨夜悬疑模板。

## 何时使用
- 用户要做 **黑色电影视频** 风格的 AI 视频提示词/分镜/成片文案时使用。
- 需要锁定该风格的镜头模板、取值词与避坑清单时使用。

## 风格锁定词（放 prompt 最前，多镜头逐字复用）

Film noir, black and white, hard chiaroscuro lighting, 35mm grain, venetian blind shadows, mysterious mood.

## 核心关键字取值

`film noir`, `black and white`, `chiaroscuro`, `venetian shadows`, `grain`

## 避坑

- 避免高饱和霓虹彩
- 不要欢快情绪词
- 保持低照度

## 提示词模板（含演示图）

演示图：`assets/tpl-noir-detective.png`（项目根目录）

### 雨夜侦探

- 画面类型：人物 · 中景 · 缓推
- 演示图：`assets/tpl-noir-detective.png`

```text
Film noir black and white. A detective in a trench coat and hat stands under a streetlamp in a rainy alley at night. Slow push in, medium shot, hard chiaroscuro shadows, 35mm grain, mysterious mood. 16:9, 5 seconds.
```

### 百叶窗室内

- 画面类型：室内 · 中近景 · 固定
- 演示图：`assets/tpl-noir-detective.png`

```text
Film noir interior, hard light through venetian blinds casting stripes on a tense face, cigarette smoke curling, low-key black and white, locked-off medium close-up. 16:9, 4 seconds.
```

### 空巷拉远

- 画面类型：空镜 · 全景 · 拉远
- 演示图：`assets/tpl-noir-detective.png`

```text
Film noir empty wet alley at night, single streetlamp, camera slowly pulls back to reveal long shadows, black and white, grain, lonely atmosphere. 16:9, 5 seconds.
```

## 推荐工作流

1. 复制风格锁定词 + 一条模板 prompt
2. 只改本镜头的「主体动作 / 运镜 / 景别」
3. 人物与场景卡保持逐字一致
4. 负面提示：`blurry, deformed hands, watermark, text, flickering, morphing`

## 相关

- 项目模板库页面：`index.html` → 「提示词模板库」
- 关键字字典：`index.html` → 「提示词关键字字典」
- 本 skill 包：`ai-video-skills/film-noir/`
