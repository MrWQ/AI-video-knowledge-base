# AI 视频制作因素知识库 — DESIGN

## Style anchor
Criterion Collection 影片笔记 + 1970s 相机说明书 + 现代研究手账。
正文可长读；演示区像“监视器窗口”。

## Palette
- Paper: `#F5F0E6`
- Ink: `#1C1B18`
- Muted: `#6B6560`
- Accent amber: `#C45C26`
- Diagram teal: `#2A6F6F`
- Monitor dark: `#141412`
- Hairline: `#D9D2C5`

## Typography
- Display: Georgia / Songti SC / SimSun / serif — 标题、章节号
- Body: Segoe UI / PingFang SC / Microsoft YaHei / sans-serif
- Scale: 42 / 28 / 18 / 15 / 13
- 标题衬线 + 正文无衬线；演示标签等宽（Consolas / monospace）

## Layout
- Desktop: 左侧 sticky TOC（约 220px）+ 正文 max-width 880px
- Mobile: 顶栏 + 折叠目录
- 节奏：章节大间距 64–96px，卡片内 16–24px
- 演示框：深色圆角“监视器”，内嵌 SVG/图，下方 caption + 术语中英

## Signature moments
1. **运镜动态演示**：SVG 场景 + CSS 动画，持续循环，可播放/暂停；路径示意与画面效果同框
2. **风格接触印相**：静态图网格，像底片小样
3. **一致性技巧**：提示词模板可复制卡片

## Content map
1. 总览地图（因素分类）
2. 运镜 Camera Movement（动态）
3. 景别 Shot Size（动态框选）
4. 角度 Angle
5. 镜头/焦段 Lens
6. 构图 Composition
7. 光影 Lighting
8. 风格 Style（静态图）
9. 色彩 Color
10. 运动与物理 Motion
11. 技术参数 Technical
12. 一致性技巧 Tips
13. Prompt 结构模板

## Assets
- `assets/style-*.png`：image_gen 生成，同一主体（红大衣年轻女性 + 雨夜街景）换风格，便于对比
- 运镜/景别：页面内 SVG 动画，无外部 GIF 依赖
- 无 CDN，系统字体，离线可开
