---
name: food-macro
description: Use when the user wants food commercial AI video prompts, macro food shots, steaming dishes, or appetizing restaurant videos.
---

# 美食微距视频

食欲感美食特写与蒸汽微距模板。

## 何时使用
- 用户要做 **美食微距视频** 风格的 AI 视频提示词/分镜/成片文案时使用。
- 需要锁定该风格的镜头模板、取值词与避坑清单时使用。

## 风格锁定词（放 prompt 最前，多镜头逐字复用）

Cinematic food commercial, photorealistic macro, warm appetizing light, glossy textures, steam and moisture detail.

## 核心关键字取值

`food commercial`, `macro`, `steam`, `glossy`, `appetizing warm light`

## 避坑

- 避免冷蓝主调
- 不要怪异食物变形
- 手部若出现需稳定

## 提示词模板（含演示图）

演示图：`assets/tpl-food-macro.png`（项目根目录）

### 汤面拉丝

- 画面类型：美食 · 大特写 · 缓慢上移
- 演示图：`assets/tpl-food-macro.png`

```text
Cinematic food commercial macro shot, steaming noodle bowl, chopsticks lifting glossy noodles, broth steam rising, warm appetizing light, extreme close-up texture, slow tilt up. 9:16, 4 seconds.
```

### 煎锅火焰

- 画面类型：美食 · 特写 · 固定微晃
- 演示图：`assets/tpl-food-macro.png`

```text
Photorealistic food shot, chef searing steak in a pan, flame burst, sizzling juices, warm kitchen light, handheld slight shake, macro detail. 16:9, 4 seconds.
```

### 甜品剖面

- 画面类型：美食 · 特写 · 刀切
- 演示图：`assets/tpl-food-macro.png`

```text
Macro dessert commercial, knife slicing a layered chocolate cake, glossy ganache, soft studio light, shallow DOF, slow precise motion. 1:1, 4 seconds.
```

## 推荐工作流

1. 复制风格锁定词 + 一条模板 prompt
2. 只改本镜头的「主体动作 / 运镜 / 景别」
3. 人物与场景卡保持逐字一致
4. 负面提示：`blurry, deformed hands, watermark, text, flickering, morphing`

## 相关

- 项目模板库页面：`index.html` → 「提示词模板库」
- 关键字字典：`index.html` → 「提示词关键字字典」
- 本 skill 包：`ai-video-skills/food-macro/`
