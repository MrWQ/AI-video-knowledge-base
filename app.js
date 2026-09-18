/* AI Video Factors knowledge base interactions */

(function () {
  const $ = (sel, root = document) => root.querySelector(sel);
  const $$ = (sel, root = document) => Array.from(root.querySelectorAll(sel));

  // Sticky TOC scroll spy
  const tocLinks = $$(".toc nav a");
  const sections = tocLinks
    .map((a) => {
      const id = a.getAttribute("href")?.replace("#", "");
      const el = id ? document.getElementById(id) : null;
      return el ? { id, el, a } : null;
    })
    .filter(Boolean);

  function setActive(id) {
    tocLinks.forEach((a) => {
      a.classList.toggle("active", a.getAttribute("href") === `#${id}`);
    });
  }

  if ("IntersectionObserver" in window && sections.length) {
    const io = new IntersectionObserver(
      (entries) => {
        const visible = entries
          .filter((e) => e.isIntersecting)
          .sort((a, b) => b.intersectionRatio - a.intersectionRatio);
        if (visible[0]) setActive(visible[0].target.id);
      },
      { rootMargin: "-15% 0px -60% 0px", threshold: [0.1, 0.25, 0.5] }
    );
    sections.forEach(({ el }) => io.observe(el));
  }

  // Play / pause camera demos
  function setAllPaused(paused) {
    $$(".demo-card .monitor").forEach((m) => {
      m.classList.toggle("cam-paused", paused);
      const btn = $(".monitor-toggle", m);
      if (btn) btn.textContent = paused ? "播放" : "暂停";
    });
    const master = $("#btn-pause-all");
    if (master) {
      master.textContent = paused ? "全部播放" : "全部暂停";
      master.classList.toggle("is-on", paused);
    }
  }

  $$(".monitor-toggle").forEach((btn) => {
    btn.addEventListener("click", () => {
      const monitor = btn.closest(".monitor");
      if (!monitor) return;
      const paused = monitor.classList.toggle("cam-paused");
      btn.textContent = paused ? "播放" : "暂停";
    });
  });

  $("#btn-pause-all")?.addEventListener("click", () => {
    const anyPlaying = $$(".demo-card .monitor").some(
      (m) => !m.classList.contains("cam-paused")
    );
    setAllPaused(anyPlaying);
  });

  $("#btn-play-all")?.addEventListener("click", () => setAllPaused(false));

  // Option chip details
  $$("[data-chip-group]").forEach((group) => {
    const chips = $$(".chip", group);
    const detail = $(".chip-detail", group);
    if (!detail) return;

    function activate(chip) {
      chips.forEach((c) => c.classList.toggle("is-active", c === chip));
      const zh = chip.dataset.zh || chip.querySelector(".zh")?.textContent || "";
      const en = chip.dataset.en || chip.querySelector(".en")?.textContent || "";
      const desc = chip.dataset.desc || "";
      const tips = chip.dataset.prompt || "";
      detail.innerHTML =
        `<div><strong>${zh}</strong> <span class="term">${en}</span></div>` +
        (desc ? `<div style="margin-top:6px;color:var(--muted)">${desc}</div>` : "") +
        (tips
          ? `<div style="margin-top:8px;font-family:var(--font-mono);font-size:12px;color:var(--teal)">prompt: ${tips}</div>`
          : "");
    }

    chips.forEach((chip) => {
      chip.addEventListener("click", () => activate(chip));
    });

    const first = chips.find((c) => c.classList.contains("is-active")) || chips[0];
    if (first) activate(first);
  });

  // Copy prompt templates
  $$(".copy-btn").forEach((btn) => {
    btn.addEventListener("click", async () => {
      const box = btn.closest(".prompt-box");
      const text = box?.querySelector(".prompt-text")?.textContent || box?.textContent.replace("复制", "").trim();
      if (!text) return;
      try {
        await navigator.clipboard.writeText(text.trim());
        btn.textContent = "已复制";
      } catch {
        const ta = document.createElement("textarea");
        ta.value = text.trim();
        document.body.appendChild(ta);
        ta.select();
        document.execCommand("copy");
        ta.remove();
        btn.textContent = "已复制";
      }
      setTimeout(() => {
        btn.textContent = "复制";
      }, 1600);
    });
  });

  // Smooth active for map cards
  $$(".map-card[href^='#']").forEach((a) => {
    a.addEventListener("click", () => {
      const id = a.getAttribute("href")?.replace("#", "");
      if (id) setActive(id);
    });
  });
})();
