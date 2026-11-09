/* Pan, zoom, and fullscreen for Mermaid blocks and linked diagram SVGs. */
(function () {
  function stageFor(img) {
    var view = document.createElement("figure");
    view.className = "diagram-view";
    var bar = document.createElement("div");
    bar.className = "diagram-toolbar";
    [["In", 1.2], ["Out", 1 / 1.2], ["Fit", 0]].forEach(function (pair) {
      var b = document.createElement("button");
      b.type = "button";
      b.textContent = pair[0];
      b.addEventListener("click", function () {
        if (pair[1] === 0) fit();
        else zoomAt(view._s.x, view._s.y, pair[1]);
      });
      bar.appendChild(b);
    });
    var full = document.createElement("button");
    full.type = "button";
    full.textContent = "Full screen";
    full.addEventListener("click", function () {
      if (document.fullscreenElement === view) document.exitFullscreen();
      else view.requestFullscreen();
    });
    bar.appendChild(full);
    var stage = document.createElement("div");
    stage.className = "diagram-stage";
    var cap = document.createElement("figcaption");
    cap.className = "diagram-caption";
    view.appendChild(bar);
    view.appendChild(stage);
    view.appendChild(cap);
    view._s = { x: 0, y: 0, k: 1, node: null };
    function apply() {
      var n = view._s.node;
      if (!n) return;
      n.style.transform = "translate(" + view._s.x + "px," + view._s.y + "px) scale(" + view._s.k + ")";
    }
    function fit() {
      var n = view._s.node;
      if (!n) return;
      var sw = stage.clientWidth;
      var sh = stage.clientHeight;
      var nw = n.scrollWidth || n.getBoundingClientRect().width || sw;
      var nh = n.scrollHeight || n.getBoundingClientRect().height || sh;
      view._s.k = Math.min(sw / nw, sh / nh, 1);
      view._s.x = Math.max(0, (sw - nw * view._s.k) / 2);
      view._s.y = Math.max(0, (sh - nh * view._s.k) / 2);
      apply();
    }
    function zoomAt(cx, cy, factor) {
      var next = Math.min(6, Math.max(0.3, view._s.k * factor));
      var r = next / view._s.k;
      view._s.x = cx - (cx - view._s.x) * r;
      view._s.y = cy - (cy - view._s.y) * r;
      view._s.k = next;
      apply();
    }
    stage.addEventListener("wheel", function (e) {
      e.preventDefault();
      var rect = stage.getBoundingClientRect();
      zoomAt(e.clientX - rect.left, e.clientY - rect.top, e.deltaY < 0 ? 1.1 : 0.9);
    }, { passive: false });
    var drag = null;
    stage.addEventListener("pointerdown", function (e) {
      drag = { x: e.clientX, y: e.clientY, ox: view._s.x, oy: view._s.y };
      stage.classList.add("is-grabbing");
      stage.setPointerCapture(e.pointerId);
    });
    stage.addEventListener("pointermove", function (e) {
      if (!drag) return;
      view._s.x = drag.ox + (e.clientX - drag.x);
      view._s.y = drag.oy + (e.clientY - drag.y);
      apply();
    });
    stage.addEventListener("pointerup", function () {
      drag = null;
      stage.classList.remove("is-grabbing");
    });
    view._fit = fit;
    view._mount = function (node, caption) {
      view._s.node = node;
      stage.appendChild(node);
      if (caption) cap.textContent = caption;
    };
    return view;
  }

  function mountImage(link) {
    var img = link.querySelector("img");
    if (!img) return;
    var view = stageFor();
    var host = link.parentElement && link.parentElement.tagName === "P" ? link.parentElement : link;
    var cap = host.nextElementSibling;
    var caption = "";
    if (cap && (cap.tagName === "EM" || (cap.tagName === "P" && cap.querySelector("em") && cap.textContent === cap.querySelector("em").textContent))) {
      caption = cap.textContent;
      cap.remove();
    }
    host.parentNode.insertBefore(view, host);
    if (host !== link) host.remove();
    else link.remove();
    img.style.width = (img.naturalWidth || 1000) + "px";
    view._mount(img, caption);
    var open = document.createElement("a");
    open.className = "diagram-open";
    open.href = link.getAttribute("href");
    open.target = "_blank";
    open.rel = "noopener";
    open.textContent = "Open vector";
    view.querySelector(".diagram-toolbar").appendChild(open);
    if (img.complete) view._fit();
    else img.addEventListener("load", function () { view._fit(); });
  }

  function mountMermaid(code) {
    var pre = code.parentElement;
    var view = stageFor();
    var holder = document.createElement("div");
    holder.className = "mermaid";
    holder.textContent = code.textContent;
    pre.parentNode.insertBefore(view, pre);
    pre.remove();
    view._mount(holder, "");
    return holder;
  }

  document.querySelectorAll(".entry a[href$='.svg']").forEach(mountImage);

  var blocks = document.querySelectorAll(".entry pre code.language-mermaid");
  if (!blocks.length) return;
  var s = document.createElement("script");
  s.src = "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js";
  s.onload = function () {
    var nodes = [];
    blocks.forEach(function (code) { nodes.push(mountMermaid(code)); });
    window.mermaid.initialize({ startOnLoad: false, theme: "dark", securityLevel: "strict" });
    window.mermaid.run({ nodes: nodes }).then(function () {
      document.querySelectorAll(".diagram-view").forEach(function (view) {
        if (view._fit) view._fit();
      });
    });
  };
  document.body.appendChild(s);
})();
