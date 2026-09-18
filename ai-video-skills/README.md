# AI 视频提示词 Skill 包

本文件夹保存各风格的 **提示词 Skill**。每个风格一套，可直接改模板生成视频。

## 加载位置

- 项目内可读包：`ai-video-skills/<style-id>/`
- MiMo Desktop 项目技能：`.claude/skills/<style-id>/`（含 `SKILL.md` + `locales/`）
- 新建技能后需 **新开对话** 才会在插件/技能列表生效

## 演示图

统一放在 `assets/` 下（`style-*.png` / `tpl-*.png`），模板内以路径引用。

## 风格一览

| ID | 名称 | 演示图 | 模板数 |
|----|------|--------|--------|
| `cinematic-realism` | 电影写实视频 | `style-photoreal.png` (有) | 3 |
| `anime-cel` | 日式动画视频 | `tpl-anime-school.png` (有) | 3 |
| `ghibli-painterly` | 吉卜力手绘视频 | `tpl-ghibli-hill.png` (有) | 3 |
| `cgi-pixar` | 3D卡通视频 | `style-3d.png` (有) | 3 |
| `cyberpunk-neon` | 赛博朋克视频 | `style-cyberpunk.png` (有) | 3 |
| `film-noir` | 黑色电影视频 | `tpl-noir-detective.png` (有) | 3 |
| `chinese-ink` | 中国水墨视频 | `tpl-ink-mountain.png` (有) | 3 |
| `oil-painting` | 油画艺术视频 | `style-oil.png` (有) | 3 |
| `product-commercial` | 产品广告视频 | `tpl-product-watch.png` (有) | 3 |
| `food-macro` | 美食微距视频 | `tpl-food-macro.png` (有) | 3 |
| `aerial-travel` | 航拍风光视频 | `tpl-aerial-coast.png` (有) | 3 |
| `horror-atmosphere` | 恐怖氛围视频 | `tpl-horror.png` (有) | 3 |
| `sports-fpv` | 运动FPV视频 | `tpl-sports-fpv.png` (有) | 3 |
| `sci-fi-space` | 科幻太空视频 | `tpl-sci-fi.png` (有) | 3 |
| `flat-motion-graphics` | 扁平动态图形 | `tpl-flat-graphic.png` (有) | 3 |
| `claymation` | 黏土定格视频 | `style-clay.png` (有) | 3 |

## 使用方式

1. 在 Agent 中描述：「用 cinematic-realism 模板做一条雨夜人物镜头」
2. 或直接打开对应文件夹复制 `templates.md` 中的 prompt
3. 配套网页手册：项目根目录 `index.html`（关键字字典 + 模板库）
