# -*- coding: utf-8 -*-
from pathlib import Path
import re

ROOT = Path(r"D:\ai_desktop_project\xiaomi")
html_path = ROOT / "index.html"
html = html_path.read_text(encoding="utf-8")

# data mirrors build script primary templates
TEMPLATES = [
    ("cinematic-realism", "电影写实", "style-photoreal.png",
     "Cinematic photorealistic, 35mm film look, shallow DOF, subtle grain.",
     "ai-video-skills/cinematic-realism",
     [
      ("雨夜人物推进", "人物 · 中近景 · 推进",
       "Cinematic photorealistic, 35mm film look. A 25-year-old woman in a red wool coat walks slowly through a rainy neon alley in Tokyo at night. Slow dolly in, medium close-up, eye level. Wet asphalt reflects cyan and orange neon. Rim light from behind, soft fill on face. Teal and orange grade, shallow DOF. 16:9, 5 seconds."),
      ("城市建立镜头", "空镜 · 大远景 · 航拍缓推",
       "Cinematic photorealistic establishing shot of a rainy neon city at night, extreme wide aerial view, slow push in toward a glowing alley, volumetric haze, teal and orange grade, 35mm film grain. 16:9, 5 seconds."),
      ("对话过肩", "双人 · 过肩 · 固定",
       "Cinematic photorealistic film still, over-the-shoulder shot in a dim cafe at night, rain on windows, woman in red coat listening, warm practical lamps, shallow DOF, natural skin tones. Locked-off camera, medium close-up. 16:9, 4 seconds."),
     ]),
    ("anime-cel", "日式动画", "tpl-anime-school.png",
     "Japanese anime cel animation, clean line art, painted background.",
     "ai-video-skills/anime-cel",
     [
      ("天台少女 · 夕阳", "人物 · 中景 · 环绕",
       "Japanese anime cel style. A high school girl in uniform stands on the rooftop at sunset, cherry blossoms drifting, wind in her hair. Slow orbit shot, medium shot, warm golden sky, clean line art, painterly background. 16:9, 5 seconds."),
      ("雨夜动画街", "场景 · 中景 · 跟随",
       "Anime cel style city street at night in rain, neon signs reflecting on wet ground, a girl with umbrella walking away. Camera follows from behind, medium shot, soft light blooms. 16:9, 5 seconds."),
      ("大特写眼神", "特写 · 固定",
       "Anime cel style extreme close-up of a girl's eyes reflecting city lights, subtle emotional blink, clean lines, soft shading. Static shot. 16:9, 3 seconds."),
     ]),
    ("ghibli-painterly", "吉卜力手绘", "tpl-ghibli-hill.png",
     "Ghibli inspired painterly anime, lush nature, soft magical light.",
     "ai-video-skills/ghibli-painterly",
     [
      ("风吹山丘", "空镜 · 远景 · 横摇",
       "Ghibli inspired painterly anime. Vast green rolling hills under towering clouds, wind through grass. Slow pan right, wide shot, soft volumetric light. 16:9, 6 seconds."),
      ("山丘上的红衣", "人物 · 全景 · 拉远",
       "Ghibli inspired painterly anime, a small girl in a red dress on a green hill, camera slowly pulls back to reveal endless sky, soft golden light. 16:9, 5 seconds."),
      ("林间光束", "场景 · 中景 · 缓推",
       "Ghibli inspired forest with god rays through leaves, fireflies drifting, slow push in through ferns. 16:9, 5 seconds."),
     ]),
    ("cgi-pixar", "3D 卡通", "style-3d.png",
     "Stylized 3D CGI, Pixar-like design, soft cinematic lighting.",
     "ai-video-skills/cgi-pixar",
     [
      ("3D 角色出场", "角色 · 中景 · 弧线推进",
       "Stylized 3D CGI Pixar-like animation. A cute round character in a red coat steps into a rain-wet neon street at night. Camera arcs in, medium shot, glossy reflections. 16:9, 5 seconds."),
      ("产品 3D 演示", "产品 · 特写 · 环绕",
       "High-quality 3D CGI product animation, matte black headphones on dark reflective floor, camera orbits slowly, studio softboxes. 1:1, 4 seconds."),
      ("欢乐群像", "群体 · 全景 · 摇镜",
       "Pixar-like 3D ensemble of colorful characters waving in a bright town square, pan left to right, sunny cheerful lighting. 16:9, 5 seconds."),
     ]),
    ("cyberpunk-neon", "赛博朋克", "style-cyberpunk.png",
     "Cyberpunk neon night, wet streets, cyan magenta palette.",
     "ai-video-skills/cyberpunk-neon",
     [
      ("霓虹巷推进", "人物 · 中近景 · 推进",
       "Cyberpunk photorealistic night, young woman in a red coat walking through a dense neon alley in the rain. Slow dolly in, medium close-up. Magenta and cyan neon, wet asphalt, steam vents, holographic ads without readable text. 16:9, 5 seconds."),
      ("未来天际线", "空镜 · 大远景 · 航拍",
       "Cyberpunk city skyline at night in rain, flying vehicles leaving light trails, extreme wide aerial establishing shot. 21:9, 5 seconds."),
      ("FPV 穿街", "动作 · FPV · 高速",
       "FPV drone flying at high speed through a cyberpunk neon alley at night, tilted horizon, light streaks, rain. 16:9, 4 seconds."),
     ]),
    ("film-noir", "黑色电影", "tpl-noir-detective.png",
     "Film noir B&W, hard chiaroscuro, venetian shadows, grain.",
     "ai-video-skills/film-noir",
     [
      ("雨夜侦探", "人物 · 中景 · 缓推",
       "Film noir black and white. A detective in a trench coat and hat stands under a streetlamp in a rainy alley at night. Slow push in, medium shot, hard chiaroscuro shadows, 35mm grain. 16:9, 5 seconds."),
      ("百叶窗室内", "室内 · 中近景 · 固定",
       "Film noir interior, hard light through venetian blinds on a tense face, cigarette smoke, low-key B&W, locked-off MCU. 16:9, 4 seconds."),
      ("空巷拉远", "空镜 · 全景 · 拉远",
       "Film noir empty wet alley at night, single streetlamp, slow pull back revealing long shadows, B&W grain. 16:9, 5 seconds."),
     ]),
    ("chinese-ink", "中国水墨", "tpl-ink-mountain.png",
     "Chinese ink wash, sumi-e strokes, misty mountains, negative space.",
     "ai-video-skills/chinese-ink",
     [
      ("水墨行旅", "人物 · 远景 · 横移",
       "Traditional Chinese ink wash animation. A lone traveler on a mountain path in mist. Slow lateral tracking, wide shot, sumi-e brushwork, vast negative space, vermilion accent. 16:9, 6 seconds."),
      ("山水显形", "空镜 · 缓显 · 雾动",
       "Chinese ink wash painting comes alive, mist drifting across layered mountain silhouettes, ink blooming on paper texture, static camera. 16:9, 6 seconds."),
      ("水墨飞鸟", "元素 · 固定",
       "Sumi-e style, a single ink-brush bird flies across white space, wet ink trails, minimal composition. 1:1, 4 seconds."),
     ]),
    ("oil-painting", "油画艺术", "style-oil.png",
     "Oil painting, impasto brushwork, impressionist light.",
     "ai-video-skills/oil-painting",
     [
      ("油画人物夜巷", "人物 · 中景 · 缓推",
       "Oil painting style, thick impasto brushwork. A woman in a red coat in a rain-lit alley at night, neon colors melted into painterly strokes. Slow push in, medium shot. 16:9, 5 seconds."),
      ("印象派风景", "空镜 · 远景 · 摇镜",
       "Impressionist oil painting landscape at dusk, loose brush strokes, slow pan left, canvas texture. 16:9, 5 seconds."),
      ("静物油画", "产品 · 特写 · 固定",
       "Oil painting still life, fruit and ceramic on a table, dramatic side light, impasto highlights. 4:3, 4 seconds."),
     ]),
    ("product-commercial", "产品广告", "tpl-product-watch.png",
     "Premium product commercial, studio light, luxury grade.",
     "ai-video-skills/product-commercial",
     [
      ("腕表环绕", "产品 · 特写 · 环绕",
       "Premium product commercial, photorealistic. Elegant wristwatch on dark reflective stone. Slow orbit, close-up, low angle. Soft key + cool rim, black and gold grade. No text on dial. 1:1, 4 seconds."),
      ("耳机开箱氛围", "产品 · 中近景 · 推进",
       "Luxury headphone product film, matte black headphones on wet black surface, subtle neon reflections, slow dolly in, shallow DOF. 16:9, 4 seconds."),
      ("悬浮产品", "产品 · 固定 · 微动",
       "Product floating in dark studio, soft gradient background, gentle object rotation, specular highlights, premium CGI packshot. 9:16, 4 seconds."),
     ]),
    ("food-macro", "美食微距", "tpl-food-macro.png",
     "Food commercial macro, warm appetizing light, steam, gloss.",
     "ai-video-skills/food-macro",
     [
      ("汤面拉丝", "美食 · 大特写 · 上移",
       "Cinematic food commercial macro, steaming noodle bowl, chopsticks lifting glossy noodles, steam rising, warm light, slow tilt up. 9:16, 4 seconds."),
      ("煎锅火焰", "美食 · 特写 · 微晃",
       "Photorealistic food shot, chef searing steak, flame burst, sizzling juices, warm kitchen light, handheld slight shake. 16:9, 4 seconds."),
      ("甜品剖面", "美食 · 特写 · 刀切",
       "Macro dessert commercial, knife slicing layered chocolate cake, glossy ganache, soft studio light, slow precise motion. 1:1, 4 seconds."),
     ]),
    ("aerial-travel", "航拍风光", "tpl-aerial-coast.png",
     "Cinematic aerial travel, epic landscape, drone footage.",
     "ai-video-skills/aerial-travel",
     [
      ("海岸线航拍", "风光 · 大远景 · 前推",
       "Cinematic aerial drone shot of turquoise coastline, waves meeting golden cliffs, golden hour, slow forward flight. 16:9, 6 seconds."),
      ("城市鸟瞰夜", "城市 · 鸟瞰 · 缓降",
       "Aerial night drone footage over a dense city, glowing street grid, slow descent, light haze. 16:9, 5 seconds."),
      ("山脊掠过", "风光 · 高速掠过",
       "Drone flying fast along a mountain ridge at sunrise, light breaking over peaks, dynamic speed. 16:9, 5 seconds."),
     ]),
    ("horror-atmosphere", "恐怖氛围", "tpl-horror.png",
     "Horror atmosphere, flickering light, fog, desaturated dread.",
     "ai-video-skills/horror-atmosphere",
     [
      ("废弃医院走廊", "场景 · 中景 · 前移",
       "Cinematic horror atmosphere, abandoned hospital corridor at night, flickering fluorescent lights, fog, slow steadicam push forward, desaturated grade. 16:9, 6 seconds."),
      ("门缝底光", "特写 · 固定微推",
       "Light leaking under a closed door in darkness, dust in beam, subtle camera creep in, tense silence. 21:9, 5 seconds."),
      ("回头惊悚", "人物 · 中近景 · 手持",
       "Handheld horror shot, person in dark hallway slowly looking over shoulder, underlight flicker, grain. 16:9, 4 seconds."),
     ]),
    ("sports-fpv", "运动 FPV", "tpl-sports-fpv.png",
     "Action sports energy, FPV speed, motion streaks.",
     "ai-video-skills/sports-fpv",
     [
      ("城市峡谷俯冲", "FPV · 高速 · 俯冲",
       "FPV drone diving through a neon city canyon at night at high speed, tilted horizon, light streaks, rain mist. 16:9, 4 seconds."),
      ("滑板跟拍", "运动 · 侧跟 · 低角度",
       "Low-angle tracking shot following a skateboarder in a sunlit skatepark, smooth gimbal, dust particles. 16:9, 5 seconds."),
      ("跑酷飞跃", "动作 · 升格 · 弧线",
       "Slow-motion parkour leap between rooftops, camera arcs around mid-air pose, golden hour rim light. 16:9, 4 seconds."),
     ]),
    ("sci-fi-space", "科幻太空", "tpl-sci-fi.png",
     "Photorealistic sci-fi, spaceship interiors, teal light, vistas.",
     "ai-video-skills/sci-fi-space",
     [
      ("舷窗星球", "场景 · 中景 · 缓推",
       "Photorealistic sci-fi spaceship interior looking out a large viewport at a glowing planet, cool teal lighting, holographic panels abstract UI no readable text, slow push toward the glass. 21:9, 6 seconds."),
      ("走廊警报", "场景 · 前移 · 红光",
       "Sci-fi corridor with red alert lighting, steam vents, slow forward move, photorealistic hard-surface design. 16:9, 5 seconds."),
      ("太空建立", "空镜 · 大远景 · 漂移",
       "Epic space establishing shot, starship drifting above a ringed planet, slow lateral drift, volumetric sun flare. 21:9, 6 seconds."),
     ]),
    ("flat-motion-graphics", "扁平动态图形", "tpl-flat-graphic.png",
     "Flat vector motion graphics, geometric, limited palette.",
     "ai-video-skills/flat-motion-graphics",
     [
      ("扁平城市说明", "图形 · 元素入场",
       "Flat vector motion graphics, geometric city skyline, simple icons sliding in, teal orange cream palette, smooth UI motion, no readable text. 16:9, 5 seconds."),
      ("图标流程动画", "信息 · 元素弹入",
       "Flat motion graphics, abstract nodes and arrows connecting with spring motion, minimal background. 1:1, 4 seconds."),
      ("扁平人物行走", "角色 · 侧面 · 循环",
       "Flat 2D vector character walking loop in side view, simple shapes, consistent stroke, seamless loop. 16:9, 4 seconds."),
     ]),
    ("claymation", "黏土定格", "style-clay.png",
     "Stop-motion claymation, handmade textures, miniature sets.",
     "ai-video-skills/claymation",
     [
      ("雨巷黏土人物", "角色 · 中景 · 缓推",
       "Stop-motion claymation, handmade clay character in a red coat on a miniature rainy neon alley set, slow push in, soft practical lights, shallow macro focus. 16:9, 5 seconds."),
      ("微缩小镇建立", "空镜 · 全景 · 横摇",
       "Miniature claymation town diorama, tiny houses and lamps, slow pan across the set, warm tabletop lighting. 16:9, 5 seconds."),
      ("黏土手部动作", "特写 · 固定",
       "Close-up claymation, clay hands placing a tiny object on a miniature table, macro DOF. 1:1, 4 seconds."),
     ]),
]

def esc(t):
    return (t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))

parts = []
parts.append('''      <!-- Template gallery -->
      <section class="section" id="tpl-gallery">
        <div class="section-head">
          <div class="section-num">模</div>
          <div>
            <h2>提示词模板库</h2>
            <span class="en">Style Templates · Scene Packs · Skills</span>
          </div>
        </div>
        <p class="intro">
          不同风格 × 不同画面的可复制提示词模板，每条都配有演示图。每个风格已落地为项目内一套 skill：
          可读包在 <span class="mono">ai-video-skills/&lt;风格ID&gt;/</span>，可加载技能在
          <span class="mono">.claude/skills/&lt;风格ID&gt;/</span>（含 SKILL.md 与 locales）。新开对话后技能列表可发现。
        </p>
        <div class="note">
          用法：复制风格锁定词 + 某一条画面模板 → 只改本镜头的动作/运镜/景别 → 人物与场景锁定词保持逐字一致。
          更多取值见 <a href="#keywords">关键字字典</a>；运镜动画见 <a href="#camera">01 运镜</a>。
        </div>
''')

for sid, name, demo, lock, skill_path, tpls in TEMPLATES:
    t_html = []
    for title, scene, prompt in tpls:
        t_html.append(f'''
            <div class="tpl-item">
              <div class="tpl-item-head">
                <h4>{esc(title)}</h4>
                <span class="scene">{esc(scene)}</span>
              </div>
              <div class="prompt-box">
                <button class="copy-btn" type="button">复制</button>
                <div class="prompt-text">{esc(prompt)}</div>
              </div>
            </div>''')
    parts.append(f'''
        <article class="tpl-block" id="tpl-{sid}">
          <div class="tpl-media">
            <img src="assets/{demo}" alt="{esc(name)}模板演示图" loading="lazy" />
          </div>
          <div class="tpl-body">
            <div class="tpl-title-row">
              <h3>{esc(name)}</h3>
              <span class="kw-key mono">{esc(sid)}</span>
            </div>
            <p class="tpl-lock"><strong>风格锁定：</strong><span class="mono">{esc(lock)}</span></p>
            <p class="tpl-skill">Skill：<span class="mono">{esc(skill_path)}/</span> · 演示图：<span class="mono">assets/{demo}</span></p>
            <div class="tpl-list">
              {''.join(t_html)}
            </div>
          </div>
        </article>''')

parts.append('''
        <div class="note" style="margin-top:8px">
          完整 skill 文档（触发说明、避坑、工作流）见各风格文件夹内 <span class="mono">SKILL.md</span>；
          索引见 <span class="mono">ai-video-skills/README.md</span>。
        </div>
      </section>
''')

fragment = "".join(parts)

# insert TOC
if 'href="#tpl-gallery"' not in html:
    html = html.replace(
        '<a href="#keywords"><span class="num">字</span>关键字字典</a>',
        '<a href="#keywords"><span class="num">字</span>关键字字典</a>\n        <a href="#tpl-gallery"><span class="num">模</span>提示词模板库</a>',
        1,
    )

# insert section after keywords section end, before camera
marker = '      <!-- 01 Camera -->'
if marker not in html:
    raise SystemExit("marker not found")
if 'id="tpl-gallery"' not in html:
    html = html.replace(marker, fragment + "\n" + marker, 1)
else:
    print("gallery already present")

html_path.write_text(html, encoding="utf-8")
print("html_updated", html_path.stat().st_size)
