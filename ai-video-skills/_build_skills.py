# -*- coding: utf-8 -*-
"""Generate AI video prompt skill packs for the project."""
from pathlib import Path
import json
import shutil

ROOT = Path(r"D:\ai_desktop_project\xiaomi")
PACK = ROOT / "ai-video-skills"
CLAUDE = ROOT / ".claude" / "skills"
ASSETS = ROOT / "assets"

# id, displayName, brief, description, demo file, locked style block, templates[(title, scene, prompt)]
SKILLS = [
    {
        "id": "cinematic-realism",
        "displayName": "电影写实视频",
        "brief": "写实电影感人物与剧情镜头的提示词模板",
        "description": "Use when the user asks for photorealistic cinematic AI video prompts, film-look shots, dramatic character scenes, or 35mm movie-style video generation.",
        "demo": "style-photoreal.png",
        "style_lock": "Cinematic photorealistic, 35mm film look, shallow depth of field, subtle film grain, natural skin tones.",
        "keywords": ["cinematic photorealistic", "35mm film", "teal and orange", "shallow DOF", "rim light"],
        "donts": ["不要同时写 cartoon 与 photorealistic", "避免一镜头堆多个运镜", "文字/logo 交给后期"],
        "templates": [
            ("雨夜人物推进", "人物 · 中近景 · 推进",
             "Cinematic photorealistic, 35mm film look. A 25-year-old woman in a red wool coat walks slowly through a rainy neon alley in Tokyo at night. Slow dolly in, medium close-up, eye level. Wet asphalt reflects cyan and orange neon. Rim light from behind, soft fill on face. Teal and orange grade, shallow DOF. 16:9, 5 seconds."),
            ("城市建立镜头", "空镜 · 大远景 · 航拍缓推",
             "Cinematic photorealistic establishing shot of a rainy neon city at night, extreme wide aerial view, slow push in toward a glowing alley, volumetric haze, teal and orange grade, 35mm film grain. 16:9, 5 seconds."),
            ("对话过肩", "双人 · 过肩 · 固定",
             "Cinematic photorealistic film still, over-the-shoulder shot in a dim cafe at night, rain on windows, woman in red coat listening, warm practical lamps, shallow DOF, natural skin tones. Locked-off camera, medium close-up. 16:9, 4 seconds."),
        ],
    },
    {
        "id": "anime-cel",
        "displayName": "日式动画视频",
        "brief": "赛璐璐日式动画角色与校园/都市场景模板",
        "description": "Use when the user wants Japanese anime cel-style AI video prompts, school rooftop scenes, anime city night, or clean line-art animation videos.",
        "demo": "tpl-anime-school.png",
        "style_lock": "Japanese anime cel animation, clean line art, painted background, soft glow highlights, vibrant but controlled colors.",
        "keywords": ["anime cel style", "painted background", "Makoto Shinkai inspired", "clean line art"],
        "donts": ["避免 photorealistic 皮肤词", "不要过度写实景深", "口型台词慎用"],
        "templates": [
            ("天台少女 · 夕阳", "人物 · 中景 · 缓慢环绕",
             "Japanese anime cel style. A high school girl in uniform stands on the rooftop at sunset, cherry blossoms drifting, wind in her hair. Slow orbit shot, medium shot, warm golden sky with dramatic clouds, clean line art, painterly background. 16:9, 5 seconds."),
            ("雨夜动画街", "场景 · 中景 · 跟随",
             "Anime cel style city street at night in rain, neon signs reflecting on wet ground, a girl with umbrella walking away. Camera follows from behind, medium shot, soft light blooms, painted background. 16:9, 5 seconds."),
            ("大特写眼神", "特写 · 固定",
             "Anime cel style extreme close-up of a girl's eyes reflecting city lights, subtle emotional blink, clean lines, soft shading, shallow glow. Static shot. 16:9, 3 seconds."),
        ],
    },
    {
        "id": "ghibli-painterly",
        "displayName": "吉卜力手绘视频",
        "brief": "吉卜力式手绘自然风光与童话场景模板",
        "description": "Use when the user asks for Ghibli-inspired painterly anime video prompts, whimsical nature scenes, rolling hills, or soft magical backgrounds.",
        "demo": "tpl-ghibli-hill.png",
        "style_lock": "Studio Ghibli inspired painterly anime, lush hand-painted nature, soft magical light, whimsical atmosphere, detailed clouds.",
        "keywords": ["Ghibli inspired", "painterly", "whimsical", "hand-painted background"],
        "donts": ["避免硬科幻机械词", "不要高反差硬光", "保持色彩柔和"],
        "templates": [
            ("风吹山丘", "空镜 · 远景 · 横摇",
             "Ghibli inspired painterly anime. Vast green rolling hills under towering clouds, wind blowing through grass and wildflowers. Slow pan right, wide shot, soft volumetric light, whimsical nature, hand-painted background. 16:9, 6 seconds."),
            ("山丘上的红衣", "人物 · 全景 · 拉远",
             "Ghibli inspired painterly anime, a small girl in a red dress standing on a green hill, camera slowly pulls back to reveal endless sky and clouds, soft golden light, magical calm mood. 16:9, 5 seconds."),
            ("林间光束", "场景 · 中景 · 缓推",
             "Ghibli inspired forest with god rays through leaves, fireflies drifting, painterly details, slow push in through ferns, peaceful magical atmosphere. 16:9, 5 seconds."),
        ],
    },
    {
        "id": "cgi-pixar",
        "displayName": "3D卡通视频",
        "brief": "皮克斯式 3D 角色与商业动画模板",
        "description": "Use when the user wants Pixar-like or stylized 3D CGI AI video prompts, cute character animation, or polished 3D commercial animation.",
        "demo": "style-3d.png",
        "style_lock": "Stylized 3D CGI animation, Pixar-like character design, soft subsurface skin, glossy materials, cinematic lighting.",
        "keywords": ["stylized 3D CGI", "Pixar-like", "subsurface scattering", "polished render"],
        "donts": ["避免 gritty realistic dirt 过量", "不要真人皮肤纹理词", "角色保持圆润可爱比例"],
        "templates": [
            ("3D 角色出场", "角色 · 中景 · 弧线推进",
             "Stylized 3D CGI Pixar-like animation. A cute round character in a red coat steps into a rain-wet neon street at night. Camera arcs in, medium shot, glossy reflections, soft cinematic lighting, appealing design. 16:9, 5 seconds."),
            ("产品 3D 演示", "产品 · 特写 · 环绕",
             "High-quality 3D CGI product animation, matte black headphones floating on dark reflective floor, camera orbits slowly, studio softboxes, clean commercial look. 1:1, 4 seconds."),
            ("欢乐群像", "群体 · 全景 · 摇镜",
             "Pixar-like 3D ensemble of colorful characters waving in a bright stylized town square, pan left to right, sunny cheerful lighting, polished render. 16:9, 5 seconds."),
        ],
    },
    {
        "id": "cyberpunk-neon",
        "displayName": "赛博朋克视频",
        "brief": "霓虹未来都市与赛博角色镜头模板",
        "description": "Use when the user wants cyberpunk AI video prompts, neon city night shots, rainy futuristic alleys, or high-tech noir atmosphere.",
        "demo": "style-cyberpunk.png",
        "style_lock": "Cyberpunk concept art photoreal hybrid, dense neon signage, wet reflective streets, magenta cyan palette, futuristic clutter.",
        "keywords": ["cyberpunk", "neon signs", "wet streets", "cyan magenta", "holographic"],
        "donts": ["避免过亮白昼", "不要田园/吉卜力词", "文字招牌写 no legible text"],
        "templates": [
            ("霓虹巷推进", "人物 · 中近景 · 推进",
             "Cyberpunk photorealistic night, young woman in a red coat walking through a dense neon alley in the rain. Slow dolly in, medium close-up. Magenta and cyan neon, wet reflective asphalt, steam vents, holographic ads without readable text. 16:9, 5 seconds."),
            ("未来天际线", "空镜 · 大远景 · 航拍",
             "Cyberpunk city skyline at night in rain, flying vehicles leaving light trails, extreme wide aerial establishing shot, slow drift forward, neon grid below. 21:9, 5 seconds."),
            ("FPV 穿街", "动作 · FPV · 高速",
             "FPV drone flying at high speed through a cyberpunk neon alley at night, tilted horizon, light streaks, rain, immersive first-person flight. 16:9, 4 seconds."),
        ],
    },
    {
        "id": "film-noir",
        "displayName": "黑色电影视频",
        "brief": "黑白高反差侦探与雨夜悬疑模板",
        "description": "Use when the user wants film noir AI video prompts, black-and-white detective scenes, hard chiaroscuro lighting, or classic mystery mood.",
        "demo": "tpl-noir-detective.png",
        "style_lock": "Film noir, black and white, hard chiaroscuro lighting, 35mm grain, venetian blind shadows, mysterious mood.",
        "keywords": ["film noir", "black and white", "chiaroscuro", "venetian shadows", "grain"],
        "donts": ["避免高饱和霓虹彩", "不要欢快情绪词", "保持低照度"],
        "templates": [
            ("雨夜侦探", "人物 · 中景 · 缓推",
             "Film noir black and white. A detective in a trench coat and hat stands under a streetlamp in a rainy alley at night. Slow push in, medium shot, hard chiaroscuro shadows, 35mm grain, mysterious mood. 16:9, 5 seconds."),
            ("百叶窗室内", "室内 · 中近景 · 固定",
             "Film noir interior, hard light through venetian blinds casting stripes on a tense face, cigarette smoke curling, low-key black and white, locked-off medium close-up. 16:9, 4 seconds."),
            ("空巷拉远", "空镜 · 全景 · 拉远",
             "Film noir empty wet alley at night, single streetlamp, camera slowly pulls back to reveal long shadows, black and white, grain, lonely atmosphere. 16:9, 5 seconds."),
        ],
    },
    {
        "id": "chinese-ink",
        "displayName": "中国水墨视频",
        "brief": "水墨山水、留白与朱砂点缀动画模板",
        "description": "Use when the user wants Chinese ink wash, sumi-e, traditional guofeng, or minimalist ink animation AI video prompts.",
        "demo": "tpl-ink-mountain.png",
        "style_lock": "Traditional Chinese ink wash painting, sumi-e brush strokes, misty mountains, sparse negative space, subtle vermilion accent.",
        "keywords": ["Chinese ink wash", "sumi-e", "misty mountains", "negative space", "vermilion accent"],
        "donts": ["避免赛博霓虹", "不要厚涂油画笔触", "色彩克制，仅朱砂点缀"],
        "templates": [
            ("水墨行旅", "人物 · 远景 · 横移",
             "Traditional Chinese ink wash animation. A lone traveler walks on a mountain path in mist. Slow lateral tracking, wide shot, sumi-e brushwork, vast negative space, single vermilion accent on the figure. 16:9, 6 seconds."),
            ("山水显形", "空镜 · 缓显 · 固定+雾动",
             "Chinese ink wash painting comes alive, mist drifting across layered mountain silhouettes, ink gradients blooming on paper texture, static camera, meditative pace. 16:9, 6 seconds."),
            ("水墨飞鸟", "特写元素 · 固定",
             "Sumi-e style, a single ink-brush bird flies across white space, wet ink trails, minimal composition, elegant traditional aesthetic. 1:1, 4 seconds."),
        ],
    },
    {
        "id": "oil-painting",
        "displayName": "油画艺术视频",
        "brief": "厚涂油画与印象派光影镜头模板",
        "description": "Use when the user wants oil painting, impasto, impressionist, or fine-art painterly AI video prompts.",
        "demo": "style-oil.png",
        "style_lock": "Oil painting style, thick impasto brushwork, visible palette knife texture, rich pigment mixing, impressionist light.",
        "keywords": ["oil painting", "impasto", "impressionist", "palette knife", "brushwork"],
        "donts": ["避免光滑 3D 塑料感", "不要锐利数码噪点", "保持笔触可见"],
        "templates": [
            ("油画人物夜巷", "人物 · 中景 · 缓推",
             "Oil painting style, thick impasto brushwork. A woman in a red coat in a rain-lit alley at night, neon colors melted into painterly strokes. Slow push in, medium shot, impressionist night atmosphere. 16:9, 5 seconds."),
            ("印象派风景", "空镜 · 远景 · 摇镜",
             "Impressionist oil painting landscape at dusk, loose brush strokes of sky and water, slow pan left, rich color mixing, canvas texture visible. 16:9, 5 seconds."),
            ("静物油画", "产品 · 特写 · 固定",
             "Oil painting still life, fruit and ceramic on a table, dramatic side light, impasto highlights, classical composition, static shot. 4:3, 4 seconds."),
        ],
    },
    {
        "id": "product-commercial",
        "displayName": "产品广告视频",
        "brief": "高端产品商业广告与棚拍镜头模板",
        "description": "Use when the user wants product commercial AI video prompts, packshots, luxury watches, headphones, or studio product films.",
        "demo": "tpl-product-watch.png",
        "style_lock": "Premium product commercial, photorealistic CGI or studio photography, controlled highlights, deep blacks, luxury grade.",
        "keywords": ["product commercial", "studio lighting", "packshot", "reflective surface", "luxury"],
        "donts": ["避免杂乱背景杂物", "不要人脸抢主体", "logo/文字默认关闭"],
        "templates": [
            ("腕表环绕", "产品 · 特写 · 环绕",
             "Premium product commercial, photorealistic. An elegant wristwatch on dark reflective stone. Camera slowly orbits, close-up, low angle. Soft key light with cool rim highlight, black and gold grade, macro details. No text on dial. 1:1, 4 seconds."),
            ("耳机开箱氛围", "产品 · 中近景 · 推进",
             "Luxury headphone product film, matte black headphones on wet black surface with subtle neon reflections, slow dolly in, shallow DOF, cinematic commercial lighting. 16:9, 4 seconds."),
            ("悬浮产品", "产品 · 固定 · 微动",
             "Product floating in dark studio, soft gradient background, gentle rotation of object only, specular highlights sweeping, premium CGI packshot. 9:16, 4 seconds."),
        ],
    },
    {
        "id": "food-macro",
        "displayName": "美食微距视频",
        "brief": "食欲感美食特写与蒸汽微距模板",
        "description": "Use when the user wants food commercial AI video prompts, macro food shots, steaming dishes, or appetizing restaurant videos.",
        "demo": "tpl-food-macro.png",
        "style_lock": "Cinematic food commercial, photorealistic macro, warm appetizing light, glossy textures, steam and moisture detail.",
        "keywords": ["food commercial", "macro", "steam", "glossy", "appetizing warm light"],
        "donts": ["避免冷蓝主调", "不要怪异食物变形", "手部若出现需稳定"],
        "templates": [
            ("汤面拉丝", "美食 · 大特写 · 缓慢上移",
             "Cinematic food commercial macro shot, steaming noodle bowl, chopsticks lifting glossy noodles, broth steam rising, warm appetizing light, extreme close-up texture, slow tilt up. 9:16, 4 seconds."),
            ("煎锅火焰", "美食 · 特写 · 固定微晃",
             "Photorealistic food shot, chef searing steak in a pan, flame burst, sizzling juices, warm kitchen light, handheld slight shake, macro detail. 16:9, 4 seconds."),
            ("甜品剖面", "美食 · 特写 · 刀切",
             "Macro dessert commercial, knife slicing a layered chocolate cake, glossy ganache, soft studio light, shallow DOF, slow precise motion. 1:1, 4 seconds."),
        ],
    },
    {
        "id": "aerial-travel",
        "displayName": "航拍风光视频",
        "brief": "旅行航拍、海岸与城市建立镜头模板",
        "description": "Use when the user wants aerial travel AI video prompts, drone landscape shots, coastline, or epic establishing footage.",
        "demo": "tpl-aerial-coast.png",
        "style_lock": "Cinematic aerial travel photography, photorealistic drone footage, golden hour or clean daylight, epic scale.",
        "keywords": ["aerial drone shot", "establishing", "golden hour", "epic landscape", "bird's-eye"],
        "donts": ["避免镜头内过多小人脸", "不要文本标注", "比例感要靠地标"],
        "templates": [
            ("海岸线航拍", "风光 · 大远景 · 前推",
             "Cinematic aerial drone shot of turquoise coastline, waves meeting golden cliffs, golden hour light, slow forward flight, epic travel establishing shot, photorealistic. 16:9, 6 seconds."),
            ("城市鸟瞰夜", "城市 · 鸟瞰 · 缓降",
             "Aerial night drone footage over a dense city, glowing street grid, slow descending move, light haze, cinematic travel film look. 16:9, 5 seconds."),
            ("山脊掠过", "风光 · FPV/掠过",
             "Drone flying fast along a mountain ridge at sunrise, light breaking over peaks, dynamic speed, photorealistic aerial adventure. 16:9, 5 seconds."),
        ],
    },
    {
        "id": "horror-atmosphere",
        "displayName": "恐怖氛围视频",
        "brief": "废弃空间、底光与悬疑惊悚镜头模板",
        "description": "Use when the user wants horror AI video prompts, abandoned places, suspense atmosphere, dark corridors, or thriller mood videos.",
        "demo": "tpl-horror.png",
        "style_lock": "Cinematic horror atmosphere, photorealistic dark spaces, flickering practical lights, fog, dread mood, desaturated grade.",
        "keywords": ["horror atmosphere", "flickering light", "abandoned", "fog", "low-key"],
        "donts": ["避免明亮高调广告光", "不要卡通可爱角色", "血腥写实要谨慎/可关闭"],
        "templates": [
            ("废弃医院走廊", "场景 · 中景 · 缓慢前移",
             "Cinematic horror atmosphere, abandoned hospital corridor at night, flickering fluorescent lights, fog, slow steadicam push forward, desaturated grade, dread mood, photorealistic. 16:9, 6 seconds."),
            ("门缝底光", "特写 · 固定",
             "Horror still-frame motion, light leaking under a closed door in darkness, dust in beam, subtle camera creep in, tense silence mood. 21:9, 5 seconds."),
            ("回头惊悚", "人物 · 中近景 · 手持",
             "Handheld horror shot, person in dark hallway slowly looking over shoulder, underlight flicker, grain, shallow DOF, suspenseful. 16:9, 4 seconds."),
        ],
    },
    {
        "id": "sports-fpv",
        "displayName": "运动FPV视频",
        "brief": "极限运动、穿越机与高速跟拍模板",
        "description": "Use when the user wants sports AI video prompts, FPV drone racing, extreme sports, high-speed chase, or dynamic action camera footage.",
        "demo": "tpl-sports-fpv.png",
        "style_lock": "Cinematic action sports, high-energy FPV or gimbal follow, motion blur streaks, vivid but clean grade.",
        "keywords": ["FPV drone", "high speed", "action sports", "motion blur", "first person"],
        "donts": ["避免静止锁死机位", "不要过多慢动作堆叠", "路径写清空间"],
        "templates": [
            ("城市峡谷俯冲", "FPV · 高速 · 俯冲",
             "FPV drone diving through a neon city canyon at night at high speed, tilted horizon, light streaks, rain mist, cinematic action sports energy. 16:9, 4 seconds."),
            ("滑板跟拍", "运动 · 侧跟 · 低角度",
             "Low-angle tracking shot following a skateboarder through a sunlit skatepark, smooth gimbal motion, dust particles, energetic sports film look. 16:9, 5 seconds."),
            ("跑酷飞跃", "动作 · 升格 · 弧线",
             "Slow-motion action shot, athlete parkour leap between rooftops, camera arcs around mid-air pose, golden hour rim light, epic sports commercial. 16:9, 4 seconds."),
        ],
    },
    {
        "id": "sci-fi-space",
        "displayName": "科幻太空视频",
        "brief": "飞船舱内、星球舷窗与未来科技模板",
        "description": "Use when the user wants sci-fi AI video prompts, spaceship interiors, space vistas, holograms, or futuristic technology videos.",
        "demo": "tpl-sci-fi.png",
        "style_lock": "Photorealistic sci-fi cinema, sleek spacecraft interiors, cool teal lighting, holographic UI without readable text, vast space vistas.",
        "keywords": ["sci-fi", "spaceship interior", "holographic", "planet vista", "teal lighting"],
        "donts": ["避免中世纪奇幻词", "不要可读乱码 UI 文字", "保持科技材质干净"],
        "templates": [
            ("舷窗星球", "场景 · 中景 · 缓推",
             "Photorealistic sci-fi spaceship interior looking out a large viewport at a glowing planet, cool teal lighting, holographic panels with abstract UI no readable text, slow push toward the glass. 21:9, 6 seconds."),
            ("走廊警报", "场景 · 前移 · 红光",
             "Sci-fi corridor with red alert lighting, steam vents, slow camera move forward, cinematic tension, photorealistic hard-surface design. 16:9, 5 seconds."),
            ("太空建立", "空镜 · 大远景 · 漂移",
             "Epic space establishing shot, starship drifting above a ringed planet, slow lateral drift, volumetric sun flare, photorealistic sci-fi. 21:9, 6 seconds."),
        ],
    },
    {
        "id": "flat-motion-graphics",
        "displayName": "扁平动态图形",
        "brief": "扁平插画信息动画与说明类视频模板",
        "description": "Use when the user wants flat illustration, motion graphics, explainer video, infographic animation, or clean vector AI video prompts.",
        "demo": "tpl-flat-graphic.png",
        "style_lock": "Flat vector motion graphics, bold geometric shapes, limited palette, clean edges, modern explainer video style, no legible text baked in.",
        "keywords": ["flat vector", "motion graphics", "explainer", "geometric", "limited palette"],
        "donts": ["避免写实景深/胶片颗粒", "不要复杂笔触", "画面文字后期叠加"],
        "templates": [
            ("扁平城市说明", "图形 · 中景 · 元素入场",
             "Flat vector motion graphics, clean geometric city skyline, simple character icons sliding into frame, bold teal orange cream palette, smooth UI-like motion, no readable text. 16:9, 5 seconds."),
            ("图标流程动画", "信息 · 固定 · 元素弹入",
             "Flat motion graphics sequence, abstract nodes and arrows connecting with bouncy spring motion, minimal background, modern tech explainer style, no text. 1:1, 4 seconds."),
            ("扁平人物行走", "角色 · 侧面 · 循环",
             "Flat 2D vector character walking loop in side view, simple shapes, consistent stroke weight, soft color blocks, seamless loop. 16:9, 4 seconds."),
        ],
    },
    {
        "id": "claymation",
        "displayName": "黏土定格视频",
        "brief": "黏土玩偶微缩布景与定格动画模板",
        "description": "Use when the user wants claymation, stop-motion, miniature diorama, or handmade toy-style AI video prompts.",
        "demo": "style-clay.png",
        "style_lock": "Stop-motion claymation, handmade clay textures, practical miniature set, soft toy-like lighting, shallow macro focus.",
        "keywords": ["claymation", "stop motion", "miniature", "handmade", "macro shallow focus"],
        "donts": ["避免光滑工业 CGI", "不要超写实人类皮肤", "保持玩偶比例"],
        "templates": [
            ("雨巷黏土人物", "角色 · 中景 · 缓推",
             "Stop-motion claymation, handmade clay character in a red coat on a miniature rainy neon alley set, slow push in, soft practical lights, shallow macro focus, tactile textures. 16:9, 5 seconds."),
            ("微缩小镇建立", "空镜 · 全景 · 横摇",
             "Miniature claymation town diorama, tiny houses and street lamps, slow pan across the set, warm tabletop lighting, handmade charm. 16:9, 5 seconds."),
            ("黏土手部动作", "特写 · 固定",
             "Close-up claymation shot, clay hands carefully placing a tiny object on a miniature table, macro depth of field, stop-motion warmth. 1:1, 4 seconds."),
        ],
    },
]


def skill_md(s: dict) -> str:
    lines = [
        "---",
        f"name: {s['id']}",
        f"description: {s['description']}",
        "---",
        "",
        f"# {s['displayName']}",
        "",
        s["brief"] + "。",
        "",
        "## 何时使用",
        f"- 用户要做 **{s['displayName']}** 风格的 AI 视频提示词/分镜/成片文案时使用。",
        "- 需要锁定该风格的镜头模板、取值词与避坑清单时使用。",
        "",
        "## 风格锁定词（放 prompt 最前，多镜头逐字复用）",
        "",
        s["style_lock"],
        "",
        "## 核心关键字取值",
        "",
        ", ".join(f"`{k}`" for k in s["keywords"]),
        "",
        "## 避坑",
        "",
        *[f"- {d}" for d in s["donts"]],
        "",
        "## 提示词模板（含演示图）",
        "",
        f"演示图：`assets/{s['demo']}`（项目根目录）",
        "",
    ]
    for title, scene, prompt in s["templates"]:
        lines += [
            f"### {title}",
            "",
            f"- 画面类型：{scene}",
            f"- 演示图：`assets/{s['demo']}`",
            "",
            "```text",
            prompt,
            "```",
            "",
        ]
    lines += [
        "## 推荐工作流",
        "",
        "1. 复制风格锁定词 + 一条模板 prompt",
        "2. 只改本镜头的「主体动作 / 运镜 / 景别」",
        "3. 人物与场景卡保持逐字一致",
        "4. 负面提示：`blurry, deformed hands, watermark, text, flickering, morphing`",
        "",
        "## 相关",
        "",
        "- 项目模板库页面：`index.html` → 「提示词模板库」",
        "- 关键字字典：`index.html` → 「提示词关键字字典」",
        f"- 本 skill 包：`ai-video-skills/{s['id']}/`",
        "",
    ]
    return "\n".join(lines)


def templates_md(s: dict) -> str:
    lines = [
        f"# {s['displayName']} · 提示词模板",
        "",
        f"演示图：`../../assets/{s['demo']}`",
        "",
        f"**风格锁定：** {s['style_lock']}",
        "",
    ]
    for title, scene, prompt in s["templates"]:
        lines += [
            f"## {title}",
            "",
            f"画面：{scene}",
            "",
            "```text",
            prompt,
            "```",
            "",
        ]
    return "\n".join(lines)


def main():
    PACK.mkdir(parents=True, exist_ok=True)
    CLAUDE.mkdir(parents=True, exist_ok=True)

    index_rows = []
    for s in SKILLS:
        # pack folder
        pdir = PACK / s["id"]
        pdir.mkdir(parents=True, exist_ok=True)
        (pdir / "SKILL.md").write_text(skill_md(s), encoding="utf-8")
        (pdir / "templates.md").write_text(templates_md(s), encoding="utf-8")
        loc = pdir / "locales"
        loc.mkdir(exist_ok=True)
        meta = {"displayName": s["displayName"], "brief": s["brief"]}
        (loc / "zh-CN.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
        (loc / "en-US.json").write_text(json.dumps(
            {"displayName": s["id"].replace("-", " ").title(), "brief": s["brief"]},
            ensure_ascii=False, indent=2), encoding="utf-8")

        # loadable project skill
        cdir = CLAUDE / s["id"]
        cdir.mkdir(parents=True, exist_ok=True)
        shutil.copy2(pdir / "SKILL.md", cdir / "SKILL.md")
        cloc = cdir / "locales"
        cloc.mkdir(exist_ok=True)
        shutil.copy2(loc / "zh-CN.json", cloc / "zh-CN.json")
        shutil.copy2(loc / "en-US.json", cloc / "en-US.json")

        demo_exists = (ASSETS / s["demo"]).exists()
        index_rows.append((s, demo_exists))

    # README
    readme = [
        "# AI 视频提示词 Skill 包",
        "",
        "本文件夹保存各风格的 **提示词 Skill**。每个风格一套，可直接改模板生成视频。",
        "",
        "## 加载位置",
        "",
        "- 项目内可读包：`ai-video-skills/<style-id>/`",
        "- MiMo Desktop 项目技能：`.claude/skills/<style-id>/`（含 `SKILL.md` + `locales/`）",
        "- 新建技能后需 **新开对话** 才会在插件/技能列表生效",
        "",
        "## 演示图",
        "",
        "统一放在 `assets/` 下（`style-*.png` / `tpl-*.png`），模板内以路径引用。",
        "",
        "## 风格一览",
        "",
        "| ID | 名称 | 演示图 | 模板数 |",
        "|----|------|--------|--------|",
    ]
    for s, ok in index_rows:
        mark = "有" if ok else "缺失"
        readme.append(f"| `{s['id']}` | {s['displayName']} | `{s['demo']}` ({mark}) | {len(s['templates'])} |")
    readme += [
        "",
        "## 使用方式",
        "",
        "1. 在 Agent 中描述：「用 cinematic-realism 模板做一条雨夜人物镜头」",
        "2. 或直接打开对应文件夹复制 `templates.md` 中的 prompt",
        "3. 配套网页手册：项目根目录 `index.html`（关键字字典 + 模板库）",
        "",
    ]
    (PACK / "README.md").write_text("\n".join(readme), encoding="utf-8")

    print(f"skills={len(SKILLS)}")
    print(f"pack={PACK}")
    print(f"claude={CLAUDE}")
    missing = [s["id"] for s, ok in index_rows if not ok]
    print("missing_demo=" + (",".join(missing) if missing else "none"))


if __name__ == "__main__":
    main()
